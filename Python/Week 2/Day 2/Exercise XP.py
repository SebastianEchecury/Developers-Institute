"""
## Exercise 1
def display_mesasge():
    print("We are learning python")

display_mesasge()

## Exercise 2
def favorite_book(title:str):
    print("One of mi favorite books is {}".format(title))

favorite_book('Harry Potter')

## Exercise 3
def describe_city(city:str, country:str = 'Argentina'):
    print('{} is in {}'. format(city, country))

describe_city('Rosario')

## Exercise 4
import random

numberRandom = random.randint(1, 101)
numberUser = int(input('Enter a number between 1 and 100: '))

if numberRandom == numberUser:
    print('They are the same number')
else:
    print('They are different')
    print('The number you entered: {}. Number generated: {}'. format(numberUser, numberRandom))


## Exercise 5
def make_shirt(**kwargs):#(size:str, message:str):
    if kwargs['size'] == 'large' or kwargs['size'] == 'medium':
        kwargs['message'] = 'I love Python'
    print("The size of the shirt is {} and the text is {}".format(kwargs['size'], kwargs['message']))

make_shirt(size = 'small', message = 'asd')
"""


## Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(mList:list):
    for magician in mList:
        print(magician)

show_magicians(magician_names)

def make_great(mList:list):
    for x in range(0, len(mList)):
        mList[x] = mList[x] + ' The Great'
    return mList

make_great(magician_names)
show_magicians(magician_names)