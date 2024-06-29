import random


class Game:
    def get_user_item(self):
        uItem = ''
        while uItem not in ['r', 'p', 's']:
            uItem = input('Select Rock, Paper or Scissor (r/p/s): ')
        return uItem

    def get_computer_item(self):
        cItem = random.choice(['r', 'p', 's'])
        return cItem

    def get_game_result(self, user_item, computer_item):
        result = ''
        if user_item == 'r':
            if computer_item == 'r':
                result = 'Draw'
            elif computer_item == 'p':
                result = 'Loss'
            else:
                result = 'Win'

        if user_item == 'p':
            if computer_item == 'r':
                result = 'Win'
            elif computer_item == 'p':
                result = 'Draw'
            else:
                result = 'Loss'

        if user_item == 's':
            if computer_item == 'r':
                result = 'Loss'
            elif computer_item == 'p':
                result = 'Win'
            else:
                result = 'Draw'

        return result


    def play(self):
        uItem = self.get_user_item()
        cItem = self.get_computer_item()
        result = self.get_game_result(uItem, cItem)
        print('You selected {}, the computer selected {}. Result {}'.format(uItem, cItem, result))
        return(result)