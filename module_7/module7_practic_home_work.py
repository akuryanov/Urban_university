import sys
import tkinter
from tkinter import filedialog # Диалоговые окна при работе с файлами
from tkinter import messagebox

import os

class File:
    def __init__(self):
        self.current_path = os.getcwd()

    def file_select(self):
        self.file_name = filedialog.askopenfilename(initialdir=self.current_path, title='Выберите файл',
                                               filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*.*')))
        return self.file_name

    def open_file(self):
        self.file_select()

        if self.file_name:
            self.file = open(self.file_name, 'r')

            text.delete(1.0, 'end')
            text.insert(1.0, self.file.read())

    def save_file(self):

        str_ = text.get(1.0, 'end')
        self.file.write(str_)


    def close_file(self):
        text.delete(1.0, 'end')
        self.file.close()


    def exit(self):
        sys.exit()

def info():
    info = '''
    Для открытия окна воспользуйтесь пунктом <Open> меню <File>\n
    Для сохранения изменений воспользуйтесь пунктом <Save> меню <File>\n
    Для закрытия файла воспользуйтесь пунктом <Close> меню <File>
    '''

    messagebox.showinfo('info', info)

def about():
    about = f'Приложение для просмотра документов\n{chr(169)} А. Курьянов\nВерсия 1.0'
    messagebox.showinfo('about', about, icon='error')

file = File()

window = tkinter.Tk()  # создание окна
window.title('Проводник')  # Заголовок окна

window.geometry('400x400')  # Размеры окна
window.configure(bg='silver')
window.resizable(False, False)  # Запрет изменения размеров окна

# Блок кнопок
#------------------------------------------------------------------
frame_button=tkinter.Frame(background='silver')
frame_button.pack()
button_open=tkinter.Button(frame_button, text='Открыть...', command=file.open_file).pack(side=['left'])
button_close=tkinter.Button(frame_button, text='Закрыть...', command=file.close_file).pack(side=['left'])

#------------------------------------------------------------------

# Текстовое окно
#------------------------------------------------------------------

text = tkinter.Text(window)
text.pack(side='left')

#------------------------------------------------------------------

# Меню окна
#------------------------------------------------------------------
menu_bar = tkinter.Menu()

help_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu = tkinter.Menu(menu_bar, tearoff=0)

file_menu.add_command(label='Open', command=file.open_file)
file_menu.add_command(label='Save')
file_menu.add_command(label='Close', command=file.close_file)

file_menu.add_separator()
file_menu.add_command(label='Exit', command=file.exit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu.add_command(label='Info', command=info)
help_menu.add_command(label='About', command=about)
menu_bar.add_cascade(label='Help', menu=help_menu)

window.config(menu=menu_bar)
#------------------------------------------------------------------


window.mainloop()

