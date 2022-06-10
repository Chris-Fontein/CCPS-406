import yaml
import pprint
from assets.characters.adventurer import Adventurer
from assets.item import Item
#from assets.items.consumable import Consumable
from assets.items.container import Container
from assets.items.equipment import Equipment
from assets.room import Room

def room_yaml():
    """ A function to read YAML file"""
    with open('Data/rooms.yml') as file:
        #config = yaml.safe_load(f)
        roomsList = yaml.safe_load(file)
        #print(roomsList)
    return roomsList #config

def character_yaml():
    """ A function to read YAML file"""
    with open('Data/characters.yml') as file:
        #config = yaml.safe_load(f)
        charactersList = yaml.safe_load(file)
        #print(roomsList)
    return charactersList #config

def item_yaml():
    """ A function to read YAML file"""
    with open('Data/items.yml') as file:
        #config = yaml.safe_load(f)
        itemsList = yaml.safe_load(file)
        #print(roomsList)
    return itemsList #config
  
def initializeRoomBuilder():
    rooms = []
    charactersDict = yaml_characters
    itemsDict = yaml_items
    
    for roomObj in yaml_rooms:
        roomID = list(roomObj.keys())[0]
        room =roomObj[roomID]
        new_room = Room(room['name'], room['description'])
        
        for characterObj in room['characters']:
           #create character 
           #add character to new_r
           character = charactersDict[characterObj]
           new_char =Adventurer(
               character['name'],
               character['description'],
               character['identifiers'],
               character['base_stats'],
               character['current_health']
               )
           new_char.set_room(new_room)
           
        if room['floor'] is not None:
            for floorObj in room['floor']:
                #add item to new_room floor
                floor = itemsDict[floorObj]
                if floor['type'] == 'item':
                    new_items_on_floor = Item(
                        floor['name'],
                        floor['description'],
                        floor['identifiers'], 
                        floor['value'], 
                        floor['weight']
                        )
                    
                elif floor['type'] == 'equipment':
                    new_items_on_floor = Equipment(
                        floor['name'],
                        floor['description'],
                        floor['identifiers'], 
                        floor['value'], 
                        floor['weight'],
                        floor['slot'],
                        floor["equipValue"]
                    )
                elif floor['type'] == 'consumable':
                    new_items_on_floor = Equipment(
                        floor['name'],
                        floor['description'],
                        "",
                        "",
                        "",
                        "",
                        floor["effect"]
                    )               
                else:
                    #maybe, this is not part of items on floor. but just in case.
                    new_items_on_floor = Container(
                        floor['name'],
                        floor['description'],
                        floor['identifiers'],
                        floor['value'],
                        floor['weight']
                    )
                new_room.add_item_to_floor(new_items_on_floor)
        
        if room['furniture'] is not None:
            for furnitureObj in room['furniture']:
                #create furniture
                #add items to furniture
                #add furniture to new_r 
                furniture = itemsDict[list(furnitureObj.keys())[0]]
                new_furniture = Container(
                    furniture['name'],
                    furniture['description'],
                    furniture['identifiers'],
                    furniture['value'],
                    furniture['weight'])
                new_room.add_funiture(new_furniture)
                
        if room['connections'] is not None:
            for connectionObj in room['connections']:
                connectionDirection = connectionObj[0]
                connectedRoomID = connectionObj[1]
                hasMonsterConnection = bool(room['monster_connections'])
                new_room.add_room_connection(connectionDirection, connectedRoomID,hasMonsterConnection)
                
        rooms.append(new_room)
        
    #for r in rooms:



# Deserialize YAML into a Room Class
yaml_items = item_yaml()
yaml_rooms = room_yaml()
yaml_characters = character_yaml()
initializeRoomBuilder()