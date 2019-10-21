from music21 import *
import decimal

def bassBeatContourVal():
    piece = corpus.parse(input('Enter name of piece: '))
    x = float(input('beat number: '))

    lastNoteMidi = piece.parts[3].recurse().notes[0].pitch.midi
    numAscending = 0
    numDescending = 0

    for n in piece.parts[3].recurse().notes:
        if n.pitch.midi > lastNoteMidi:
            if n.beat == x:
                numAscending += 1
        if n.pitch.midi < lastNoteMidi:
            if n.beat == x:
                numDescending += 1
        lastNoteMidi = n.pitch.midi

    print('Number of ascending notes on beat',x, "=", numAscending)
    print('Number of descending notes on beat',x, "=", numDescending)
    bassBeatContourVal()

bassBeatContourVal()


