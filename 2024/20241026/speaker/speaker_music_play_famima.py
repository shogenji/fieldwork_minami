# Speaker - music module - play method

from microbit import *
import music

music.set_tempo(ticks=4, bpm=60)
notes = ['f#5:2', 'd:2', 'a4:2', 'd5:2',
         'e:2', 'a:6', 'e:2', 'f#:2',
         'e:2', 'a4:2', 'd5:4', 'r:4']

for i in range(12):
    music.play(notes[i])
