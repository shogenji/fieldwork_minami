from microbit import *

i2c.write(16, bytes([0, 0, 50]))
i2c.write(16, bytes([2, 0, 50]))
sleep(500)
i2c.write(16, bytes([0, 1, 50]))
i2c.write(16, bytes([2, 0, 50]))
sleep(500)
i2c.write(16, bytes([0, 0, 50]))
i2c.write(16, bytes([2, 1, 50]))
sleep(500)
i2c.write(16, bytes([0, 0, 0]))
i2c.write(16, bytes([2, 0, 0]))

