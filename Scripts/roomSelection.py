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
    #print("You died")    
    print("Fall into Dungeon... End of the game.")    

#ToDO:
#1. read data file
#   room list is getting from the data file
#   room episode as per room selected
#2. create log file and write to the save file.

def room00():
    #Entrance
    #Connections: [room00, room02, room11], where room11 is END
    room00 = myRooms[0]['room00']
    #roomBuilder([True, True, False], room00['short_description'], True, [room00['connections'][0], room00['connections'][1], room00['connections'][2]])
    #roomBuilder([True, True, False], room00['name'] + ". " + room00['description'], False, [room00['connections']['w'], room00['connections']['e'], room00['connections']['s']])
    roomBuilder([True, True, False], room00['name'] + ". " + room00['description'], False, room00['connections'])

def room01():
    #Connections: [room00, room03], where room00 is START
    room01 = myRooms[1]['room01']
    #roomBuilder([True, True], room01['name'] + ". " + room01['description'], False, [room01['connections'][0], room01['connections'][1]])
    roomBuilder([True, True], room01['name'] + ". " + room01['description'], False, room01['connections'])


def room02():
    #Connections: [room00, room04], where room00 is START
    room02 = myRooms[2]['room02']
    #roomBuilder([True, True], room02['name'] + ". " + room02['description'], False, [room02['connections']['n'], room02['connections']['w']])
    roomBuilder([True, True], room02['name'] + ". " + room02['description'], False, room02['connections'])

def room03():
    #Connections: [room01, room05, room07]
    room03 = myRooms[3]['room03']
    #roomBuilder([True, True, True], room03['name'] + ". " + room03['description'], False, [room03['connections']['n'], room03['connections']['e'], room03['connections']['s']])    
    roomBuilder([True, True, True], room03['name'] + ". " + room03['description'], False, room03['connections'])


def room04():
    #Connections: [room02, room06]
    room04 = myRooms[4]['room04']
    #roomBuilder([True, True], room04['name'] + ". " + room04['description'], False, [room04['connections']['n'], room04['connections']['s']])    
    roomBuilder([True, True], room04['name'] + ". " + room04['description'], False, room04['connections'])


def room05():
    #Connections: [room03, room08]
    room05 = myRooms[5]['room05']
    #roomBuilder([True, True], room05['name'] + ". " + room05['description'], False, [room05['connections']['n'], room05['connections']['w']])
    roomBuilder([True, True], room05['name'] + ". " + room05['description'], False, room05['connections'])


def room06():
    #Connections: [room04, room08]
    room06 = myRooms[6]['room06']
    #roomBuilder([True, True], room06['name'] + ". " + room06['description'], False, [room06['connections']['s'], room06['connections']['w']])
    roomBuilder([True, True], room06['name'] + ". " + room06['description'], False, room06['connections'])

def room07():
    #Connections: [room03, room09]
    room07 = myRooms[7]['room07']
    #roomBuilder([True, True], room07['name'] + ". " + room07['description'], False, [room07['connections']['s'], room07['connections']['n']])
    roomBuilder([True, True], room07['name'] + ". " + room07['description'], False, room07['connections'])
    
def room08():
    #Connections: [room05, room06, room10]
    room08 = myRooms[8]['room08']
    #roomBuilder([True, True, True], room08['name'] + ". " + room08['description'], False, [room08['connections']['n'], room08['connections']['e'], room08['connections']['s']])
    roomBuilder([True, True, True], room08['name'] + ". " + room08['description'], False, room08['connections'])

def room09():
    #Connections: [room07, room10]
    room09 = myRooms[9]['room09']
    #roomBuilder([True, True], room09['name'] + ". " + room09['description'], False, [room09['connections']['e'], room09['connections']['s']])
    roomBuilder([True, True], room09['name'] + ". " + room09['description'], False, room09['connections'])

def room10():
    #Connections: [room09, room08]
    room10 = myRooms[10]['room10']
    #roomBuilder([True, True], room10['name'] + ". " + room10['description'], False, [room10['connections']['w'], room10['connections']['s']])
    roomBuilder([True, True], room10['name'] + ". " + room10['description'], False, room10['connections'])
    
def room11():    
    #Connections: [room01, room10, room09, room06]
    room11 = myRooms[11]['room11']
    #roomBuilder([True, True, True, True], room11['name'] + ". " + room11['description'], False, [room11['monster_connections']['n'], room11['monster_connections']['s'], room11['monster_connections']['w'], room11['monster_connections']['e']])
    roomBuilder([True, True, True, True], room11['name'] + ". " + room11['description'], False, room11['monster_connections'])
    
def room12():    
    time.sleep(delay)
    print("Fall into Dungeon... End of the game.")

    
# ([list of doors(T/F)], The Room Name, last room(T,F)), [list of next rooms])
# 1st parameter: True: safe to go; False: kill room
# nextRoom: where to go
def roomBuilder(roomList, roomName, isEndRoom, nextRooms):
    print(f"******************************************")
    print(f"You have just entered {roomName}.")
    print(f"(input keyword: [n]North, [e]East, [s]South, [w]West, & [q]Quit)")
    time.sleep(delay) #wait for the next message
    roomCount = len(roomList)
    choices = []
    nextRoomNames = []

# Dynamically build an input message based on my number of doors
    #inputMessage = "Choose a door ("
    inputMessage = "Next, you are heading toward the ("

# Add each door name to the list and to a message | e.g. (door 1, door 2, door 3)
    doorMessage = ""
    for count in range(roomCount):
        #choices.append(f"door {count + 1}")
        choices.append(f"{nextRooms[count][0]}")
        nextRoomNames.append(f"{nextRooms[count][1]}")
        if count + 1 < roomCount:
            #doorMessage += f"door {count + 1}, "
            doorMessage += f"{nextRooms[count][0]}, "
        else:
            #doorMessage += f"door {count + 1}):  "
            doorMessage += f"{nextRooms[count][0]}):  "

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
                    eval(nextRooms[choices.index(command)][1] + "()" )
                    #eval(nextRooms[choices.index(command)] + "()" )
                    break
            else:
                room11()
                #kill()
                break
        elif command == "q":
           kill()
           break
        else:
            time.sleep(delay)
            print(f"Sorry, you must enter {doorMessage}")
    
def initializeGame():
    room00 = myRooms[0]['room00']
    #print(room1)

    #aRoom = Room(room1['name'], room1['description'])
    #roomBuilder([True, True, False], room00['name'] + ". " + room00['description'] , False, [room00['connections']['w'], room00['connections']['e'], room00['connections']['s']])
    roomBuilder([True, True, False], room00['name'] + ". " + room00['description'] , False, room00['connections'])
    #True: safe to go; False: kill room,  nextRoom: where to go

# Deserialize YAML into a Room Class
myRooms = read_yaml()
initializeGame()