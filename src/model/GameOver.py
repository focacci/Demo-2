from model.Player import Player
from model.PlayerState import PlayerState

class GameOver(PlayerState(Player)):

    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def isAlive(self):
        return False
