## Exercise 1
"""
import random

fileName = 'C:\\Users\\Lenovo\\Desktop\\Developers Institute\\Curso\\Python\\Week 4\\Day 4\\words.txt'

def get_words_from_file(fileName):
    with open(fileName, 'r') as f:
        words = f.readlines()
    return words

def get_random_sentence(cant, words):
    sentence = ''
    for n in range(0, cant):
        aux = random.randint(0, len(words)-1)
        sentence += words[aux].strip() + ' '
    return sentence.lower()

def main(fileName):
    print('Hello, welcome!')
    print('In this program we will create a sentence with random words and a length you will specify')
    print('The length of the sentence must be between 2 and 20')

    flag = False
    while not flag:
        cant = int(input("How long the sentence should be? "))
        if cant >= 2 and cant <= 20:
            flag = True
            words = get_words_from_file(fileName)
            print(get_random_sentence(cant, words))
        else:
            print('Wrong number!')


main(fileName)

"""

## Exercise 2
"""
import json
sampleJson = { 
                "company":{ 
                    "employee":{ 
                        "name":"emma",
                        "payable":{ 
                            "salary":7000,
                            "bonus":800
                        }
                    }
                }
            }

print(sampleJson["company"]["employee"]["payable"]["salary"])
sampleJson["company"]["employee"]["birth_date"] = 'dd/mm/YYYY'

jsonFile = 'file.json'

with open(jsonFile, 'w') as file_obj:
    json.dump(sampleJson, file_obj, indent = 2, sort_keys=True)
"""