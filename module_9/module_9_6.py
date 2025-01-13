# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:i + j + 1]

a = all_variants("abcdef")

for i in a:
    print(i)