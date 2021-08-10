"""
    This file is to decode umlauts from a file
    Exchange:
        -  'ÃŸ' -> ß
        -  'Ã„' -> Ä
        -  'Ã¤' -> ä
        -  'Ãœ' -> Ü
        -  'Ã¼' -> ü
        -  'Ã–' -> Ö
        -  'Ã¶' -> ö

        -  'Ue' -> Ü
        -  'ue' -> ü
        -  'Oe' -> Ö
        -  'oe' -> ö
        -  'Ae' -> Ä
        -  'ae' -> ä
        -  'ss' -> ß


    Just put the output from the text file into the class and get the encoded string with the function .encode() back

"""

__date__ = '09.07.2021'
__completed__ = '13.07.2021'
__work_time__ = 'about 2 Hours'
__author__ = 'Christof Haidegger'
__version__ = '1.0'
__licence__ = 'Common Licence'
__debugging__ = 'Christof Haidegger'

import re


class Encode_umlauts:
    """
        This is the class to encode the Umlauts from a read text file
    """
    def __init__(self, string):
        """
            -> to get the encoded string run the .encode function

        :param string: string to encode
        :type: string
        """
        self.string = string

    def refactor(self, indexes, new_letter):
        """

        :param indexes:    indexes are the points where the umlauts are
        :param new_letter: is the letter which is to replace (example: ä)
        :return:           the new word with the replaced letters
        """
        string_list = list(self.string)
        for index in indexes:
            string_list[index] = new_letter  # refactor the first letter of the umlaut code
            string_list[index + 1] = ''  # ignore the second letter of the umlaut code

        return ''.join(string_list)  # join the single letters

    def rebuild(self, word):
        umlaut_codes = ['ÃŸ', 'Ã„', 'Ã¤', 'Ãœ', 'Ã¼', 'Ã–', 'Ã¶', 'Ae', 'ae', 'Ue', 'ue', 'Oe', 'oe']
        refactor_letters = ['ß', 'Ä', 'ä', 'Ü', 'ü', 'Ö', 'ö', 'Ä', 'ä', 'Ü', 'ü', 'Ö', 'ö']

        for refactor_letter, umlaut_code in zip(refactor_letters, umlaut_codes):
            if word.find(umlaut_code) != -1:
                word = self.refactor(self.get_all(umlaut_code), refactor_letter)  # refactor the string
        if word.isalpha() is True:
            return word

        else:
            new_word = ''
            for letter in list(word):
                if letter.isascii() is True:
                    new_word += letter
                else:
                    print('put letter: ', letter, ' away from string')
                    new_word += ''
            return new_word

    def get_all(self, umlaut_code):
        """

        :param umlaut_code: code for the umlaut (example: Ã„)
        :return:            the indexes, where the umlauts are
        """
        return [i.start() for i in re.finditer(umlaut_code, self.string)]  # list with indexes of the umlauts

    def encode(self):
        """

        :return: the new encoded words with the right umlauts
        """

        single_words = self.string.split()
        new_string = ''

        for counter, word in enumerate(single_words):
            if word.isascii() is True:
                if counter > 0:
                    if (single_words[counter - 1].find('/') == -1 and single_words[counter - 1].find('\\') == -1) \
                            or (single_words[counter - 1].find('/') != 0 and single_words[counter - 1].find('\\') != 0):
                        new_string += ' ' + word
                    else:
                        new_string += word
                else:
                    new_string += word
            else:
                if counter > 0:
                    if (single_words[counter - 1].find('/') == -1 and single_words[counter - 1].find('\\') == -1) \
                            or (single_words[counter - 1].find('\\') != 0 and single_words[counter - 1].find('/') != 0):
                        new_string += ' ' + self.rebuild(word)
                    else:
                        new_string += self.rebuild(word)
                else:
                    new_string += self.rebuild(word)

        self.string = new_string

        return self.string

    def headless_encode(self):
        """
        :return: the new encoded words with the right umlauts
        """

        exception_words = ['Bergbauernbuam', 'Queens']
        umlaut_codes = ['ÃŸ', 'Ã„', 'Ã¤', 'Ãœ', 'Ã¼', 'Ã–', 'Ã¶', 'Ae', 'ae', 'Ue', 'ue', 'Oe', 'oe']
        refactor_letters = ['ß', 'Ä', 'ä', 'Ü', 'ü', 'Ö', 'ö', 'Ä', 'ä', 'Ü', 'ü', 'Ö', 'ö']

        single_words = self.string.split()

        for counter, word in enumerate(single_words):
            self.string = word
            if word in exception_words:
                continue
            for refactor_letter, umlaut_code in zip(refactor_letters, umlaut_codes):
                if word.find(umlaut_code) != -1:
                    word = self.refactor(self.get_all(umlaut_code), refactor_letter)  # refactor the string
                    print(word)
                    single_words[counter] = word

        self.string = ' '.join(single_words)
        return self.string


def main():
    """

    : -> to test the class Encode_umlauts()
    """
    data = open('text_file.txt', 'r')
    string = data.read()
    data.close()
    encoded = Encode_umlauts(string)
    print('with encode: \n', encoded.encode())

    return 0


if __name__ == '__main__':
    main()
