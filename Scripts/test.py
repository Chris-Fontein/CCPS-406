"""fine"""
#from assets.item import Item
from assets.items.container import Container
#from assets.asset import Asset
from assets.room import Room
from assets.characters.adventurer import Adventurer
from controllers.playerController import PlayerController
from controllers.adventurerController import AdventurerController

char1 = Adventurer(
        "bob",
        "A man in red robes",
        ["man, bob, red, robes"],
        {"attack":1, "armor":1, "weight":15, "health":10},
        10
    )
char2 = Adventurer(
        "gil",
        "A woman in black robes",
        ["man, bob, red, robes"],
        {"attack":3, "armor":0, "weight":15, "health":10},
        10
    )

table = Container("table", "A solid oak table", ["table", "oak", "solid"], 0, 100, True)

entrance = Room("Entrance", "The entrance to the cave.  There is a room to the east, and a hallway leading north.")
dead_end = Room("Dead end", "A dead end.  The entrance lies to the west.")
hallway = Room("Hallway", "A long hallway.  The entrance lies to the south and a room to the north.")
dining_room = Room("Dining room", "A large dining room.  A long hallway lies to the south")

char2.set_room(entrance)
char1.set_room(dead_end)

entrance.add_room_connection("east", dead_end)
dead_end.add_room_connection("west", entrance)
entrance.add_room_connection("north", hallway)
hallway.add_room_connection("south", entrance)
hallway.add_room_connection("north", dining_room)
dining_room.add_room_connection("south", hallway)

dining_room.add_funiture(table)

char1.set_controller(AdventurerController())
char2.set_controller(PlayerController())
while True:
    char1.action()
    char2.action()
