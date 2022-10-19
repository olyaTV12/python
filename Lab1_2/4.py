from os.path import exists as file_exists
import re

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
        words = 0
        with open(self.__file) as f:
            for lines in f:
                words += len(lines.split())
        return words

    def characters_count(self):
        chars = 0
        with open(self.__file) as f:
            for line in f:
                chars += sum(1 for c in line if c != ' ')
            return chars

    def sentences_count(self):
        sentences = 0
        with open(self.__file) as f:
            for lines in f:
                if not lines.endswith('.' or '!' or '?'):
                    sentences -= 1
                sentences += len(re.split(r"[.!?]+", lines))
        return sentences
