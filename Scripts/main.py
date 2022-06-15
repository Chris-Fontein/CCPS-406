#import time
#import yaml
#import pprint
from room_builder import Room_builder

if __name__ == "__main__":
    #exec(open("room_builder.py").read())


    rooms=Room_builder()
    game_world=rooms.initialize_room_builder(rooms.read_yaml('characters'), rooms.read_yaml('items'), rooms.read_yaml('rooms'))


    print("***** Game Start *****")
    #print(game_world)
    characters = game_world[1]

    while True:
        for c in characters:
            if len(c)>0:
                c[0].action()

