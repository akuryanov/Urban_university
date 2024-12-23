class WordsFinder:
    def __init__(self, *file):
        self.file = file
        # self.line_ = []
        # self.all_words = {}

    def get_all_words(self):
        all_words = {}
        for file_name in self.file:
            line_ = []
            with open(file_name,  encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.split()
                    for i in range(len(line)):
                        line_.append(line[i])
            all_words.update({file_name: line_})

        return all_words

    def find(self, word):
        word = word.lower()
        content = self.get_all_words()

        for name, words in content.items():
            if word in words:
                positions = words.index(word)
                return {name: positions + 1}

    def count(self, word):
        word = word.lower()
        content = self.get_all_words()
        for name, words in content.items():
            if word in words:
                counts = words.count(word)
                return {name: counts}


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



