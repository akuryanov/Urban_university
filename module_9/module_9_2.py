first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elem) for elem in first_strings if len(elem) > 5]
print(first_result)

second_result = [(elem_first, elem_second) for elem_first in first_strings for elem_second in second_strings
                 if len(elem_first) == len(elem_second)]
print(second_result)

third_strings = first_strings + second_strings
third_result = {elem: len(elem) for elem in third_strings if len(elem) % 2 == 0}
print(third_result)