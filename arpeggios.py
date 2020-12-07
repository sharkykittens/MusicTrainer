import notes


def major7(root, permutation):
    arp = []
    if permutation == 0:
        arp.append(root['note'])
        arp.append(notes.search_note((root['value']+4) % 12)['note'])
        arp.append(notes.search_note((root['value']+7) % 12)['note'])
        arp.append(notes.search_note((root['value']+11) % 12)['note'])
        print(str(root['note'])+" major 7th arpeggio in root position")

    # elif permutation == 1:

    # elif permutation == 2:

    # elif permutation == 3:
    return arp


def minor7(root, permutation):
    arp = []
    return arp


def dom7(root, permutation):
    arp = []
    return arp


def halfdim7(root, permutation):
    arp = []
    return arp
