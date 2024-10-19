# Speaker - music module - play method

from microbit import *
import music

music.set_tempo(ticks=8, bpm=120)
notes = ['c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5',
         'e5', 'g4', 'c5', 'e5', 'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5',
         'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5',
         'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
         'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5',
         'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5',
         'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5', 'c4', 'd', 'f#', 'a',
         'd5', 'f#4', 'a', 'd5', 'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5',
         'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5', 'b3', 'd4', 'g', 'd5',
         'g5', 'g4', 'd5', 'g5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
         'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g',
         'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
         'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5', 'd3', 'a', 'd4', 'f#',
         'c5', 'd4', 'f#', 'c5', 'g3', 'b', 'd4', 'g', 'b', 'd', 'g', 'b', 'g3',
         'b3', 'd4', 'g', 'b', 'd', 'g', 'b'
]

count = 0
for note in notes:
    music.play(note)
    count += 1
    pin8.write_digital(count%2)

