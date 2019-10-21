from music21 import *
from collections import Counter

def bassContourProfile():
    piece = corpus.parse(input('Enter name of piece: '))
    lastNoteMidi = piece.parts[3].recurse().notes[0].pitch.midi
    numAscending = []
    numDescending = []

    for n in piece.parts[3].recurse().notes:
        if n.pitch.midi > lastNoteMidi:
            numAscending.append(n.beat)
        if n.pitch.midi < lastNoteMidi:
            numDescending.append(n.beat)
        lastNoteMidi = n.pitch.midi

    print(Counter(numAscending))
    print(Counter(numDescending))
    bassContourProfile()

bassContourProfile()

