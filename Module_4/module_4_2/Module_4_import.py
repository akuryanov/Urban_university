from dis import dis

def say_hi():
    print('Привет это функция say_hi() модуль_4_import')

def main():
    a = 5
    b= 10
    print('Hi, I am main()')

if __name__ == '__main__':
     main()
     say_hi()


dis(say_hi)