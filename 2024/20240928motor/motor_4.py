# motor I2C通信データテスト

from microbit import *

    #i2c.write(16, bytes([0, 0, 50]))
#sleep(100)
#i2c.write(16, bytes([1, 0, 50]))    # 動かない
#sleep(100)
#i2c.write(16, bytes([2, 0, 50]))
#sleep(100)
i2c.write(16, bytes([3, 0, 50]))    # 動かない
sleep(100)
