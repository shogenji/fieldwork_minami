from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.DUCK)
    else:
        display.clear()
