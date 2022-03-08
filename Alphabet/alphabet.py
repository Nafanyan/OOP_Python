import string


class Alphabet:
    def __init__(self):
        self.lang = 'rus'
        self.letters = 'абвгдеёжзийклрмнопрстуфхцчшщъыьэюя'
    def print(self):
        for i in self.letters:
            print (i, end='')
        print()
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):

    __letters_num = 26
    def __init__(self, us_lang):
        super().__init__()
        if us_lang == 'en': self.letters = string.ascii_uppercase

    def is_en_letter(self, letter):
        if (letter.upper() in self.letters): return True
        else: return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print( 'Hi, its me, Mario!')


if __name__=='__main__':
    eng = EngAlphabet('en')
    eng.print()
    print(eng.letters_num())
    print(eng.is_en_letter('F'))
    print(eng.is_en_letter('Щ'))
    eng.example()



