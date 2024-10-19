from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin15, 4)

while True:
    irL = pin13.read_digital()
    if irL == 0:
        np[0] = (randint(0, 255), randint(0, 255), randint(0, 255))
        np[1] = (randint(0, 255), randint(0, 255), randint(0, 255))
        np[2] = (randint(0, 255), randint(0, 255), randint(0, 255))
        np[3] = (randint(0, 255), randint(0, 255), randint(0, 255))
        np.show()
    else:
        np.clear()
    sleep(100)
