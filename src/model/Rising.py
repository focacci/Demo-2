from model.Player import Player
from model.InAir import InAir
from model.Falling import Falling


class Rising(InAir(Player)):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.player.state.rising = True
        self.player.jumpCapable = False

    def update(self, dt):
        self.player.update(dt)
        if self.player.velocity.z <= 0.0:
            self.player.state = Falling(self.player)

    def jumpReleased(self):
        self.player.velocity.z /= 2.0
