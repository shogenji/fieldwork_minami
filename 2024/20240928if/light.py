from microbit import *

while True:
    lv = display.read_light_level()
    print(lv)
    sleep(100)
