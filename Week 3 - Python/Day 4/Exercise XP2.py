## Exercise 3
"""
from ExerciseXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dogNames = self.name
        for name in args:
            dogNames += (' ' + name)
        print('{} plays all together'.format(dogNames))

    def doATrick(self):
        tricks = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained:
            nr = random.randint(0, 3)
            print(self.name + ' ' + tricks[nr])

pd = PetDog('Renzo', 4, 25)
pd.play('Barto', 'Polvillo')

#pd.train()
pd.doATrick()
"""

## Exercise 4

class Family:
    def __init__(self, members:list=[], lastname=''):
        self.members = members
        self.lastname = lastname

    def born(self, **kwargs):
        self.members.append(kwargs)
        print('Congratulations!')

    def is18(self, name):
        for m in self.members:
            if m['name'] == name:
                if m['age'] > 18:
                    return True
                else:
                    return False
                
    def familyPresentation(self):
        print('Family: {}'.format(self.lastname))
        for m in self.members:
            print(m)
"""
f = Family(lastname='Cosme fulanito')



f.born(name='Michael', age=35, gender='Male', is_child=False)
f.born(name='Sarah', age=32, gender='Female', is_child=False)

f.is18('Sarah')

f.familyPresentation()
"""

## Exercise 5

class TheIncredibles(Family):
    def __init__(self, members: list = [], lastname=''):
        super().__init__(members, lastname)

    def usePower(self):
        for m in self.members:
            if m['age'] < 18:
                raise('{} its not over 18'.format(m['name']))
            else:
                print('{} superpower is {}'.format(m['name'], m['power']))

    def incrediblePresentation(self):
        print('Here is our powerful family ')
        super().familyPresentation()


increibles = TheIncredibles(lastname='The Incredibles')

increibles.born(name='Michael', age=35, gender='Male', is_child=False, power='fly', incredible_name='MikeFly')
increibles.born(name='Sarah', age=32, gender='Female', is_child=False, power='read minds', incredible_name='SuperWoman')
 
increibles.incrediblePresentation()

increibles.born(name='Jack', age=1, gender='Male', is_child=False, power='unknown', incredible_name='Baby Jack')

increibles.incrediblePresentation()