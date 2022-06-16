from time import sleep
#import yaml
#import pprint
from room_builder import Room_builder
from data.rw_data import Data

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

    room_class_obj = data.data_mapping(rooms_data)

    rooms=Room_builder()
    #game_world=rooms.initialize_room_builder(rooms.read_yaml('characters'), rooms.read_yaml('items'), rooms.read_yaml('rooms'))
    game_world=rooms.initialize_room_builder(characters_data, items_data, rooms_data)
    print("***********************")
    print("***** Game Start *****")
    print("***********************")
    #print(game_world)
    characters = game_world[1]
    print (characters)

    while True:
        for c in characters:
            print(c)
            c.action()
            sleep(0.25)