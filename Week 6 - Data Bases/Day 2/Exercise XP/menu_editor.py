import menu_manager as mm
import menu_item as mi

def show_user_menu():
    op = ''
    while op != 'X':
        while op not in ['v', 'A', 'D', 'U', 'S', 'X']:
            showOptions()
            op = input('Enter option: ')
        
        if op == 'V':
            pass
        if op == 'A':
            add_item_to_menu()
        if op == 'D':
            remove_item_from_menu()
        if op == 'U':
            update_item_from_menu()
        if op == 'S':
            items = mm.MenuManager.all_items()
            for i in items:
                print(i)
        if op == 'X':
            items = mm.MenuManager.all_items()
            for i in items:
                print(i)
            break
        print('')
        op = ''

def add_item_to_menu():
    name = input('Enter name: ')
    price = int(input('Enter price: '))

    item = mi.MenuItem(name, price)
    mi.saveItem(item)

    print('item was added successfully')

def remove_item_from_menu():
    name = input('Enter name: ')
    try:
         mi.deleteItem(name)
         print('Item deleted')
    except Exception as e:
        print(f"Error: {e}")

def update_item_from_menu():
    name = input('Enter name: ')
    price = int(input('Enter price: '))
    item = mi.MenuItem(name, price)

    name = input('Enter new name: ')
    price = int(input('Enter new price: '))
    item2 = mi.MenuItem(name, price)
    try:
         mi.updateItem(item, item2)
         print('Item updated')
    except Exception as e:
        print(f"Error: {e}")

def showOptions():
    print('View an Item (V)')
    print('Add an Item (A)')
    print('Delete an Item (D)')
    print('Update an Item (U)')
    print('Show the Menu (S)')
    print('Exit (X)')


if __name__ == "__main__":
    show_user_menu()