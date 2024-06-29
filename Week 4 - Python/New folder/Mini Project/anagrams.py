from anagramChecker import AnagramChecker

def isAValidWord(word):
    wAux = word.strip()
    if len(wAux.split(' ')) > 1:
        print('Just one word')
        return False
    if not wAux.isalpha():
        return False
    return True

valid = False
finish = False
while not finish:
    while not valid:
        word = input('Enter a word(exit to finish): ')
        if isAValidWord(word):
            valid = True
    if word == 'exit':
        finish = True 
    else:
        a = AnagramChecker()  
        print('Your word: {}'.format(word))
        if (a.isValidWord(word)):
            print('This is a valid english word')
            words = a.getAnagrams(word)
            print('Anagrams for your word:')
            for w in words:
                print(w)
        else:
            print('This is not a valid english word')
    valid = False
