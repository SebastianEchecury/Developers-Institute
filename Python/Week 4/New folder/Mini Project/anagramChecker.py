fileName = 'C:\\Users\\Lenovo\\Desktop\\Developers Institute\\Curso\\Python\\Week 4\\New folder\\sowpods.txt'

class AnagramChecker:
    def __init__(self) -> None:
        with open(fileName, 'r') as f:
            self.words = f.read().split('\n')

    def isValidWord(self, word):
        if word.upper() in self.words:
            return True
        else:
            return False
        
    def getAnagrams(self, word):
        anagrams = list()
        for w in self.words:
            if self.isAnagram(w, word.upper()):
                anagrams.append(w)
        anagrams.remove(word.upper())
        return anagrams
    
    @staticmethod
    def isAnagram(w1, w2):
        if sorted(w1) == sorted(w2):
            return True
    
    
        
"""
a = AnagramChecker()
#print(a.words[0])

word = input('Enter a word: ')
print('Valid word: {}'.format(a.isValidWord(word)))
print('Anagrams:')
print(a.getAnagrams(word))
"""