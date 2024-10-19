# Speaker - music module - pitch method

from microbit import *
import music

for f in range(440, 1720, 16):
    music.pitch(f, 10)
for i in range(0, 82):
    f = 1720 - i * 16
    music.pitch(f, 10)

