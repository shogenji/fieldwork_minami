# motor 前進・停止

from microbit import *

i2c.write(16, bytes([0, 0, 50]))
i2c.write(16, bytes([2, 0, 50]))

sleep(1000)

i2c.write(16, bytes([0, 0, 0]))
i2c.write(16, bytes([2, 0, 0]))