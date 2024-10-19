# Speaker - write_digital

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(3)
    pin0.write_digital(0)
