import random
import arpeggios as ap
import notes as n

seed = random.seed()


def random_arpeggio():

    ran_note = random.randint(0, 11)
    ran_arp = random.randint(0, 0)  # 0 to 4 based on which arp
    ran_permute = random.randint(0, 0)  # which permuation from root to 3

    if ran_arp == 0:
        note_list = ap.major7(n.search_note(ran_note), ran_permute)

    return note_list
