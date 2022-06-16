from dataclasses import dataclass
from data.container_data_structure import Container
from data.equip_data_structure import Equipment
import yaml

@dataclass
class RoomClass:
    name: str
    description: str
    identifiers: list
    characters: list[str]
    floor:list[str]
    furniture: list[str]
    connections: list[[]]
    monster_connections:list[[]]

    def __init__(self, room_obj):
        self.name = room_obj['name']
        self.description = room_obj['description']
        self.identifiers = room_obj['identifiers']
        self.characters = room_obj['characters']
        self.floor = room_obj['floor']
        self.furniture = room_obj['furniture']
        self.connections = room_obj['connections']
        self.monster_connections = room_obj['monster_connections']

    def noop(self, *args, **kw):
        pass

    def update_room(self, room_data_dict, room_key, field, value):
        #rooms_list = []
        #rooms_dict= {}
        #room_keys = list(room_data_list.keys())
        #for r_key in room_keys:
        #    room_obj=RoomClass(room_data_list[r_key]['name'],
        #              room_data_list[r_key]['description'],
        #              room_data_list[r_key]['identifiers'],
        #              room_data_list[r_key]['characters'],
        #              room_data_list[r_key]['floor'],
        #              room_data_list[r_key]['furniture'],
        #              room_data_list[r_key]['connections'],
        #              room_data_list[r_key]['monster_connections'])
        #    rooms_list.append(room_obj)
        #    rooms_dict[r_key]=room_obj

        match field:
            case 'name':
                room_data_dict[room_key].name = value
                self.name = value
            case 'description':
                room_data_dict[room_key].description = value
                self.description = value
            case 'identifiers':
                room_data_dict[room_key].identifiers = value
                self.identifiers = value
            case 'characters':
                room_data_dict[room_key].characters = value
                self.characters = value
            case 'floor':
                room_data_dict[room_key].floor = value
                self.floor = value
            case 'furniture':
                room_data_dict[room_key].furniture = value
                self.furniture = value
            case 'connections':
                room_data_dict[room_key].connections = value
                self.connections = value
            case 'monster_connections':
                room_data_dict[room_key].monster_connections = value
                self.monster_connections = value

        #rooms_dict[list(room_data_list.keys())[0]].name= "Start"

        yaml.emitter.Emitter.process_tag = self.noop
        with open(r'./data/text_files/saved_rooms.yml','w') as file:
            document=yaml.dump(room_data_dict, file, sort_keys=False)





    #def __getitem__(self, item):
        #return self.name[item], self.description[item], self.identifiers[item], self.characters[item],self.floor[item],self.furniture[item],self.connections[item],self.monster_connections[item]