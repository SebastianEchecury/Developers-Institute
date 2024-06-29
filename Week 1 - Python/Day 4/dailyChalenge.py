"""
Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples
number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]


number = int(input("Enter a number: "))
length = int(input("Enter a lenght: "))
multiples = list()

for x in range(1, length+1):
    multiples.append(number * x)

print(multiples)
"""

"""
Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples
user's word : "ppoeemm" ➞ "poem"
user's word : "wiiiinnnnd" ➞ "wind"
user's word : "ttiiitllleeee" ➞ "title"
user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


string = input("Enter a string: ")
uniqueChars = list()

for x in string:
    if x not in uniqueChars:
        uniqueChars.append(x)

string = ''.join(uniqueChars)
print(string)
"""