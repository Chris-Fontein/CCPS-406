import time
import yaml
import pprint
from assets.room import Room

delay = 0.5 #(in seconds)

def read_yaml():
    """ A function to read YAML file"""
    with open('Data/rooms.yml') as file:
        #config = yaml.safe_load(f)
        roomsList = yaml.safe_load(file)
        #print(roomsList)
    return roomsList #config

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

def room00():
    #Entrance
    #Connections: [room00, room02, room11], where room11 is END
    room00 = myRooms[0]
    #roomBuilder([True, True, False], room00['short_description'], True, [room00['connections'][0], room00['connections'][1], room00['connections'][2]])
    roomBuilder([True, True, False], room00['short_description'], False, [room00['connections'][0], room00['connections'][1], room00['connections'][2]])

def room01():
    #Connections: [room00, room03], where room00 is START
    room01 = myRooms[1]
    roomBuilder([True, True], room01['short_description'], False, [room01['connections'][0], room01['connections'][1]])


def room02():
    #Connections: [room00, room04], where room00 is START
    room02 = myRooms[2]
    roomBuilder([True, True], room02['short_description'], False, [room02['connections'][0], room02['connections'][1]])

def room03():
    #Connections: [room01, room05, room07]
    room03 = myRooms[3]
    roomBuilder([True, True, True], room03['short_description'], False, [room03['connections'][0], room03['connections'][1], room03['connections'][2]])    


def room04():
    #Connections: [room02, room06]
    room04 = myRooms[4]
    roomBuilder([True, True], room04['short_description'], False, [room04['connections'][0], room04['connections'][1]])    


def room05():
    #Connections: [room03, room08]
    room05 = myRooms[5]
    roomBuilder([True, True], room05['short_description'], False, [room05['connections'][0], room05['connections'][1]])


def room06():
    #Connections: [room04, room08]
    room06 = myRooms[6]
    roomBuilder([True, True], room06['short_description'], False, [room06['connections'][0], room06['connections'][1]])

def room07():
    #Connections: [room03, room09]
    room07 = myRooms[7]
    roomBuilder([True, True], room07['short_description'], False, [room07['connections'][0], room07['connections'][1]])

def room08():
    #Connections: [room05, room06, room10]
    room08 = myRooms[8]
    roomBuilder([True, True, True], room08['short_description'], False, [room08['connections'][0], room08['connections'][1], room08['connections'][2]])

def room09():
    #Connections: [room07, room10]
    room09 = myRooms[9]
    roomBuilder([True, True], room09['short_description'], False, [room09['connections'][0], room09['connections'][1]])

def room10():
    #Connections: [room09, room08]
    room10 = myRooms[10]
    roomBuilder([True, True], room10['short_description'], False, [room10['connections'][0], room10['connections'][1]])
    
def room11():    
    time.sleep(delay)
    print("Fall into Dungeon... End of the game.")    

    
# ([list of doors(T/F)], The Room Name, last room(T,F)), [list of next rooms])
# 1st parameter: True: safe to go; False: kill room
# nextRoom: where to go
def roomBuilder(roomList, roomName, isEndRoom, nextRooms):
    print(f"You have just entered {roomName}.")
    print("***********************************")
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
                room11()
                #kill()
                break
        else:
            time.sleep(delay)
            print(f"Sorry, you must enter {doorMessage}")
    
def initializeGame():
    room00 = myRooms[0]
    #print(room1)

    #aRoom = Room(room1['name'], room1['description'])
    roomBuilder([True, True, False], room00['short_description'] + ". " + room00['description'] , False, [room00['connections'][0], room00['connections'][1], room00['connections'][2]])
    #True: safe to go; False: kill room,  nextRoom: where to go

# Deserialize YAML into a Room Class
myRooms = read_yaml()
initializeGame()