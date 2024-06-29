## Exercise 1
"""
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

b = Bengal('Pancho', 2)   
c = Chartreux('Manchas', 3) 
s = Siamese('Pelusa', 3)
allCats = [b, c, s]

saraPets = Pets(allCats)
saraPets.walk()
"""

## Exercise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print('{} is barking'.format(self.name))

    def runSpeed(self):
        return self.weight/self.age*10
    
    def fight(self, anotherDog): 
        if (self.runSpeed()*self.weight) > (anotherDog.runSpeed()*anotherDog.weight):
            print('{} won'.format(self.name))
        else:
            print('{} won'.format(anotherDog.name))

d1 = Dog('Pancho', 2, 10)
d2 = Dog('Ronan', 4, 25)
d3 = Dog('Barto', 4, 22)

d1.fight(d3)



