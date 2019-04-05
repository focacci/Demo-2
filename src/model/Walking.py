class Walking:
    def __init__(self, player):
        self.player = player

    def leftPressed(self):
        self.player.walkLeft()

    def rightPressed(self):
        self.player.walkRight()

    def jumpPressed(self):
        from model.Rising import Rising
        self.player.velocity.z = self.player.walkingJumpVelocity
        self.player.state = Rising(self.player)

    def leftReleased(self):
        self.player.leftReleased()

    def rightReleased(self):
        self.player.rightReleased()

    def fallingPlatformCollision(self):
        self.player.velocity.z = 0

    def noPlatformCollision(self):
        self.player.velocity.z += 0
