# motor 180度回転

from microbit import *

i2c.write(16, bytes([0, 0, 50]))
i2c.write(16, bytes([2, 1, 50]))

sleep(1700)

i2c.write(16, bytes([0, 0, 0]))
i2c.write(16, bytes([2, 0, 0]))
