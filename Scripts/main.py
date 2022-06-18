''' main to start the game: << python main.py >> '''

from time import sleep
#import yaml
#import pprint
from room_builder import RoomBuilder
from rw_data import Data
from helper_funcs import print_text as pt

if __name__ == "__main__":
    data=Data()
    data_lists = data.load()
    characters_data = data_lists[0]
    items_data = data_lists[1]
    rooms_data = data_lists[2]

    rooms=RoomBuilder()
    game_world=rooms.initialize_room_builder(characters_data, items_data, rooms_data)

    print("\n\n")
    pt(r"   ______      __      ____   ____ _________ _______    ____  _____  _______ ")
    pt(r" /  ___  |    /  \    |_  _| |_  _|_   ___  |_   __ \  |_   \|_   _|/  ___  |")
    pt(r"/ /    \_|   / /\ \     \ \   / /   | |_  \_| | |__) |   |   \ | | |  (___\_|")
    pt(r"| |         / ____ \     \ \ / /    |  _|  _  |  __ /    | |\ \| |  \_____ \ ")
    pt(r"\ \____/\ _/ /    \ \_    \ ' /    _| |___/ |_| |  \ \_ _| |_\   |_|\\____) |")
    pt(r" \______/|____|  |____|    \_/    |_________|____| |___|_____|\____|_______/ ")
    sleep(1)

    pt()
    pt()
    pt("Navigate the caverns and try to escape with as much valuable loot as you can but, "
            "beware your fellow treasure hunters and other more sinister foes lie ahead.")
    sleep(4)
    pt()
    pt()
    pt("***** Your adventure begins *****")
    pt()
    pt()
    sleep(1)
    characters = game_world[1]

    while True:
        for c in characters:
            c.action()
            pt("")
