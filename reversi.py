board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]


class Board:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        """ draw the play board """
        print('  a b c d e f g h')
        for num_line, line in enumerate(self.board):
            print(num_line + 1, ' '.join(line))
    

def main():
    play_board = Board(board)
    play_board.draw_board()


if __name__ == '__main__':
    main()