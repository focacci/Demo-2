from model.PlayerState import PlayerState


class InAir(PlayerState):

    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def leftPressed(self):
        self.player.moveLeftMidAir()

    def rightPressed(self):
        self.player.moveRightMidAir()

    def fallingPlatformCollision(self):
        self.player.fallingPlatformCollision()
