class Alphabet:
    def __init__(self):
        self.lang = 'rus'
        self.letters = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','р','м','н','о','п',
                        'р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    def print(self):
        for i in self.letters:
            print (i, end=' ')
    def letters_num(self):
        return len(self.letters)


if __name__=='__main__':
    rus = Alphabet()
    rus.print()
    print(rus.letters_num())


