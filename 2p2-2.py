import string
import os


class ReadFile:
    """Contains the name of file and counts number of characters, words and sentences inside"""
    def __init__(self, file_name):
        """Checks file opening process

        Checks if a name of file was entered; if it has str type; if this directory exists;
        if file is *.txt format; if it isn't empty

        :param file_name: name of file *.txt
        :type file_name: str
        """
        if not file_name:
            raise ValueError("no file name was entered")
        if not isinstance(file_name, str):
            raise TypeError("file name must be str")
        if not os.path.exists(file_name):
            raise OSError("File/directory does not exist")
        if not file_name.endswith(".txt"):
            raise TypeError("file must be *.txt")
        if not os.path.getsize(file_name):  # ==0
            raise OSError("File is empty")
        self.file_name = file_name

    @property
    def chars_num(self) -> int:
        """Counts characters in file

        Splits file into lines to read it separately, counting all the characters in each line.
        Removes all whitespaces and counts the line length.

        :returns: number of characters
        :rtype: int
        """
        f = open(self.file_name, 'r')
        characters = 0
        while True:
            line = f.readline()
            if not line:
                break
            characters += len(line.replace(' ', ''))
        f.close()
        return characters

    @property
    def words_num(self) -> int:
        """Counts words in file

        Splits file into lines to read it separately.

        :returns: number of words
        :rtype: int
        """
        f = open(self.file_name, 'r')
        words = 0
        while True:
            line = f.readline()
            if not line:
                break
            words += sum([i.strip(string.punctuation).isalpha() for i in line.split()])
        f.close()
        return words

    @property
    def sents_num(self) -> int:
        """Counts sentences in file

        Splits file into lines to read it separately. Counts all points, question marks
        and exclamation marks inside each line.

        :returns: number of sentences
        :rtype: int
        """
        f = open(self.file_name, 'r')
        sentences = 0
        while True:
            line = f.readline()
            if not line:
                break
            sentences += line.count('.') + line.count('?') + line.count('!')
        f.close()
        return sentences


x = ReadFile("smth.txt")
print(f'chars: {x.chars_num}')
print(f'words: {x.words_num}')
print(f'sentences: {x.sents_num}')
