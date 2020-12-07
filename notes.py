global allnotes


C = {
    "note": "C",
    "value": 0
}

Db = {
    "note": "Db",
    "value": 1
}

D = {
    "note": "D",
    "value": 2
}

Eb = {
    "note": "Eb",
    "value": 3
}

E = {
    "note": "E",
    "value": 4
}

F = {
    "note": "F",
    "value": 5
}

Gb = {
    "note": "Gb",
    "value": 6
}

G = {
    "note": "G",
    "value": 7
}

Ab = {
    "note": "Ab",
    "value": 8
}

A = {
    "note": "A",
    "value": 9
}

Bb = {
    "note": "Bb",
    "value": 10
}

B = {
    "note": "B",
    "value": 11
}

allnotes = [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]


def search_note(note_val):
    for note in allnotes:
        if note["value"] == note_val:
            return note
