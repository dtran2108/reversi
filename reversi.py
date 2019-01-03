board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]

directions = [(-1, 0), (0,  1),
              ( 1, 0), (0, -1),
              ( 1, 1), (-1,-1),
              (-1, 1), (1, -1)]


class Player:
    def __init__(self, player):
        self.player_name = player
    
    def __repr__(self):
        return self.player_name


class Board:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        """ draw the play board """
        print('  a b c d e f g h')
        for num_line, line in enumerate(self.board):
            print(num_line + 1, ' '.join(line))

    def update_board(self):
        """ update the board """ 
        pass

    def find_valid_move(self):
        pass
    

def main():
    play_board = Board(board)
    play_board.draw_board()


if __name__ == '__main__':
    main()