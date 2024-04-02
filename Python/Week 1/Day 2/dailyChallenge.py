import random

print("Enter a string of 10 characters:")
string = input()

if len(string) == 10:
    print("Perfect string")
elif len(string) > 10:
    print("string not long enough")
else:
    print("string too long")

print("First letter: {}. Last letter: {}".format(string[0], string[-1]))

for x in range(len(string)+1):
    print(string[:x])

sShuffled = ''.join(random.sample(string, len(string)))
print(sShuffled)
