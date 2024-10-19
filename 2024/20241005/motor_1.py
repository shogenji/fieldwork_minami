# motor

from microbit import *

i2c.write(16, bytes([0, 0, 50]))
i2c.write(16, bytes([2, 0, 0]))
