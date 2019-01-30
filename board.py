from player import Player


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
    
    col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = ['1', '2', '3', '4', '5', '6', '7', '8']

    def draw_board(self):
        """ draw the play board """
        print('  ' + ' '.join(self.col))
        for lineNum, line in enumerate(self.board):
            print(self.row[lineNum], ' '.join(line))
    
    def gameOver(self):
        """ return true if both players cannot play """
        if not self.get_valid_moves('W') and not self.get_valid_moves('B'):
            return True

    @staticmethod
    def moveCoordinate(x, y, dirX, dirY):
        """ change the x, y coordinate """
        plus_x, plus_y = x + dirX, y + dirY
        minusX, minusY = x - dirX, y - dirY
        return plus_x, plus_y, minusX, minusY

    @staticmethod
    def onBoard(x, y):
        """ returns True if the coordinates are located on the board """
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def is_valid_moves(self, tile, xstart, ystart):
        """ find the valid moves for player """
        if self.board[xstart][ystart] != '.' or not self.onBoard(xstart, ystart):
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
            x, y, _, _ = self.moveCoordinate(x, y, xdirection, ydirection)
            if self.onBoard(x, y) and self.board[x][y] == otherTile:
                x, y, _, _ = self.moveCoordinate(x, y, xdirection, ydirection)
                if not self.onBoard(x, y):
                    continue
                while self.board[x][y] == otherTile:
                    x, y, _, _ = self.moveCoordinate(x, y, xdirection, ydirection)
                    if not self.onBoard(x, y):
                        break
                if not self.onBoard(x, y):
                    continue
                if self.board[x][y] == tile:
                    while True:
                        _, _, x, y = self.moveCoordinate(x, y, xdirection, ydirection)
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

        self.board[xstart][ystart] = '.'
        if not tilesToFlip:
            return False
        return tilesToFlip

    def get_valid_moves(self, tile):
        """ returns list of valid moves """      
        valid_moves = []
        validMoves = []
        for x in range(8):
            for y in range(8):
                if self.is_valid_moves(tile, x, y):
                    valid_moves.append([x, y])
        for move in valid_moves:
            validMoves.append(self.col[move[1]] + self.row[move[0]])
        validMoves.sort()
        return validMoves
    
    def print_validChoice(self, tile):
        """ display the valid choices """
        valid_moves = self.get_valid_moves(tile)
        if len(valid_moves) == 1:
            print('Valid choice: {}'.format(' '.join(valid_moves)))
        else:
            print('Valid choices: {}'.format(' '.join(valid_moves)))
    
    def check_playerInput(self, tile, playerInput):
        """ check if the player's input is valid """
        if playerInput in self.get_valid_moves(tile):
            return True

    def makeMove(self, tile, choice):
        """ place the tile on xstart, ystart position
            and flip any of the opponent's pieces """
        ystart = self.col.index(choice[0])
        xstart = self.row.index(choice[1])
        tilesToFlip = self.is_valid_moves(tile, xstart, ystart)
        if not tilesToFlip:
            return False
        self.board[xstart][ystart] = tile
        for x, y in tilesToFlip:
            self.board[x][y] = tile
        return True
    
    def getScore(self):
        """ get the score of the players """
        W_score, B_score = 0, 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 'W':
                    W_score += 1
                elif self.board[x][y] == 'B':
                    B_score += 1
        print('Player W score: {}'.format(W_score))
        print('Player B score: {}'.format(B_score))
        if W_score > B_score:
            print('Player W wins.')
        else:
            print('Player B wins.')

    def go_player(self, player_name):
        """ A player's turn """
        player = Player(player_name)
        self.print_validChoice(player.name())
        player_input = player.player_input()
        while not self.check_playerInput(player.name(), player_input):
                print('{}: invalid choice.'.format(player_input))
                player_input = player.player_input()        
        self.makeMove(player.name(), player_input)