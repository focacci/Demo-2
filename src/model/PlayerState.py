from model.Player import Player


class PlayerState(Player):

    def __init__(self, player):
        super().__init__(player.location, player.velocity)
        self.player = player
        self.timeInState = 0.0
        self.jumpCapable = True
        self.rising = False

    def update(self, dt):
        self.timeInState += dt

        if self.player.leftKeyHeld:
            self.leftPressed()
        elif self.player.rightKeyHeld:
            self.rightPressed()

    def jumpPressed(self):
        from model.Rising import Rising
        if self.jumpCapable:
            self.player.velocity.z = self.player.standingJumpVelocity
            self.player.state = Rising(self.player)

    def fallingPlatformCollision(self):
        self.player.velocity.z = 0.0
        self.jumpCapable = True

    def isAlive(self):
        return True

