from model.PlayerState import PlayerState
from model.Rising import Rising


class Walking(PlayerState):

    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def leftPressed(self):
        self.player.walkLeft()

    def rightPressed(self):
        self.player.walkRight()

    def jumpPressed(self):
        self.player.velocity.z = self.player.walkingJumpVelocity
        self.player.state = Rising(self.player)

    def leftReleased(self):
        self.player.leftReleased()

    def rightReleased(self):
        self.player.rightReleased()

    def fallingPlatformCollision(self):
        self.player.velocity.z = 0
