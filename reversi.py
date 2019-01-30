#!/usr/bin/env python
from board import Board


def main():
        board = Board()
        while not board.gameOver():
                board.draw_board()
                board.go_player('W')
                board.draw_board()
                board.go_player('B')
        board.draw_board()
        board.getScore()


if __name__ == '__main__':
    main()