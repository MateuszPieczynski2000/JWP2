class OX:
    ALL_SPACES = list('123456789')
    X, O, BLANK = 'X', 'O', ' '

    def __init__(self):
        self.__board = {}
        for space in OX.ALL_SPACES:
            self.__board[space] = OX.BLANK

    def __str__(self):
        return f'''
                {self.__board['1']}|{self.__board['2']}|{self.__board['3']} 1 2 3 
                -+-+- 
                {self.__board['4']}|{self.__board['5']}|{self.__board['6']} 4 5 6 
                -+-+- 
                {self.__board['7']}|{self.__board['8']}|{self.__board['9']} 7 8 9'''

    def is_valid_space(self, space):
        if space is None:
            return False
        return space in OX.ALL_SPACES or self.__board[space] == OX.BLANK

    def is_winner(self, player):
        b, p = self.__board, player
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def is_board_full(self):
        for space in OX.ALL_SPACES:
            if self.__board[space] == OX.BLANK:
                return False
        return True

    def update_board(self, space, mark):
        self.__board[space] = mark


def main():
    print('Witaj w grze kółko i krzyżyk!')
    ox = OX()
    current_player, next_player = OX.X, OX.O

    while True:
        print(ox)

        move = None
        while not ox.is_valid_space(move):
            print(f'Jaki jest ruch gracza {current_player}? (1-9)')
            move = input()

        ox.update_board(move, current_player)

        if ox.is_winner(current_player):
            print(ox)
            print(current_player + ' wygrał grę!')
            break
        elif ox.is_board_full():
            print(ox)
            print('Gra zakończyła się remisem!')
            break

        current_player, next_player = next_player, current_player
    print('Dziękuję za grę!')


if __name__ == '__main__':
    main()
