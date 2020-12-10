import random
import arpeggios as ap
import notes as n

seed = random.seed()


def random_arpeggio():

    ran_note = random.randint(0, 11)
    ran_arp = random.randint(0, 3)  # 0 to 3 based on which arp
    ran_permute = random.randint(0, 3)  # which permuation from root to 3
    which_arp = ""
    which_perm = ""

    if ran_permute == 0:
        which_perm = " root"
    elif ran_permute == 1:
        which_perm = " third"
    elif ran_permute == 2:
        which_perm = " fifth"
    elif ran_permute == 3:
        which_perm = " seventh"

    if ran_arp == 0:
        note_list = ap.major7(n.search_note(ran_note), ran_permute)
        which_arp = " Major 7th Arpeggio"
    elif ran_arp == 1:
        note_list = ap.minor7(n.search_note(ran_note), ran_permute)
        which_arp = " Minor 7th Arpeggio"
    elif ran_arp == 2:
        note_list = ap.dom7(n.search_note(ran_note), ran_permute)
        which_arp = " Dominant 7th Arpeggio"
    elif ran_arp == 3:
        note_list = ap.halfdim7(n.search_note(ran_note), ran_permute)
        which_arp = " Half-diminished 7th Arpeggio"

    print("Please play "+str(n.search_note(ran_note)
                             ['note'])+which_arp+" starting from the"+which_perm)

    return note_list
