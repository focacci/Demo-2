class Falling:

    def __init__(self, player):
        self.player = player

    def fallingPlatformCollision(self):
        from model.Walking import Walking
        self.player.fallingPlatformCollision()
        self.player.state = Walking(self.player)
        self.player.jumpCapable = True
