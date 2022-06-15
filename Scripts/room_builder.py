# import pprint
import yaml
from assets.characters.adventurer import Adventurer
from controllers.playerController import PlayerController
from controllers.adventurerController import AdventurerController
from controllers.controller import Controller
from assets.item import Item
# from assets.items.consumable import Consumable
from assets.items.container import Container
from assets.items.equipment import Equipment
from assets.room import Room

class Room_builder:

    def __init__(self):
        super().__init__()


    def read_yaml(self,file_name):
        """ A function to read YAML file"""
        with open(f"Data/{file_name}.yml") as file:
            # config = yaml.safe_load(f)
            data_list = yaml.safe_load(file)
            # print(roomsList)
        return data_list  # config

    def build_a_room(self,room,characters_dict,items_dict):
        new_room = Room(room['name'], room['description'])
        characters=[]
        for character_obj in room['characters']:
            # create character
            # add character to new_r
            character = characters_dict[character_obj]
            new_char = Adventurer(
                character['name'],
                character['description'],
                character['identifiers'],
                character['base_stats'],
                character['current_health']
                )
            new_char.set_room(new_room)

            if character['controller'] == 'AdventurerController':
                new_char.set_controller(AdventurerController())

            elif character['controller'] == 'PlayerController':
                new_char.set_controller(PlayerController())

            #elif character['controller'] == 'MonsterController':
                #new_char.set_controller(MonsterController())
            else:
                new_char.set_controller(Controller())

            characters.append(new_char)


        if room['floor'] is not None:
            for floor_obj in room['floor']:
                # add item to new_room floor
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
                    # maybe, this is not part of items on floor. but just in case.
                    new_items_on_floor = Container(
                        floor['name'],
                        floor['description'],
                        floor['identifiers'],
                        floor['value'],
                        floor['weight'],
                    )
                new_room.add_item_to_floor(new_items_on_floor)

            if room['furniture'] is not None:
                for furniture_obj in room['furniture']:
                    # create furniture
                    # add items to furniture
                    # add furniture to new_r
                    furniture = items_dict[list(furniture_obj.keys())[0]]
                    new_furniture = Container(
                        furniture['name'],
                        furniture['description'],
                        furniture['identifiers'],
                        furniture['value'],
                        furniture['weight'],
                        )
                    new_room.add_funiture(new_furniture)
        return new_room, characters


    def initialize_room_builder(self, yaml_characters,yaml_items,yaml_rooms):

        rooms = {} #[]
        room_dict = yaml_rooms
        characters =[]


        for room_id in room_dict:
            room =room_dict[room_id]
            a_room =self.build_a_room(room,yaml_characters,yaml_items)
            new_room =a_room [0]
            rooms[room_id] = new_room
            characters.append(a_room[1])
            #rooms.append(new_room)

        #Now, the connections will be established below based on all the rooms built above.
        for room_id in room_dict:
            room=rooms[room_id]
            if room_dict[room_id]['connections'] is not None:
                for connection_obj in room_dict[room_id]['connections']:
                    connection_direction = connection_obj[0]
                    #connected_room_id = connection_obj[1]
                    room.add_room_connection(connection_direction, rooms[connection_obj[1]], False)

            if room_dict[room_id]['monster_connections'] is not None:
                for connection_obj in room_dict[room_id]['monster_connections']:
                    connection_direction = connection_obj[0]
                    #connected_room_id = connection_obj[1]
                    room.add_room_connection(connection_direction, rooms[connection_obj[1]], True)

        return rooms, characters



    #initialize_room_builder(read_yaml('characters'),read_yaml('items'),read_yaml('rooms'))