print('Hello, ' + 'word')
print('Меня зовут %s, мне %s лет'% ('Денис', 14)) # Устаревшее форматирование строк
print('Меня зовут %(name)s, мне %(year)s лет'% {'name' :'Денис','year': 14}) # Устаревшее форматирование строк
# Новый метод через .format
print('Я учусь в {title}-{postfix} {title}'.format(title='Урбан', postfix='Univercity'))

# еще один новый метод
print(f'{"Urban " *2}- это лучший университет')