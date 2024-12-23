class WordsFinder:
    def __init__(self, *file):
        self.file = file

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        str_ = ''
        for file_name in self.file:
            line_ = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower() # Переводим строки в нижний регистр
                    str_ += line # Объединяем все строки в одну
                for i in str_:
                    if i in punct:
                        str_ = str_.replace(i, '')  # Удаляем знаки препинания
                dict_ = str_.split() # Переводим строку в список слов

                all_words.update({file_name: dict_}) # создаем словарь, где ключ - имя файла, значение - список слов файла
                str_ = ''

        return all_words

    def find(self, word):
        word = word.lower()
        dict_ = {}
        content = self.get_all_words()
        for file, words in content.items():
            if word in words:
                positions = words.index(word)
                dict_.update({file: positions + 1})
        return dict_

    def count(self, word):
        dict_ = {}
        word = word.lower()
        content = self.get_all_words()
        for self.file, words in content.items():
            # counts = 0
            if word in words:
                counts = words.count(word)
                dict_.update({self.file: counts})

        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())

print(finder2.find('TEXT'))
print( finder2.count('Text'))

finder2 = WordsFinder('file_1.txt', 'file_2.txt', 'file_3.txt')

print(finder2.get_all_words())
print(finder2.find('Text_2_2'))
print(finder2.find('Text_1_1'))
print(finder2.find('Text_3_2'))
print(finder2.find('Text_3_7'))
print(finder2.count('Text_3_7'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('The'))
print(finder1.count('THE'))






