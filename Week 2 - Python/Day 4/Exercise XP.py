## Exercise 1
"""
import random

def get_random_temp(season:str):
    minT = float()
    maxT = float()
    if season == 'winter':
        minT = -10
        maxT = 16
    elif season == 'summer':
        minT = 18
        maxT = 40
    elif season == 'autumn':
        minT = 5
        maxT = 18
    elif season == 'spring':
        minT = 13
        maxT = 28
    return round(random.uniform(minT, maxT), 1)

def main():

    monthNumber = int(input('Enter the number of the month: '))
    if monthNumber in [12, 1, 2]: season = 'summer'
    elif monthNumber in [3, 4, 5]: season = 'autumn'
    elif monthNumber in [6, 7, 8]: season = 'winter'
    else: season = 'spring'
    temperature = get_random_temp(season)
    if temperature < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif temperature < 16:
        print('Quite chilly! Don’t forget your coat')
    elif temperature < 23:
        print('Between 16 and 23')
    elif temperature < 32:
        print('Between 23 and 32')
    else:
        print('Between 32 and 40')


    
    print('The temperature right now is {} degrees Celsius.'.format(temperature))

main()
"""

## Exercise 2
"""
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def resultUser():
    print('Total questions: {}. Answers right: {}. Answers wrong: {}'.format(len(data), len(data)-errors, errors))
    print('List of wrong questions')
    print()
    for x in range(0, len(wrongAnswers)):
        print('Question: {}'.format(questions[x]))
        print('Right answer: {}'.format(correctAnswer[x]))
        print('Your answer: {}'.format(wrongAnswers[x]))

def makingQuestions():
    for q in data:
        print(q['question'])
        answer = input('Whats the answer? ')
        if not answer == q['answer']:
            global errors 
            errors += 1
            wrongAnswers.append(answer)
            questions.append(q['question'])
            correctAnswer.append(q['answer'])
    resultUser()

playAgain = 'Y'
while playAgain == 'Y':
    errors = 0
    wrongAnswers = list()
    questions = list()
    correctAnswer = list()
    makingQuestions()
    playAgain = 'N'
    if errors >= 3:
        playAgain = input(print('Do you want to play again? Y/N'))
"""

## Exercise 3
"""
from datetime import date

def getAge(birthDate:date):
    today = date.today()
    age = today.year - birthDate.year
    return age

def canRetire(gender:str, birthDate:date):
    age = getAge(birthDate)
    print(age)
    if (gender == 'm' and age >= 67): canRetire = True
    if (gender == 'f' and age >= 62): canRetire = True
    return canRetire

gender = input("Enter gender (m/f): ")
year = int(input("Age of birth: "))
month = int(input("Month of birth: "))
day = int(input("Day of birth: "))

if canRetire(gender, date(year, month, day)):
    print('Can retire')
else:
    print('Cant retire')
"""

## Exercise 4
def operation(number:str):
    n = int(number)
    n2 = int(number*2)
    n3 = int(number*3)
    n4 = int(number*4)
    return n + n2 + n3 + n4

print(operation(input('Enter a number: ')))