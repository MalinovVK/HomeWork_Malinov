class WordsFinder:
    def __init__(self, *names):
        # Принимаем неограниченное количество файлов и сохраняем их в атрибут file_names
        self.names = names

    def get_all_words(self):
        punct_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.names:
            with open(file_name, encoding='utf-8') as file:
                elem = file.read().lower()
                for char in punct_:
                    elem = elem.replace(char, '')
                elements = elem.split()
                all_words[file_name] = elements
        return all_words
    def find(self, word):
        find_ = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            index = words.index(word.lower()) + 1
            find_[file_name] = index
        return find_
    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        return result

with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write("""It's a text for task.
    Найти везде и использовать его для самопроверки.
    Успехов в решении задачи.
    Text text text.""")

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))