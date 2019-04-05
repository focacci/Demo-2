from tkinter import *
from model.Player import Player
#from model.playerstates.PlayerState import PlayerState


class KeyboardInputs:

    def __init__(self, player):
        self.myContainer1 = Frame(player)
        self.myContainer1.pack()

        def keyPressed(event):
            print(repr(event.char))
            if repr(event.keysym_num) == '119':
                print('w')
                player.jumpPressed()
            elif repr(event.keysym_num) == '100':
                print('d')
                player.rightPressed()
            elif repr(event.keysym_num) == '97':
                print('a')
                player.leftPressed()
            else:
                print("Wrong Key")

        def keyReleased(event):
            if repr(event.keysym_num) == '119':
                print('wR')
                player.jumpReleased()
            elif repr(event.keysym_num) == '100':
                print('dR')
                player.rightPressed()
            elif repr(event.keysym_num) == '97':
                print('aR')
                player.leftPressed()
            else:
                print("Wrong Key")

        def callback(event):
            frame.focus_set()
            print("clicked at", event.x, event.y)

        frame = Frame(root, width=100, height=100)
        frame.bind("<KeyPress>", keyPressed)
        frame.bind("<KeyRelease>", keyReleased)
        frame.bind("<Button-1>", callback)
        frame.pack()


root = Tk()
inputs = KeyboardInputs(root)
root.mainloop()
