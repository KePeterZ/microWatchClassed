def playIcon(positionX, positionY, size=0):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX+14+size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX+14+size, positionY+8+size, 1)

def pauseIcon(positionX, positionY, size=0):
    d.rect(positionX, positionY, 6+int(size/2), 16+size, 1)
    d.rect(positionX+10+int(size/2), positionY, 6+int(size/2), 16+size, 1)

def nextIcon(positionX, positionY, size=0, secondOffset=5):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX+14+size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX+14+size, positionY+8+size, 1)
    d.line(positionX+secondOffset, positionY, positionX+secondOffset, positionY+16+size, 1)
    d.line(positionX+secondOffset, positionY, positionX+14+size+secondOffset, positionY+8+size, 1)
    d.line(positionX+secondOffset, positionY+16+size, positionX+14+size+secondOffset, positionY+8+size, 1)

def prevIcon(positionX, positionY, size=0, secondOffset=5):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX-14-size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX-14-size, positionY+8+size, 1)
    d.line(positionX-secondOffset, positionY, positionX-secondOffset, positionY+16+size, 1)
    d.line(positionX-secondOffset, positionY, positionX-14-size-secondOffset, positionY+8+size, 1)
    d.line(positionX-secondOffset, positionY+16+size, positionX-14-size-secondOffset, positionY+8+size, 1)
