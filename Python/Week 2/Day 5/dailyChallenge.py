## Challenge 1
sequence = input('Enter a comma separated sequence of words: ')
words = sequence.split(',')
print(sorted(words))


## Challenge 2
sentence = input('Enter a sentence: ')
words = sentence.split(' ')

longestword = ''
for word in words:
    if len(word) > len(longestword):
        longestword = word

print('The longest word its: {}'.format(longestword))