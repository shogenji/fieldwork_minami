# line stop

from microbit import *

while True:
    irL = pin13.read_digital()
    irR = pin14.read_digital()
    if irL == 0 and irR == 0:
        i2c.write(16, bytes([0, 0, 0]))
        i2c.write(16, bytes([2, 0, 0]))
    else:
        i2c.write(16, bytes([0, 0, 50]))
        i2c.write(16, bytes([2, 0, 50]))
