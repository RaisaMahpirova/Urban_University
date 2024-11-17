class WordsFinder:
    def __init__(self, *files_names):
        self.files_names = files_names

    def get_all_words(self):
        all_words = {}
        names = []
        words = []
        for i in self.files_names:
            names.append(i)
            words_in_file = []
            with open(i, encoding='utf-8') as file:
                words_in_lines = []
                for lines in file:
                    line = lines.lower()
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(symbol, ' ')
                    _line = line.split()
                    for word in line.split():
                        words_in_lines.append(word)

                for word in words_in_lines:
                    words_in_file.append(word)

            all_words[i] = words_in_file
        return all_words

    def find(self, word):
        the_dict = self.get_all_words()
        for name, words in the_dict.items():
            if word.lower() in the_dict[name]:
                result = {name: the_dict[name].index(word.lower()) + 1}
                return result

    def count(self, word):
        the_dict = self.get_all_words()
        for name, words in the_dict.items():
            if word.lower() in the_dict[name]:
                result = {name: the_dict[name].count(word.lower())}
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
