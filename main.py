import arpeggios as ap
import notes as n
import arp_trainer


while True:
    print("0: Exit Program")
    print("1: Arpeggio Trainer Mode")
    mode_select = input("Please select which mode to choose from: ")
    if mode_select == "0":
        exit()

    elif mode_select == "1":
        print("Press any key for a new arpeggio")
        print("or press esc to return to mode selection")

        while True:
            keystroke = input()
            if keystroke != "esc":
                print(arp_trainer.random_arpeggio())
                print("Press any key for a new arpeggio")
                print("or press esc to return to mode selection")

            else:
                break
