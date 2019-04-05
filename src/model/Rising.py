class Rising:

    def __init__(self, player):
        self.player = player
        self.player.state.rising = True
        self.player.jumpCapable = False

    def update(self, dt):
        from model.Falling import Falling
        self.player.update(dt)
        if self.player.velocity.z <= 0.0:
            self.player.state = Falling(self.player)

    def jumpReleased(self):
        self.player.velocity.z /= 2.0
