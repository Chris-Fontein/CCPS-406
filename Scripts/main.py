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
    characters = game_world['room00']._characters
    while True:
        for c in characters:
            c.action()
