# Challenge 1
"""
word = input("Enter a word: ")
wordDict = dict()

for idx, x in enumerate(word):
    if x not in wordDict:
        wordDict[x] = list()
    wordDict[x].append(idx)

print(wordDict)
"""

# Challenge 2
"""
def convertToNumber(string:str):
    string = string.replace('$', '')
    string = string.replace(',', '')
    #print(string)
    return int(string)

def isAffordable(price:int, budget:int):
    if price <= budget:
        return True
    else: return False

def affordableItems(dictionary:dict, budget:int):
    affordableItemsList = list()
    for item in dictionary:
        #print("Item {}, precio {}, presupuesto {}". format(item, convertToNumber(dictionary[item]), convertToNumber(budget)))
        if isAffordable(convertToNumber(dictionary[item]), convertToNumber(budget)):
            affordableItemsList.append(item)
    print(sorted(affordableItemsList))


items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

affordableItems(items_purchase, wallet)
# ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

affordableItems(items_purchase, wallet)
# ["Apple", "Bananas", "Fan", "Honey", "Spoon"]



items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

affordableItems(items_purchase, wallet)
# "Nothing"
"""