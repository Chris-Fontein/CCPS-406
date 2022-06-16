from time import sleep
#import yaml
#import pprint
from room_builder import Room_builder
from data.rw_data import Data
from data.room_data_structure import RoomClass

if __name__ == "__main__":
    #exec(open("room_builder.py").read())

    data=Data()
    #characters_data = data.read_yaml('characters')
    #items_data = data.read_yaml('items')
    #rooms_data=data.read_yaml('rooms')
    data_lists = data.load()
    characters_data = data_lists[0]
    items_data = data_lists[1]
    rooms_data = data_lists[2]

    rooms=Room_builder()
    #game_world=rooms.initialize_room_builder(rooms.read_yaml('characters'), rooms.read_yaml('items'), rooms.read_yaml('rooms'))
    game_world=rooms.initialize_room_builder(characters_data, items_data, rooms_data)
    print("***********************")
    print("***** Game Start *****")
    print("***********************")
    #print(game_world)
    characters = game_world[1]
    #print (characters)



    #creating room dictionary lists:
    room_keys = list(rooms_data.keys())
    room_obj_dict={}
    for r_key in room_keys:
        room_class_obj = RoomClass(rooms_data[r_key])
        #room_class_obj=RoomClass(rooms_data[r_key]['name'],
        #            rooms_data[r_key]['description'],
        #            rooms_data[r_key]['identifiers'],
        #            rooms_data[r_key]['characters'],
        #            rooms_data[r_key]['floor'],
        #            rooms_data[r_key]['furniture'],
        #            rooms_data[r_key]['connections'],
        #            rooms_data[r_key]['monster_connections'])
        #room_obj_list.append(room_class_obj)
        room_obj_dict[r_key]=room_class_obj

    my_room = RoomClass(rooms_data['room00'])
    my_room.update_room(room_obj_dict, 'room00','name',"Start")


    while True:
        for c in characters:
            #print(c)
            c.action()
            sleep(0.25)