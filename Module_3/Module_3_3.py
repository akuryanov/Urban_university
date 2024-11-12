def print_param(a = 1, b = 'string', c = True):
    print(a, b, c)

print_param()
print_param(2)
print_param(2, 'B')
print_param(2, 'B', False)
print_param('строка')
print_param(b = 25)
c = [1, 2, 3]
print_param(c = [1, 2, 3])

values_list = [5, 'string_list', True]
values_dict = {'a' : 3, 'b' : 'string_dict', 'c' : False}
print_param(*values_list)
print_param(**values_dict)
print_param(*values_dict)

values_list2 = [8, 'string_list-2', 42]
print_param(*values_list2)
