import notes


def major7(root, permutation):
    arp = []
    if permutation == 0:
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+11) % 12)['note'])
        print(str(root['note'])+" major 7th arpeggio in root position")

    elif permutation == 1:
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+11) % 12)['note'])
        arp.append(root['note'])
        print(str(root['note'])+" major 7th arpeggio starting from the third")

    elif permutation == 2:
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+11) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        print(str(root['note'])+" major 7th arpeggio starting from the fifth")

    elif permutation == 3:
        arp.append(notes.search_note((root['value']+11) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        print(str(root['note']) +
              " major 7th arpeggio starting from the seventh")
    return arp


def minor7(root, permutation):
    arp = []
    if permutation == 0:
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        print(str(root['note'])+" minor 7th arpeggio in root position")

    elif permutation == 1:
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        print(str(root['note'])+" minor 7th arpeggio starting from the third")

    elif permutation == 2:
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        print(str(root['note'])+" minor 7th arpeggio starting from the fifth")

    elif permutation == 3:
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        print(str(root['note']) +
              " minor 7th arpeggio starting from the seventh")
    return arp


def dom7(root, permutation):
    arp = []
    if permutation == 0:
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        print(str(root['note'])+" dominant 7th arpeggio in root position")

    elif permutation == 1:
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        print(str(root['note']) +
              " dominant 7th arpeggio starting from the third")

    elif permutation == 2:
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        print(str(root['note']) +
              " dominant 7th arpeggio starting from the fifth")

    elif permutation == 3:
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        print(str(root['note']) +
              " dominant 7th arpeggio starting from the seventh")
    return arp


def halfdim7(root, permutation):
    arp = []
    if permutation == 0:
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+6) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        print(str(root['note'])+" half dim 7th arpeggio in root position")

    elif permutation == 1:
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+6) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        print(str(root['note']) +
              " half dim 7th arpeggio starting from the third")

    elif permutation == 2:
        arp.append(notes.search_note((root['value']+6) % 12)['note'])
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        print(str(root['note']) +
              " half dim 7th arpeggio starting from the fifth")

    elif permutation == 3:
        arp.append(notes.search_note((root['value']+10) % 12)['note'])
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+3) % 12)['note'])
        arp.append(notes.search_note((root['value']+6) % 12)['note'])
        print(str(root['note']) +
              " half dim 7th arpeggio starting from the seventh")
    return arp
