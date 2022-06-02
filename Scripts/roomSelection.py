import time

delay = 0.5 #(in seconds)

def win():
    time.sleep(delay)
    #print("You win")
    print("You won! Congratulations!")


def kill():
    time.sleep(delay)
    print("You died")

#ToDO:
#1. read data file
#   room list is getting from the data file
#   room episode as per room selected
#2. create log file and write to the save file.

def emerald():    
    roomBuilder([True, False], "the emerald room", True, ["win", "kill"])


def opal():    
    roomBuilder([False, True], "the opal room", True, ["kill", "win"])

    
def jade():    
    roomBuilder([False, True], "the jade room", True, ["kill","win"])    

    
def diamond():    
    roomBuilder([False, True], "the diamond room", False, ["kill","jade"])    


def sapphire():    
    roomBuilder([True, False], "the sapphire room", False, ["emerald", "kill"])


def ruby():    
    roomBuilder([False, True], "the ruby room", False, ["kill", "opal"])


    
# ([list of doors(T/F)], The Room Name, last room(T,F)), [list of next rooms])
def roomBuilder(roomList, roomName, isEndRoom, nextRooms):
    print(f"You have just entered {roomName}.")
    time.sleep(delay) #wait for the next message
    roomCount = len(roomList)
    choices = []
    
# Dynamically build an input message based on my number of doors
    inputMessage = "Choose a door ("
    
# Add each door name to the list and to a message | e.g. (door 1, door 2, door 3)
    doorMessage = ""
    for count in range(roomCount):
        choices.append(f"door {count + 1}")
        if count + 1 < roomCount:
            doorMessage += f"door {count + 1}, "
        else:
            doorMessage += f"door {count + 1}):  "

# Add the door message onto the back of the input message
    inputMessage += doorMessage
    time.sleep(delay)
    
    while True:
        command = input(inputMessage).lower()
        
        #print(command)
        if command in choices:
            if roomList[choices.index(command)]:
                if isEndRoom:
                    time.sleep(delay)
                    print("You have chosen wisley.")
                    win()
                    break
                else:
                    time.sleep(delay)
                    print("Please proceed to the next room")
                    time.sleep(delay)
                    eval(nextRooms[choices.index(command)] + "()" )
                    break
            else:
                kill()
                break            
        else:
            time.sleep(delay)            
            print(f"Sorry, you must enter {doorMessage}")    
    
    
roomBuilder([True, True, True], "the entrance hall", False, ["diamond","sapphire","ruby"])
#True: safe to go; False: kill room,  nextRoom: where to go
    

    
    