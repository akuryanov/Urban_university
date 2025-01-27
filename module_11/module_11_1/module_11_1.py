# Домашнее задание по теме "Обзор сторонних библиотек Python"

import pandas as pd
import datetime

def get_new_file():
    input_file = 'data_file.xlsx'

    df = pd.ExcelFile(input_file)
    sheet_name = df.sheet_names

    path = './Files/'
    for name in sheet_name:
        if name != 'Содержание':
            parsing = pd.ExcelFile(input_file).parse(sheet_name = name)
            value = parsing.iloc[0, 0]
            value = value[-11:-1]
            year = value[-4:]
            month = value[-7:-5]
            day =  value[-10:-8]
            date_value = year+'.'+month+'.'+day
            print(date_value)

            parsing.drop(parsing.index[0:4], axis=0, inplace=True)
            parsing.drop(parsing.index[109:], axis=0, inplace=True)
            parsing.pop('Unnamed: 1')  # Удалить столбец B
            parsing.pop('Unnamed: 3')  # Удалить столбец D

            parsing.rename(columns={'К содержанию ':'Наименование', 'Unnamed: 2':'Значение'}, inplace=True)


            value = datetime.datetime.strptime(value, '%d.%m.%Y') # Преобразование даты из строки в формат даты

            parsing['Дата'] = value
            parsing.to_excel(path+'Цены'+'_'+date_value+'.xlsx', index=False)


get_new_file()