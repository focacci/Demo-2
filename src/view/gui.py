
from model.Game import*
from model.Platform import *
from controller.KeyboardInputs import*
import time
import math
from tkinter import *


class GUI:

    def __init__(self):
        self.lastUpdateTime = time.time()
        self.game = Game()
        self.scaleFactor = 30.0
        self.windowWidth = self.game.gridWidth * self.scaleFactor
        self.windowHeight = self.game.gridHeight * self.scaleFactor
        self.playerSpriteSize = self.game.playerSize
        self.platformThickness = 0.1
        self.sceneGraphics = self.group()
        self.player1sprite = self.player_sprite(self.game.player.location, self.game.player.location, color="Red" )
        self.player2sprite = self.player_sprite(self.game.player.location.x, self.game.player.location.z, color="Blue")
        self.sceneGraphics.children.add(self.player1sprite)
        self.sceneGraphics.children.add(self.player2sprite)

    def convert(self, width):
        return self-width/2.0

    def convert2(self,height):
        return (self.game.gridHeight-(self - self.game.killine)-height) * self.scaleFactor

    def player_sprite(self, ylocation, color):
        self.rectangle= self.Rectangle(
            width=self.playerSpriteSize * self.scaleFactor,
            height=self.playerSpriteSize * self.scaleFactor,
            translatex=self.convert(self, self.playerSpriteSize),
            translatey=self.convert(ylocation.self.playerSpriteSize),
            fill=color
        )
        return self.rectangle

    def compute_distance(self, v, v2):
        math.sqrt(math.pow(v2.x - v.x, 2.0) + math.pow(v2.z - v.z, 2.0))

    def platformSprite(self):
        self.distance= self.compute_distance(self.Platform.start, self.Platform.end)




    def frame(self):
        window = Tk()
        window.title = "The Race"
        window.geometry(self.windowWidth, self.windowHeight)
        window.bind(self.keyPressed(self.game.player))

        self.update = time
        self.dt = (time - self.lastUpdateTime) / 1000000000.0
        self.lastUpdateTime = time
        self.update(self.dt)

        self.player1sprite.translatex.value = self.convert(self.game.player.location.x, self.playerSpriteSize)
        self.player1sprite.translatex.value = self.convert2(self.game.player.location.z, self.playerSpriteSize)
        self.player2sprite.translatex.value = self.convert(self.game.player.location.x, self.playerSpriteSize)
        self.player2sprite.translatey.value = self.convert2(self.game.player.location.z, self.playerSpriteSize)
        window.mainloop()























