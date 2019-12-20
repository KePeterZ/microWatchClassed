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

# [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

class brick:
    def __init__(self, startingPosition=[32, 8], gravity=1, layout=[(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3)]):
        self.layout = layout
        self.center = startingPosition
        self.pixels = layout
        for pixel in self.pixels:
            w.d.pixel(self.center[0]+pixel[0], self.center[1]+pixel[1], 1)
        w.d.show()

    def largify(self, value):
        self.pixels = self.layout

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

    def rotate(self, modifier=(-1, -1)):
        self.pixels = [(p[0]*modifier[0], p[1]*modifier[1]) for p in self.pixels]
        self.showObject()
    
    def changeRawCoords(self, pixels):
        self.pixels = pixels
        self.showObject()

    def returnRawCoords(self):
        return [w.d.pixel(self.center[0]+pixel[0], self.center[1]+pixel[1], 1) for pixel in self.pixels]

brickArray = []
brickArray.append(1)

brickArray[-1] = brick([110,32], layout=[(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])

rotateCount = 0
speed = 2
timeToWait = 0.1
stackPixels = [(0, y) for y in range(64)]
t1 = time.time()

while True:
    w.d.fill(0)
    changer = 0
    if not w.keyUp.value():
        changer = -4
    elif not w.keyDown.value():
        changer = 4
    if not w.keyCenter.value():
        rotateTuple = [()]
        oldPixels = brickArray[-1].pixels
        newPixels = [(p[1], p[0]) for p in oldPixels]
        rotateCount += 1
        brickArray[-1].changeRawCoords(newPixels)
    brickArray[-1].move(0, changer)
    if time.time()-t1 > timeToWait: brickArray[-1].move(speed*-2, 0); t1 = time.time()
    # if any([(p[0], p[1]) in stackPixels for p in brickArray[-1].returnRawCoords()]):
    #     brickArray.append(1)
    #     brickArray[-1] = brick([110,32], layout=[(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])