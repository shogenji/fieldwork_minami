# line trace

from microbit import *

while True:
    irL = pin13.read_digital()
    irR = pin14.read_digital()
    if irL == 0:
        i2c.write(16, bytes([0, 1, 30]))
        i2c.write(16, bytes([2, 0, 90]))
    else:
        i2c.write(16, bytes([0, 0, 90]))
        i2c.write(16, bytes([2, 1, 30]))
