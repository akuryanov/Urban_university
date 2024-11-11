def string_info(string):
    global calls
    number_of_characters = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    count_calls()
    return number_of_characters, string_upper, string_lower

def is_contains(string, list_to_search):
    global calls
    for str_of_list in list_to_search:
        list_to_search = (str_of_list.lower())

    if string.lower() in list_to_search:
        output_str = True
    else:
        output_str = False
    count_calls()
    return output_str

def count_calls():
    global calls
    calls += 1
    return calls

calls = 0


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)