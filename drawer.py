from boot import Watch
import time

w = Watch()
w.d.rotate(90)

# Tetris
# 
# Game build up: 
#   1st goal: render object
#   2nd goal: move object left or right, and rotate
#   3rd goal: set gravity
#   4th goal: stop from falling below 0
#   5th goal: object collision
#   6th goal: point counter

class brick:
    def __init__(self, startingPosition=[32, 8], gravity=1):
        self.center = startingPosition
        self.pixels = [(0,0), (0,1), (0,-1), (1, 0), (-1,0)]
        for pixel in self.pixels:
            w.d.pixel(self.center[0]+pixel[0], self.center[1]+pixel[1], 1)
        w.d.show()

    def showObject(self):
        for pixel in self.pixels:
            w.d.pixel(self.center[0]+pixel[0], self.center[1]+pixel[1], 1)
        w.d.show()

    def maximizer(self, inValue, maxValue=132):
        return inValue%(maxValue-1)

    def move(self, moveXby=0, moveYby=0):
        self.center[0] = (self.center[0]+moveXby)%133
        self.center[1] = (self.center[1]+moveYby)%65
        self.showObject()


b = brick([132,32])
while True:
    speed = 4
    if not w.keyLeft.value():
        speed += 1
    elif not w.keyRight.value():
        speed -= 1
    if speed < 0:
        speed = 0
    changer = 0
    if not w.keyUp.value():
        changer = -2
    elif not w.keyDown.value():
        changer = 2
    if not w.keyCenter.value():
        w.d.fill(0)
    b.move(-abs(speed), changer)