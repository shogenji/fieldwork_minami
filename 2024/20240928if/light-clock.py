from microbit import *

while True:
    lv = display.read_light_level()
    lv = (lv / 255) * 11
    lv = int(lv)

    display.show(Image.ALL_CLOCKS[lv]) 
    sleep(100)
