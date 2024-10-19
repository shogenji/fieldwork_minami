from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin15, 4)

while True:
    irL = pin13.read_digital()
    if irL == 0:
        for i in range(0, 4):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            np[i] = (r, g, b)
            np.show()
    else:
        np.clear()
    sleep(100)
