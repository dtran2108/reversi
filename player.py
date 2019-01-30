class Player:
    def __init__(self, player):
        self.player_name = player
    
    def name(self):
        return self.player_name
    
    def player_input(self):
        """ get the player's input """
        print('Player {}: '.format(self.player_name), end='')
        playerInput = input()
        return playerInput