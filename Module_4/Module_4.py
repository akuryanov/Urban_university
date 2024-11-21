# Модули и пакеты
import Module_4_import as m_4_1 # Присваиваем имя m_4_1

print('Привет это модуль_4')
print(m_4_1.a)
m_4_1.say_hi()


from Module_4_import import * # Импортируем всё из Module_4_1
from Module_4_import import say_hi, a, b # Импортируем только необходимые элементы


# при импорте модулей интерпретатор сначала выполняет все
# действия из импортируемого модуля
# Если необходимо, чтобы действия из импортируемого модуля не выполнялись,
# необходимо добавить в импортируемый модуль следующую конструкцию
#
# if __name__ == '__main__':
#     main()
#     say_hi()
# то есть включить вызов функций в проверку условия

import Module_4_import
# Для вызова функции, необходимо будет указать ее явно
Module_4_import.say_hi()
Module_4_import.main()

# или

from Module_4_import import say_hi, main
say_hi()
main()

# Можно присвоить псевдоним импортируемой функции
from Module_4_import import say_hi as sh
sh()

