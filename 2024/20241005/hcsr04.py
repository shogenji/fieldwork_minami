# HCSR04

from microbit import *
import machine
pin2.read_digital()
while True:
    pin1.write_digital(1)
    sleep(1)
    pin1.write_digital(0)
    t = machine.time_pulse_us(pin2, 1)
    d = int(t * 340 / 20000)
    print(t, d)
