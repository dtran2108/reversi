#!/usr/bin/env python

class Player:
    def __init__(self, player):
        self.player_name = player
    
    def __repr__(self):
        return self.player_name


class Board:
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

    def draw_board(self):
        """ draw the play board """
        print('  a b c d e f g h')
        for num_line, line in enumerate(self.board):
            print(num_line + 1, ' '.join(line))

    def update_board(self):
        """ update the board """ 
        self.board[1][1] = 'W'
        pass

    @staticmethod
    def isOnBoard(x, y):
        """ returns True if the coordinates are located on the board """
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def is_valid_moves(self, tile, xstart, ystart):
        """ find the valid moves for player """
        if self.board[xstart][ystart] != '.' or not self.isOnBoard(xstart, ystart):
            return False
        # temporarily set the tile on the board
        self.board[xstart][ystart] = tile

        if tile == 'W':
            otherTile = 'B'
        else:
            otherTile = 'W'
        tilesToFlip = []

        for xdirection, ydirection in self.directions:
            x, y = xstart, ystart
            x += xdirection
            y += ydirection
            if self.isOnBoard(x, y) and self.board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not self.isOnBoard(x, y):
                    continue
                while self.board[x][y] == otherTile:
                    x += xdirection
                    y += ydirection
                    if not self.isOnBoard(x, y):
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self.board[x][y] == tile:
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

        self.board[xstart][ystart] = '.'
        if len(tilesToFlip) == 0:
            return False
        return tilesToFlip
    

def main():
    play_board = Board()
    play_board.draw_board()
    play_board.update_board()
    print('updated')
    play_board.draw_board()


if __name__ == '__main__':
    main()