# line ARROW

from microbit import *

while True:
    irL = pin13.read_digital()
    irR = pin14.read_digital()
    if irL == 0 and irR == 0:
        display.show(Image.ARROW_N)
    elif irL == 0:
        display.show(Image.ARROW_E)
    elif irR == 0:
        display.show(Image.ARROW_W)
    else:
        display.show(Image.ARROW_S)
