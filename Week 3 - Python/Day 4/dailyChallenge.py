import math

class Pagination():
    def __init__(self, items:list=None, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.actualPage = 1
        self.nPages = math.ceil(len(items) / pageSize)

    def getVisibleItems(self):
        aux = self.actualPage * self.pageSize
        print(self.items[aux-self.pageSize:aux])
        
    def prevPage(self):
        self.actualPage -= 1

    def nextPage(self):
        self.actualPage += 1

    def firstPage(self):
        self.actualPage = 1
    
    def lastPage(self):
        self.actualPage = self.nPages

    def goToPage(self, n):
        if n > self.nPages:
            n = self.nPages
        if n <= 0:
            n = 1
        self.actualPage = n


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

p.getVisibleItems()

p.nextPage()
p.getVisibleItems()

p.goToPage(15)
p.getVisibleItems()

p.prevPage()
p.getVisibleItems()