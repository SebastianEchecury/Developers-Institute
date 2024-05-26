import menu_item as mi

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = mi.getConnection()
        cursor = conn.cursor()
        query = "SELECT * FROM menu_items WHERE item_name = '{}'".format(name) 
        cursor.execute(query)
        item = cursor.fetchone()
        #print(item)
        conn.close()
        if item != None:
            return mi.MenuItem(item[1], item[2])
        else: 
            return None
        
    @classmethod
    def all_items(cls):
        itemsList = list()
        conn = mi.getConnection()
        cursor = conn.cursor()
        query = "SELECT * FROM menu_items"
        cursor.execute(query)
        items = cursor.fetchall()
        for row in items:
            itemsList.append(mi.MenuItem(row[1], row[2]))
        conn.close()
        return(itemsList)    
        

#item = MenuManager().get_by_name("Ensalada2")
#print(item)


#items = MenuManager().all_items()
#for i in items:
#    print(i)