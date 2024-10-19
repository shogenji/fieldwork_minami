from microbit import *
import neopixel

np = neopixel.NeoPixel(pin15, 4)

np[0] = (255, 0, 0)
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)
np[3] = (255, 255, 255)
np.show()

sleep(1000)

np.clear()