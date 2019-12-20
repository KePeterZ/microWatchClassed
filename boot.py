from machine import Pin, I2C
from neopixel import NeoPixel
import sh1106 # Import Display module
import time # Import time module
import network # Import network module
import random
import usocket as socket

# buttons = {
#     "up": 12, 
#     "down": 13, 
#     "center": 14, 
#     "left": 2,
#     "right": 0
#     }
# for button in buttons.keys(): 
#     exec(
#         button+
#         "Button = Pin(buttons[button], Pin.IN, Pin.PULL_UP)")

class Watch:
    def __init__(self, displaySDA=5, displaySCL=4, NeoPixelPin=15):
        self.l = NeoPixel(Pin(NeoPixelPin, Pin.OUT), 1) # Declare LED
        self.d = sh1106.SH1106_I2C(
            132, 64, I2C(scl=Pin(displaySCL), 
            sda=Pin(displaySDA), freq=400000)) # Declare display
        self.d.fill(0); self.d.show() # Clear display before use
        self.wifi = network.WLAN(network.STA_IF) # Declare Wifi
        self.wifi.active(True) # Activate Wifi
        self.keyUp = Pin(12, Pin.IN, Pin.PULL_UP)
        self.keyDown = Pin(13, Pin.IN, Pin.PULL_UP)
        self.keyCenter = Pin(14, Pin.IN, Pin.PULL_UP)
        self.keyLeft = Pin(2, Pin.IN, Pin.PULL_UP)
        self.keyRight = Pin(0, Pin.IN, Pin.PULL_UP)
    
    def textAt(self, string, x, y, color=1, eraseBefore=False, show=False):
        if eraseBefore: self.d.fill(0)
        self.d.text(string, x, y, color)
        if show: self.d.show()
    
    def textInMiddle(self, string, y, color=1, eraseBefore=False, show=False):
        if eraseBefore: self.d.fill(0)
        self.d.text(str(string), int((132-len(string)*8)/2), y, color)
        if show: self.d.show()
    
    def runOnServer(self, command):
        s = socket.socket()
        s.connect(socket.getaddrinfo("192.168.0.33", 445)[0][-1])
        s.sendall(command.encode("utf-8"))
        return s.recv(512).decode('utf-8').rstrip()
    
    def connectWifi(self, wifi, password=None, waitForConnect=False):
        if password: self.wifi.connect(wifi, password)
        else: self.wifi.connect(wifi)
        if waitForConnect: 
            while not self.wifi.isconnected(): pass 
    
    def colorOnLed(self, r, g, b):
        self.l[0] = (r, g, b)
        self.l.write()
    
    def refreshScreen(self, fillBefore=False):
        if fillBefore: self.d.fill(0)
        self.d.show()