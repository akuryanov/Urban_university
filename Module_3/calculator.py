import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())  # Получение значения из текстового поля number1_entry и преобразование в int
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(values):
    answer_entry.delete(0, 'end') # Очистка окна вывода
    answer_entry.insert(0, values) # Вывод результат в окно вывода answer_entry

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk() # Создаем графическое окно
window.title('Калькулятор') # Задаем имя окна
window.geometry('350x350') # Задаем размер окна
window.resizable(False, False) # Запрещаем изменять размеры окна по горизонтали и вертикали


number1_entry = tk.Entry(window, width=28) # Создаем поле ввода

number1_entry.place(x=100, y=75) # Устанавливаем положение поля ввода

number2_entry = tk.Entry(window, width=28) # Создаем поле ввода

number2_entry.place(x=100, y=130) # Устанавливаем положение поля ввода

answer_entry = tk.Entry(window, width=28) # Создаем поле вывода
answer_entry.place(x=100, y = 200)


button_add = tk.Button(window, text='+', width=2, height=2, command=add) # Создаем кнопку
button_add.place(x=100, y=250) # Устанавливаем положение кнопки
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub) # Создаем кнопку
button_sub.place(x=150, y=250) # Устанавливаем положение кнопки
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul) # Создаем кнопку
button_mul.place(x=200, y=250) # Устанавливаем положение кнопки
button_div = tk.Button(window, text='/', width=2, height=2, command=div) # Создаем кнопку
button_div.place(x=250, y=250) # Устанавливаем положение кнопки



number1 = tk.Label(window, text='Введите целое число')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите целое число')
number2.place(x=100, y=105)

answer_ = tk.Label(window, text='Ответ:')
answer_.place(x=100, y=175)
window.mainloop() # Цикл обновления графического окна
