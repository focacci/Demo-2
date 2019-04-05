import math
from model.PhysicsVector import PhysicsVector


class Physics:

    def __init__(self):
        self.epsilon = 0.00000001

    def equalDoubles(self, d1, d2):
        return abs(d1 - d2) < self.epsilon

    def computePotentialLocation(self, obj, dt):
        newX = obj.location.x + dt * obj.velocity.x
        newY = obj.location.y + dt * obj.velocity.y
        newZ = obj.location.z + dt * obj.velocity.z
        return PhysicsVector(newX, newY, newZ)

    def updateVelocity(self, obj, world, dt):
        obj.velocity.z = obj.velocity.z - (world.gravity * dt)

    def slope(self, p1, p2):
        if p2.x - p1.x == 0.0:
            return math.inf
        else:
            return (p2.z - p1.z) / (p2.x - p1.x)

    def yIntercept(self, p1, m):
        return p1.z - m * p1.x

    def detectPlatformCollision(self, obj, potentialLocation, platform):
        if obj.location.x == potentialLocation.x and obj.location.z == potentialLocation.z: # if player didnt move
            return False

        mObj = self.slope(obj.location, potentialLocation)
        bObj = self.yIntercept(obj.location, mObj)

        mBound = self.slope(platform.start, platform.end)
        bBound = self.yIntercept(platform.start, mBound)

        if self.equalDoubles(mObj, mBound):
            return False

        largeSlope = 1000.0
        if abs(mObj) > largeSlope:
            ix = potentialLocation.x
            iy = ix * mBound + bBound

            if obj.location.z > potentialLocation.z:
                objUp = obj.location.z
                objDown = potentialLocation.z
            else:
                objUp = potentialLocation.z
                objDown = obj.location.z

            bLeft = platform.start.x
            bRight = platform.end.x

            return (iy >= objDown and iy <= objUp) and (ix >= bLeft and ix <= bRight)
        else:
            ix = (bBound - bObj) / (mObj - mBound)

            objLeft = obj.location.x.min(potentialLocation.x)
            objRight = obj.location.x.max(potentialLocation.x)

            bLeft = platform.start.x.min(platform.end.x)
            bRight = platform.start.x.max(platform.end.x)

            return (ix >= objLeft - self.epsilon and ix <= objRight + self.epsilon) and (ix >= bLeft - self.epsilon and ix <= bRight + self.epsilon)

    def updateWorld(self, player, world, dt):
        for obj in world.objects:
            # update velocity
            self.updateVelocity(obj, world, dt)

            # compute potentialLocation
            potentialLocation = self.computePotentialLocation(obj, dt)

            # check for collisions
            collisionDetected = False
            for platform in world.platforms:
                if self.detectPlatformCollision(obj, potentialLocation, platform):
                    collisionDetected = True

            # if collision, do not update z
            obj.location.x = potentialLocation.x
            obj.location.y = potentialLocation.y
            if (not collisionDetected) or (potentialLocation.z > obj.location.z):
                obj.location.z = potentialLocation.z

            if collisionDetected:
                player.checkCollision()
            else:
                player.noPlatformCollision()
