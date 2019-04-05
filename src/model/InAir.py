class InAir:

    def __init__(self, player):
        self.player = player

    def leftPressed(self):
        self.player.moveLeftMidAir()

    def rightPressed(self):
        self.player.moveRightMidAir()

    def fallingPlatformCollision(self):
        self.player.fallingPlatformCollision()
