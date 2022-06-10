import yaml
import pprint
from assets.room import Room

def read_yaml():
    """ A function to read YAML file"""
    with open('Data/rooms.yml') as file:
        #config = yaml.safe_load(f)
        roomsList = yaml.safe_load(file)
        #print(roomsList)
    return roomsList #config
  
def initializeRoomBuilder():
    rooms = []
    for roomObj in yaml_rooms:
        roomID = list(roomObj.keys())[0]
        room =roomObj[roomID]
        new_r = Room(room['name'], room['description'])
                
        for character in room['characters']:
           #create character 
           #add character to new_r 
        for floor in room['floor']:
           #add item to new_r floor
        for furniture in room['furniture']:
            #create furniture
            #add items to furniture
            #add furniture to new_r 
        for connectection in room['connections']:
            
        for connectection in room['monster_connections'':
        
        rooms.append(new_r)
    #for r in rooms:
    
    
  
  # Deserialize YAML into a Room Class
yaml_rooms = read_yaml()
initializeRoomBuilder()