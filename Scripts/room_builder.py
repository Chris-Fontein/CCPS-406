#import pprint
import yaml
from assets.characters.adventurer import Adventurer
from assets.item import Item
#from assets.items.consumable import Consumable
from assets.items.container import Container
from assets.items.equipment import Equipment
from assets.room import Room

def read_yaml(file_name):
    """ A function to read YAML file"""
    with open(f"Data/{file_name}.yml") as file:
        #config = yaml.safe_load(f)
        data_list = yaml.safe_load(file)
        #print(roomsList)
    return data_list #config

def initialize_room_builder(yaml_items, yaml_rooms, yaml_characters):

    rooms = []

    #for room in yaml_rooms:
        #room =build_room()
        #rooms[roomID] = room

    characters_dict = yaml_characters
    items_dict = yaml_items
    room_dict = yaml_rooms

    for room_id in room_dict:
        room =room_dict[room_id]
        new_room = Room(room['name'], room['description'])

        for character_obj in room['characters']:
           #create character
           #add character to new_r
           character = characters_dict[character_obj]
           new_char =Adventurer(
               character['name'],
               character['description'],
               character['identifiers'],
               character['base_stats'],
               character['current_health']
               )
           new_char.set_room(new_room)

        if room['floor'] is not None:
            for floor_obj in room['floor']:
                #add item to new_room floor
                floor = items_dict[floor_obj]
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
            for furniture_obj in room['furniture']:
                #create furniture
                #add items to furniture
                #add furniture to new_r
                furniture = items_dict[list(furniture_obj.keys())[0]]
                new_furniture = Container(
                    furniture['name'],
                    furniture['description'],
                    furniture['identifiers'],
                    furniture['value'],
                    furniture['weight'])
                new_room.add_funiture(new_furniture)

        if room['connections'] is not None:
            for connection_obj in room['connections']:
                connection_direction = connection_obj[0]
                connected_room_id = connection_obj[1]
                has_monster_connection = bool(room['monster_connections'])
                new_room.add_room_connection(connection_direction, connected_room_id,has_monster_connection)

        rooms.append(new_room)

    #for r in rooms:

initialize_room_builder(read_yaml('items'),read_yaml('rooms'),read_yaml('characters'))