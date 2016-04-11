nice = 0
mean = 0

def main ():
    start()

def start():
    print"Hello and welcome to nice or mean!"
    name = raw_input("What's your name? : ")
    print "Hi and welcome ,"+name+":"
    print "In this game, you will be greeted by several different people. You can treate them nicely or you can be nice or mean."
    print "At the end of the game, your fate will be determined by how you acted."

    choice = raw_input("Do you want to play? y/n ")

    if choice == "y":
        print "Great, use 'm' for mean and 'n' for nice!"
        begin()

    if choice == "n":
        print"NVM, peace out...."
        

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job - you win! Everyone loves you and you live in a palace!"
        choice = raw_input ("Do you want to play again? y/n ")

        if choice == "y":
            print "Okay, Let's Go"
            nice = 0
            begin()

        if choice == "n":
            print "Say no more..."
            exit()

    if mean > 2:
        print "Too bad - game over! The struggle is real"

        choice = raw_input("Do you want to play again? y/n")

        if choice == "y":
            print "Game Start"
            mean = 0
            begin ()

        if choice == "n":
            print "Peace out"
            exit()

        elif choice != "y"+"n":
            print "Please enter y or n"

            if choice == "y":
                begin()
            if choice == "n":
                print "Later"
                exit()

            if choice != "y"+"n":
                  choice = raw_input("Do you want to play? y/n")

    pick = raw_input("Someone approaches you to talk. Will you be Nice or Mean? n/m")

    if pick == "n":
        print "They smile, wave and walk away."
        nice = nice+1
        print "You currently have" + str(nice) + " nice."
        begin()

    if pick == "m":
        print "They frown, glare at you and storm off."
        mean == mean+1
        print "You currently have " + str(mean) + " mean."
        begin()
                            




    
start()
    
