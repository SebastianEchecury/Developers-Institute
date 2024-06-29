## Exercise 1 
"""
class Currency:
    def __init__(self, currency, amount:int):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1:
            currency = self.currency + 's'
        else: currency = self.currency
        return '{} {}'.format(self.amount, currency)
    
    def __int__(self) -> int:
        return self.amount
    
    def __repr__(self) -> str:
        if self.amount > 1:
            currency = self.currency + 's'
        else: currency = self.currency
        return '{} {}'.format(self.amount, currency)
    
    def __add__(self, other) -> int:
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError('Cannot add between Currency type <dollar> and <shekel>')
        return int(self) + int(other)
    
    def __iadd__(self, other):
        self.amount = self.amount + int(other)
        return self



    #Your code starts HERE

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

print(c1+5)

print(c1+c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)


c1 + c3
"""

## Exercise 2
"""
from func import func

func()
"""

## Exercise 3
"""
import string
import random


letters = string.ascii_letters  # Contiene todas las letras mayúsculas y minúsculas
print(''.join(random.choice(letters) for x in range(5)))
"""

## Exercise 4
"""
import datetime
print(datetime.date.today())
"""

## Exercise 5
"""
import datetime
date = datetime.datetime.strptime('01-01-2025',"%d-%m-%Y" )
dif = date - datetime.datetime.today()
print('The 1st of January is in {}'.format(dif))
"""

## Exercise 6
"""
from datetime import datetime

def minutesLived(birthDate):
    date1 = datetime.today() 
    diferencia = date1 - birthDate
    return diferencia.total_seconds() / 60

birthDate = input('Enter date of birth (dd/mm/yyyy): ')
birthDate = datetime.strptime(birthDate,"%d/%m/%Y")
minutesLived = minutesLived(birthDate)
print("Minutes lived:", minutesLived)
"""

## Exercise 7
from faker import Faker

f = Faker()
users = list()

def addFakeUser(users):
    user = dict()
    user['name'] = f.name()
    user['adress'] = f.address()
    #user['langage_code'] = 
    users.append(user)

addFakeUser(users)
addFakeUser(users)
for u in users:
    print(u)
