from model.PhysicalObject import PhysicalObject
from model.Walking import Walking


class Player(PhysicalObject):

    def __init__(self, location, velocity):
        super().__init__(location, velocity)

        self.location = location
        self.velocity = velocity
        self.walkingSpeed = 4.0
        self.airSpeed = 3.0

        self.standingJumpVelocity = 6.0
        self.walkingJumpVelocity = 8.0

        self.jumpCapable = True

        self.points = 0

        self.state = Walking(self)

        self.leftKeyHeld = False
        self.rightKeyHeld = False
        self.jumpKeyHeld = False

    def leftPressed(self):
        self.leftKeyHeld = True
        self.state.leftPressed()

    def rightPressed(self):
        self.rightKeyHeld = True
        self.state.rightPressed()

    def jumpPressed(self):
        self.jumpKeyHeld = True
        self.state.jumpPressed()

    def leftReleased(self):
        self.leftKeyHeld = False
        self.state.jumpReleased()

    def rightReleased(self):
        self.rightKeyHeld = False
        self.state.rightReleased()

    def jumpReleased(self):
        self.jumpKeyHeld =False
        self.state.jumpReleased()

    def update(self, dt):
        self.state.update(dt)

    def risingPlatformCollision(self):
        self.state.risingPlatformCollision()

    def fallingPlatformCollision(self):
        self.state.fallingPlatformCollision()

    def noPlatformCollision(self):
        self.state.noPlatformCollision()

    def isAlive(self):
        self.state.isAlive()

    def walkLeft(self):
        self.velocity.x = -self.walkingSpeed

    def walkRight(self):
        self.velocity.x = self.walkingSpeed

    def moveLeftMidAir(self):
        self.velocity.x = self.velocity.x.min(-self.airSpeed)

    def moveRightMidAir(self):
        self.velocity.x = self.velocity.x.max(self.airSpeed)

    def stop(self):
        self.velocity.x = 0.0

    def checkCollision(self):
        if not self.state.rising:
            self.fallingPlatformCollision()
