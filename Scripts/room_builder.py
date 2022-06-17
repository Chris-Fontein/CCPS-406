# import pprint
import yaml
from assets.characters.adventurer import Adventurer
from controllers.playerController import PlayerController
from controllers.adventurerController import AdventurerController
from controllers.controller import Controller
from assets.item import Item
# from assets.items.consumable import Consumable
from assets.items.container import Container
from assets.items.openable_container import OpenableContainer
from assets.items.equipment import Equipment
from assets.room import Room

class Room_builder:

    def __init__(self):
        super().__init__()

    def read_yaml(self,file_name):
        """ A function to read YAML file"""
        with open(f"data/{file_name}.yml") as file:
            # config = yaml.safe_load(f)
            data_list = yaml.safe_load(file)
            # print(roomsList)
        return data_list  # config

    def build_a_room(self,room,characters_dict,items_dict):
        new_room = Room(**room)
        characters=[]
        for character_key in room['characters']:
            # create character
            # add character to new_r
            character_obj = characters_dict[character_key]
            new_char = Adventurer(**character_obj)

            if character_obj['inventory'] is not None:
                for item_key in character_obj['inventory']:
                    item=items_dict[item_key]

                    match item['type']:
                        case 'Equipment':
                            new_item = Equipment(**item)
                            new_char.add_item(new_item)
                        case 'Item':
                            new_item = Item(**item)
                            new_char.add_item(new_item)

            if character_obj['equipped'] is not None:
                for equip_key in character_obj['equipped']:
                    equip=items_dict[equip_key]

                    match equip['type']:
                        case 'Equipment':
                            new_equip = Equipment(**equip)
                            new_char.add_item(new_equip)

            new_char.set_room(new_room)

            if character_obj['controller'] == 'AdventurerController':
                new_char.set_controller(AdventurerController())

            elif character_obj['controller'] == 'PlayerController':
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
                if floor['type'] == 'Item':
                    new_items_on_floor = Item(**floor)

                elif floor['type'] == 'Equipment':
                    new_items_on_floor = Equipment(**floor)
                elif floor['type'] == 'Consumable':
                    new_items_on_floor = Equipment(**floor)
                else:
                    # maybe, this is not part of items on floor. but just in case.
                    new_items_on_floor = Container(**floor)
                new_room.add_item_to_floor(new_items_on_floor)

        if room['furniture'] is not None:
            for furniture_obj in room['furniture']:
                # create furniture
                # add items to furniture
                # add furniture to new_r
                furniture = items_dict[list(furniture_obj.keys())[0]]
                match furniture['type']:
                    #we are creating container here
                    case 'Container':
                        new_furniture = Container(**furniture)
                        new_room.add_funiture(new_furniture)
                    case 'OpenableContainer':
                        new_furniture = OpenableContainer(**furniture)
                        new_room.add_funiture(new_furniture)

                #new_furniture = Container(**furniture)

                #here, we are creating items with container.
                if furniture['content'] is not None:
                    for item_key in furniture['content']:
                        item=items_dict[item_key]

                        match item['type']:
                            case 'Equipment':
                                new_item = Equipment(**item)
                                new_furniture.add_item_contents(new_item)
                            case 'Item':
                                new_item = Item(**item)
                                new_furniture.add_item_contents(new_item)
                            case 'Container':
                                new_item = Container(**item)
                                new_furniture.add_item_contents(new_item)
                            case 'OpenableContainer':
                                new_item = OpenableContainer(**item)
                                new_furniture.add_item_contents(new_item)

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
            characters.extend(a_room[1])
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