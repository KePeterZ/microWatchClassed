from boot import Watch

w = Watch()

def menu(options):
    yNumbers = [0, 8, 16, 24, 32, 40, 48, 56]
    currentSelected = 0
    selectedOption = None
    while not selectedOption:
        for option in range(len(options)):
            w.textAt(options[option], 0, yNumbers[option])
        if not w.keyDown.value():
            currentSelected += 1
        if not w.keyUp.value():
            currentSelected -= 1
        w.d.fill_rect(0, 8, 138, 8, 1)
        w.d.show()

menu(["hey", "hi"])