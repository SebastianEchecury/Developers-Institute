## Part 1 : Quizz :
"""
What is a class?
A template definition of the methods and variables in a particular kind of object

What is an instance?
Is a specific occurrence or copy of an object that is created from a class

What is encapsulation?
Encapsulation is the practice of bundling related data into a structured unit, along with the methods used to work with that data

What is abstraction?
The ability to hide complex implementation details and show only the necessary features of an object

What is inheritance?
The ability to inherit the properties and methods of an existing class

What is multiple inheritance?
The ability to inherit the properties and methods from more than one parent object or parent class

What is polymorphism?
The ability of something to have or to be displayed in more than one form

What is method resolution order or MRO?
MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy
"""

## Part 2
import itertools
import random


class Card:
    def __init__(self):
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Deck:
    def __init__(self, c:Card):
        self.cards = ['{} {}'.format(carta[0], carta[1]) for carta in itertools.product(c.suit, c.value)]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            

    def deal(self):
        aux = random.randint(0, 51)
        print('You card is {}'.format(self.cards[aux]))
        self.cards.pop(aux)

