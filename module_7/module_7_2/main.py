def custom_write(file_name, strings):
    file = open(file_name, 'w')
    strings_positions = {}

    for i in range(len(strings)):
        tuple_ = (i+1, file.tell())
        file.write(str(strings[i]) + '\n')
        str_ = {tuple_: strings[i]}
        strings_positions.update(str_)

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)