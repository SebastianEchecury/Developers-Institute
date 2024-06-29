board = [
    [' ', '|', ' ', '|', ' '],
    ['-', '-', '-', '-', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '-', '-', '-', '-'],
    [' ', '|', ' ', '|', ' ']
]

def displayBoard(board):
    print('BOARD')
    for x in board:
        print(''.join(x))

def playerInput(value:str, board:list):
    print()
    row = int(input('Enter row: '))
    column = int(input('Enter column: '))
    row = adaptColRow(row)
    column = adaptColRow(column)
    updateBoard(column, row, value, board)

def updateBoard(column:int, row:int, value:str, board:list):
    board[row][column] = value


def adaptColRow(number:int):
    if number == 1:
        realN = 0
    elif number == 2:
        realN = 2
    elif number == 3:
        realN = 4
    return realN

def play():
    print("TIC TAC TOE")
    print()
    print('Player 1 (X) Player 2 (O)')
    win = False
    lastPlayer = '2'
    plays = 0
    while not win and plays < 9:
        lastPlayer = '1' if lastPlayer == '2' else '2'
        print('Player {} its your turn'.format(lastPlayer))
        value = 'X' if lastPlayer == '1' else 'O'
        playerInput(value, board)
        displayBoard(board)
        win = checkWin(board)
        plays += 1
        if plays == 9:
            print('Game tied')

def checkWin(board:list):
    winner = False
    for x in range(1, 4):
        chars1 = ''
        chars2 = ''
        for y in range(1, 4):
            chars1 += board[adaptColRow(x)][adaptColRow(y)]
            chars2 += board[adaptColRow(y)][adaptColRow(x)]
        if chars1 == 'XXX' or chars2 == 'XXX':
            print('Player 1 wins!')
            winner = True
        if chars1 == 'OOO' or chars2 == 'OOO':
            print('Player 2 wins!')
            winner = True
        if winner:
            break
    return winner

play()