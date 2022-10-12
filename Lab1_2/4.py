from os.path import exists as file_exists

class TextFileProcessing:
    def __init__(self, file_name):
        if not file_exists(file_name):
            raise FileNotFoundError('File not found')
        self.__file = file_name

    def __str__(self):
        return f'Words: {self.words_count()}\
                \nCharacters: {self.characters_count()}\
                \nSentences : {self.sentences_count()}'

    def words_count(self):
        with open(self.__file) as file:
            data = file.read()
            lines = data.split()
            words_num = len(lines)
            return words_num

    def characters_count(self):
        with open(self.__file) as file:
            data = file.read().replace(' ', '')
            characters_num = len(data)
            return characters_num

    def sentences_count(self):
        with open(self.__file) as file:
            data = file.read()
            sentences_count = sum(map(data.count, ['.', '!', '?']))
            return sentences_count
