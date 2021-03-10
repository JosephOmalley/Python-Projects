#Python:    3.9.2
#Author: Joseph Omalley
#Purpose: Using varible using and functions to produce a functional game




def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
check if this is a new game or not.
if it is new, get the user's name.
if it is not a new game, thank the player for playing again and continue with the game
"""

#meaning, if we do not already habe this user's name,
#then they are a new player and we need to get their name
    if name != "":
        print("\n Thank you for playing agiain, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nwhat is your name \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \n will be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \n conversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiliing...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \n menacingly and storms off..")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, nice) and ({}, mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 cariables
    if nice > 2: # if condition is valid, call win function passing in the varibles so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the varibles so i tcan use them
        lose(nice,mean,name)
    else:           #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #suvstitute the {} wildcards with our varible values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our varibles
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhh too bad you lost, you lost")
    again(nice,mean,name)
    
#This is where I made a change\/
    # add survey
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? y/n:\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        elif choice == "n":
            stop = False
            survey(name)
        else:
            print =("\nEnter (y) for 'yes', ( n ) for 'no':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)
                       
def survey(name):
    answer1 = input("y or n Did you like my game {} ?". format(name))
    if answer1 == "y":
        print("thanks for the positive feedback!")
    elif answer1 == "n":
        print("Sorry to hear that!")
    else:
        print("please enter y your n")
    
if __name__ == "__main__":
    start()




