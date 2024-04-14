from game import Game

def get_user_menu_choice():
    print()
    print('1. Play a new game')
    print('2. Show scores')
    print('3. Quit')

def print_results(results):
    print('Total games playes: {}'.format(results['Win']+results['Loss']+results['Draw']))
    print('Games you won: {}'.format(results['Win']))
    print('Games you lost: {}'.format(results['Loss']))
    print('Games you drew: {}'.format(results['Draw']))
    print('Thanks for playing!')

def main():
    print('Rock-Paper-Scissors')
    op = 0
    while op != 3:
        while op not in [1, 2, 3]:
            get_user_menu_choice()
            op = int(input('Option: '))
        if op == 1:
            g = Game()
            result = g.play()
            results[result] += 1
        if op == 2:
            print_results(results)
        if op == 3:
            print_results(results)
            break
        op = 0

results = {
    'Win': 0,
    'Loss': 0,
    'Draw': 0
}

main()