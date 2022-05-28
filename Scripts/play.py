import time  # Imports a module to add a pause

if __name__ == "__main__":
    exec(open("rwData.py").read())

# Figuring out how users might respond
answerA = ["A", "a"]
answerB = ["B", "b"]
answerC = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
sword = 0
gold = 0

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication

# The story is broken into sections, starting with "intro"

def intro():
    print("***** Game Start *****")
    print(" Long Description of Room 1 "
        "You are in the cave ... "
        " "
        "when you hear a "
        "grotesque sound emitting behind you. A roving monster is "
        "running towards you. You will:")
    time.sleep(1)
    print("""  A. Grab a nearby rock and throw it at the monster
  B. Lie down and wait to be mauled
  C. Run""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answerA:
        optionRock()
    elif choice in answerB:
        print ("\nOuch, that was quick. "
               "\n\nYou died!")
        print("***** Game END *****")
    elif choice in answerC:
        optionRun()
    else:
        print (required)
        intro()

def optionRock(): 
    print ("\nThe monster is stunned, but regains control. He begins "
    "running towards you again. Will you:")
    time.sleep(1)
    print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answerA:
        optionRun()
    elif choice in answerB:
        print ("\nYou decided to throw another rock, as if the first " 
               "rock thrown did much damage. The rock flew well over the "
               "monster head. You missed. \n\nYou died!")
        print("***** Game END *****")
    elif choice in answerC:
        optionCave()
    else:
        print (required)
        optionRock()

def optionCave():
    print ("\nYou were hesitant, since the cave was dark and "
           "ominous. Before you fully enter, you notice a shiny sword on "
           "the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1 #adds a sword
    else:
        sword = 0
        print ("\nWhat do you do next?")
    time.sleep(1)
    print ("""  A. Hide in silence
   B. Fight
   C. Run""")
    choice = input(">>> ")
    if choice in answerA:
        print ("\nReally? You're going to hide in the dark? I think "
               "monster can see very well in the dark, right? Not sure, but "
               "I'm going with YES, so...\n\nYou died!")
        print("***** Game END *****")
    elif choice in answerB:
        if sword > 0:
            print ("\nYou laid in wait. The shimmering sword attracted "
                   "the monster, which thought you were no match. As he walked "
                   "closer and closer, your heart beat rapidly. As the orc "
                   "reached out to grab the sword, you pierced the blade into "
                   "its chest. \n\nYou survived!")
            print("***** Game END *****")
        else: #If the user didn't grab the sword
            print ("\nYou should have picked up that sword. You're "
                   "defenseless. \n\nYou died!")
            print("***** Game END *****")
    elif choice in answerC:
        print ("As the monster enters the dark cave, you sliently "
               "sneak out. You're several feet away, but the orc turns "
               "around and sees you running.")
        optionRun()
    else:
        print (required)
        optionCave()

def optionRun():
    print ("\nYou run as quickly as possible, but the monster's "
           "speed is too great. You will:")
    time.sleep(1)
    print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answerA:
        print ("You're easily spotted. "
               "\n\nYou died!")
        print("***** Game END *****")
    elif choice in answerB:
        print ("\nYou're no match for an orc. "
               "\n\nYou died!")
        print("***** Game END *****")
    elif choice in answerC:
        optionRoom3()
    else:
        print (required)
        optionRun()
    
def optionRoom3():
    print("long description of room3 if first time or requested")
    print("short description otherwise")
    print ("\nWhile frantically running, you notice a rusted "
           "sword lying in the mud. You quickly reach down and grab it, "
           "but miss. You try to calm your heavy breathing as you hide "
           "behind a delapitated building, waiting for the orc to come "
           "charging around the corner. You notice a gold "
           "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        gold = 1 #adds a flower
    else:
        gold = 0
        print ("You hear its heavy footsteps and ready yourself for "
               "the impending monster.")
    time.sleep(1)
    if gold > 0:
        print ("\nYou quickly hold out the gold, somehow "
               "hoping it will stop the monster. It does! The monster was looking "
               "for love. "
               "\n\nThis got weird, but you survived!")
        print("***** Game END *****")
    else: #If the user didn't grab the sword
        print ("\nMaybe you should have picked up the gold. "
               "\n\nYou died!")
        print("***** Game END *****")

intro()