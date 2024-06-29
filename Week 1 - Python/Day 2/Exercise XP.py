## Exercise XP

## Exercise 1
for x in range(4):
    print("Hello world")


## Exercise 2
print((99**3)*8)    


## Exercise 3
print(5 < 3)
print(3 == 3)
print(3 == "3")
##print("3" > 3)
print("Hello" == "hello")

## Exercise 4
computerBrand = "Lenovo"
print("I have a {} computer".format(computerBrand))


## Exercise 5
name = "Seba"
age = 27
shoeSize = 10.5
info = "I love dogs"
print("My name is {}, I am {} years old, my shoe size is {} and a fun fact about me is {}.". format(name, age, shoeSize, info))


## Exercise 6
a = 15
b = 8
if a > b:
    print("Hello world")


## Exercise 7
print("Enter a number")
number = int(input())

if (number % 2) == 0:
    print("Even number")
else:
    print("Odd number")
 

## Exercise 8
print("Write your name: ")
name8 = input()
if name == name:
    print("We have the same name!")


## Exercise 9
print("Enter your height in cm:")
height = int(input())
if height > 145:
    print("You can ride")
else:
    print("You are not tall enough")



## Exercise XP Gold
    
## Exercise 1
print("Hello world" * 4 + " I love python" * 4)


## Exercise 2
print("enter a number between 1 and 12:")
month = int(input())

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month >= 12 and month <= 2:
    print("Winter")