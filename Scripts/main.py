from time import sleep
#import yaml
#import pprint
from room_builder import RoomBuilder
from rw_data import Data

if __name__ == "__main__":
    data=Data()
    data_lists = data.load()
    characters_data = data_lists[0]
    items_data = data_lists[1]
    rooms_data = data_lists[2]

    rooms=RoomBuilder()
    game_world=rooms.initialize_room_builder(characters_data, items_data, rooms_data)

    print("***** Game Start *****")
    characters = game_world[1]

    while True:
        for c in characters:
            c.action()
            sleep(0.25)