import os
import csv
import pandas as pd

class Trades:
    def __init__(self):
        self.directory = os.getcwd() + '/trades/'
        self.files = os.listdir(self.directory)  # Список файлов в каталоге trades
        self.volant = []
        self.files_null = []


    def run(self):
        for file in self.files:
            file_name = os.path.join(self.directory, file)  # Полный путь к файлу
            with open(file_name) as file_scv:
                a = pd.read_csv(file_scv)
                a.head()
                price = a['PRICE']
                ticker = a['SECID']
                min_ = min(price)
                max_ = max(price)

                average_price = (max_ + min_) / 2
                volatility = ((max_ - min_) / average_price) * 100

                if volatility == 0:
                    self.files_null.append(ticker)
                else:
                    self.volant.append(volatility)

        # list_ = str(self.files_null)
        # print(f'Нулевая волатильность: {list_}')
        print(self.files_null)




if __name__ == '__main__':
    trades = Trades()
    trades.run()















