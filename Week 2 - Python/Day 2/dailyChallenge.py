matrix = [['7', 'i', 'i'],
          ['T', 's', 'x'],
          ['h', '%', '?'],
          ['i', ' ', '#'],
          ['s', 'M', ' '],
          ['$', 'a', ' '],
          ['#', 't', '%'],
          ['^', 'r', '!']]



secretMessage = str()
for column in range(0, len(matrix[0])):
    for row in range(0, len(matrix)):
        if matrix[row][column].isalpha():
            secretMessage += matrix[row][column]
        else: secretMessage += ' '

print(secretMessage)