from model.InAir import InAir
from model.Walking import Walking


class Falling(InAir):

    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def fallingPlatformCollision(self):
        self.player.fallingPlatformCollision()
        self.player.state = Walking(self.player)
        self.player.jumpCapable = True
