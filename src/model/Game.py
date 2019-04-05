from model.Physics import Physics
from model.PhysicsVector import PhysicsVector
from model.World import World
from model.GameOver import GameOver
from model.Player import Player
from model.Platform import Platform
import random


class Game:

    def __init__(self):
        self.world = World(10)
        self.gridWidth = 15
        self.gridHeight = 20
        self.playerSize = 0.5

        self.speed = 0.03
        self.killLine = -0.1

        self.platforms = [Platform(PhysicsVector(0, 0, 0), PhysicsVector(gridWidth, 0, 0))]

        self.minPlatformWidth = 1.0
        self.maxPlatformWidth = 6.0
        self.maxPlatformGaps = 8.0
        self.probabilityOfNoPlatforms = 0.2
        self.gapProbability = 0.8

        self.lastLevelGenerated = 0

        self.skipped = 0
        self.maxConsecutiveSkips = 2

        self.player = Player(
            PhysicsVector(self.gridWidth / 3.0, 0, self.gridHeight / 2.0),
            PhysicsVector(0, 0, 0)
        )
        self.world.objects = [self.player]

        self.generateUntilLevel(int(self.gridHeight) - 5)


    def generateUntilLevel(self, levelStop):
        for level in range(self.lastLevelGenerated + 1, levelStop):
            currentRow = self.thisCurrentRow()
        while currentRow < self.gridWidth - 3:
            if random.random() < self.gapProbability:
                currentRow += random.random * self.maxPlatformGaps
            platformWidth = self.minPlatformWidth.max(random.random() * self.maxPlatformWidth)
            newPlatform = Platform(PhysicsVector(currentRow, 0, level), PhysicsVector((self.gridWidth - 1).min(currentRow + platformWidth), 0, level))
            currentRow += newPlatform.append(self.platforms)
        self.lastLevelGenerated = levelStop

    generateUntilLevel(self.gridHeight.toInt - 5)

    def thisCurrentRow(self):
        if (self.skipped < self.maxConsecutiveSkips) and (random.random < self.probabilityOfNoPlatforms):
            self.skipped += 1
            return self.gridWidth
        else:
            self.skipped = 0
            return 1.0

    def risingWorld(self):
        self.killLine += self.speed
        self.generateUntilLevel(int(self.killLine + 2 * self.gridHeight))

    def checkIfPlayerFell(self, player):
        if player.location.z < self.killLine and player.isAlive():
            player.state = GameOver(player)
            print("BOO YOU STINK")

    def update(self, dt):
        Physics.updateWorld(self.player, self.world, dt)
        self.player.update(dt)
        self.player.points = self.lastLevelGenerated
        self.risingWorld()
        self.checkIfPlayerFell(self.player)
