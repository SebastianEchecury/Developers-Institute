## Exercise 1
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


c1 = Cat('Pepito', 5)
c2 = Cat('Bigotes', 2)
c3 = Cat('IPA', 7)
cats = [c1, c2, c3]

def findOldestCat(cats:list):
    aux = 0
    for cat in cats:
        if cat.age > aux:
            cAux = cat
    return cAux

oldestCat = findOldestCat(cats)
print('The oldest cat is {}, and is {} years old'.format(oldestCat.name, oldestCat.age))
"""

## Exercise 2
"""
class Dog:
    def __init__(self, dogName, dogHeight):
        self.name = dogName
        self.height = dogHeight

    def bark(self):
        print('{} goes woof!'.format(self.name))
    
    def jump(self):
        print('{} jumps {} cm high!'.format(self.name, self.height*2))

davidsDog = Dog('Rex', 50)

print(davidsDog.name)
print(davidsDog.height)
print(davidsDog.bark())
print(davidsDog.jump())

sarasDog = Dog('Teacup', 20)

print(sarasDog.name)
print(sarasDog.height)
print(sarasDog.bark())
print(sarasDog.jump())

if sarasDog.height > davidsDog.height:
    print('Saras dog is bigger')
else: 
    print('Davis dog is bigger')
"""

## Exercise 3
"""
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singMeASong(self):
        for x in self.lyrics:
            print(x)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.singMeASong()
"""

## Exercise 4
"""
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = list()
        self.animalsDict = dict()

    def addAnimals(self, newAnimal):
        self.animals.append(newAnimal)

    def getAnimals(self):
        for a in self.animals:
            print(a)

    def sellAnimal(self, animalSold):
        self.animals.remove(animalSold)

    def sortAnimals(self):
        aux = ''
        cont = 0
        for a in sorted(self.animals):
            if a[0] != aux:
                cont += 1
                self.animalsDict[cont] = list()
                self.animalsDict[cont].append(a)
                aux = a[0]
            else:
                self.animalsDict[cont].append(a)
            
    def getGroups(self):
        print(self.animalsDict)

z1 = Zoo('ramatGanSafari')

z1.addAnimals('Leon')
z1.addAnimals('Oso')
z1.addAnimals('Leopardo')
z1.addAnimals('Elefante')
z1.addAnimals('Tortuga')
z1.addAnimals('Toro')

z1.getAnimals()

z1.sortAnimals()

z1.getGroups()
"""