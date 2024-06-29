from collections import Counter 

listStopWords = list()

class Text:
    def __init__(self, text):
        self.__text = text

    def wordFrequency(self, word):
        words = self.__text.lower().split(' ')
        return words.count(word)
    
    def mostCommonWord(self):
        #print(self.__text.lower())
        words = self.__text.lower().split(' ')
        #print(words)
        c = Counter(words)
        mostFrequent, count = c.most_common(1)[0]
        print('The most frequente word is "{}" with {} appearences'.format(mostFrequent, count))
    
    def listOfWords(self):
        words = self.__text.lower().split(' ')
        uniqueWords = set(words)
        print(uniqueWords)

    @classmethod
    def from_file(cls):
        string = ''
        for line in open("C:\\Users\\Lenovo\\Desktop\\Developers Institute\\Curso\\Python\\Week 4\\Day 4\\the_stranger.txt"):
            aux = line.replace('\n', '')
            aux2 = aux[0:len(aux)-1]
            if len(aux2) > 1:
                string += ''.join(aux2)
        #print(string)
        return Text(string)
    
    def getText(self):
        return self.__text
        

text = 'A good book, would sometimes cost: as much as a good house.'
t = Text(text)
"""
print(t.wordFrequency('a'))
t.mostCommonWord()
t.listOfWords()

#Text.from_file()
newT = Text.from_file()
newT.mostCommonWord()
newT.listOfWords()
"""


class TextModification(Text):

    def removePunctuation(self):
        return self.getText().replace('.', '')
    
    def removeSpecialCharacters(self):
        aux = ''
        for l in self.getText():
            if not l.isalnum():
                aux += ' '
            else: aux += l
        return aux

    
    def removeStopWords(self):
        lAux = self.__text.split(' ')
        aux = list()
        for word in lAux:
            if word not in listStopWords:
                aux.append(word)
        return ''.join(aux)
    

t2 = TextModification(text)
print('Get Text')
print(t2.getText())
print('Remove Punctuation')
print(t2.removePunctuation())
print('Remove special ')
print(t2.removeSpecialCharacters())