# Создание системы регистрации пользователя с применением класса
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
        print(self.data)

    def numbers(self):
        x = 0
        for char in self:
            if char.isnumeric():
                x +=1
        return x

    def upper_char(self):
        x = 0
        for char in self:
            if char.isupper():
                x +=1
        return x

    def lower_char(self):
        x = 0
        for char in self:
            if char.islower():
                x += 1
        return x

    def valid_password(self):
        if len(self) < 8:
            print('Пароль должен быть не менее 8 символов')
            return False

        elif Database.numbers(self) == 0:
            print('Пароль должен содержать хотя бы одну цифру')
            return False

        elif Database.upper_char(self) == 0 or Database.lower_char(self) == 0:
            print('Пароль должен содержать хотя бы одну заглавную и строчную букву')
            return False
        else:
            return True

class User:
    '''
    Класс пользователя содержащий атрибуты: логин, пароль

    '''

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ =='__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n '))
        if choice == 1:
            login = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                else:
                    print('Неправильный пароль')
            else:
                print('Пользователь не найден')

        if choice == 2:
            user = User(input('Введите имя пользователя: '), password := input('Введите пароль: '),
                        password2 :=  input('Повторите пароль: '))
            if password != password2:
                print('Введенные пароли не совпадают')
                continue
            if Database.valid_password(user.password):
                database.add_user(user.username, user.password)
                # print(database.data)





