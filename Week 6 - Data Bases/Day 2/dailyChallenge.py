import requests
import json
import random
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE = 'API'

   
try:
    connection = psycopg2.connect(
        dbname = DATABASE,
        user = USERNAME,
        password = PASSWORD,
        host = HOSTNAME
    )
except Exception as e:
    print(f"Error: {e}")

page = 'https://restcountries.com/v3.1/all'
response = requests.get(page)

data = json.loads(response.content)

numbers = []
while len(numbers) < 10:
    n = random.randint(0, 249)  
    if n not in numbers:
      numbers.append(n)

for n in numbers:
    country = data[n]
    name = country['name']['common']
    capital = ''.join(country['capital'])
    flag = country['flags']['png']
    subregion = country['subregion']
    population = country['population']

    cursor = connection.cursor()
    query = "INSERT INTO country (name, capital, flag, subregion, population) VALUES ('{}', '{}', '{}', '{}', {});".format(name, capital, flag, subregion, population) 
    #print(query)
    cursor.execute(query)
    connection.commit()
    
connection.close()
