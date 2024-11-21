from math import inf

def divide(first, second):
    try:
        result = first / second
        print(f'{first} / {second} = {result}')
    except ZeroDivisionError:
        print(f'{first} / {second} = {inf}')