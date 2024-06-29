import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE = 'restaurant'

def getConnection():
        try:
            connection = psycopg2.connect(
                dbname = DATABASE,
                user = USERNAME,
                password = PASSWORD,
                host = HOSTNAME
                )
        except Exception as e:
            print(f"Error: {e}")
        return connection


class MenuItem:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    def __str__(self):
        return "Name: {}. Price: {}".format(self.name, self.price)



def saveItem(i:MenuItem):
    conn = getConnection()
    cursor = conn.cursor()
    query = "INSERT INTO {} (item_name, item_price) VALUES ('{}', {});".format('menu_items', i.name, int(i.price)) 
    # print(query)
    cursor.execute(query)
    conn.commit()
    conn.close()

def deleteItem(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = "DELETE FROM {} WHERE item_name = '{}';".format('menu_items', name) 
    #print(query)
    cursor.execute(query)
    conn.commit()
    conn.close()

def updateItem(item:MenuItem, item2:MenuItem):
    conn = getConnection()
    cursor = conn.cursor()
    query = "UPDATE {} SET item_name = '{}', item_price = {} WHERE item_name = '{}' AND item_price = {};".format('menu_items', item2.name, int(item2.price), item.name, int(item.price))
    #print(query)
    cursor.execute(query)
    conn.commit()
    conn.close()

#item = MenuItem('Ensalada', 10)
#saveItem(item)
#deleteItem(3)
#item.name = 'Ensalada2'
#updateItem(item, 4)