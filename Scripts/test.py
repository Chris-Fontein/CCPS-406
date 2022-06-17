from time import sleep

"""fine"""
from assets.item import Item
from assets.items.container import Container
from assets.items.equipment import Equipment
#from assets.asset import Asset
from assets.room import Room
from assets.characters.adventurer import Adventurer
from controllers.playerController import PlayerController
from controllers.adventurerController import AdventurerController
from controllers.controller import Controller

char1 = Adventurer(
        name="bob",
        description="A man in red robes",
        identifiers=["man", "bob", "red", "robes"],
        base_stats={"attack":1, "armor":1, "weight":15, "health":10},
        current_health=10
    )
char2 = Adventurer(
        name="gil",
        description="A woman in black robes",
        identifiers=["woman", "bob", "red", "robes"],
        base_stats={"attack":3, "armor":0, "weight":15, "health":10},
        current_health=10
    )
char3 = Adventurer(
        name="carol",
        description="A man in grey robes",
        identifiers=["woman", "carol", "green", "robes"],
        base_stats={"attack":1, "armor":1, "weight":15, "health":5},
        current_health=10
    )
char4 = Adventurer(
        name="dave",
        description="A man in grey robes",
        identifiers=["man", "dave", "grey", "robes"],
        base_stats={"attack":1, "armor":1, "weight":15, "health":5},
        current_health=10
    )
char5 = Adventurer(
        name="Golem",
        description="A big rock guy",
        identifiers=["golem", "rock", "guy"],
        base_stats={"attack":1, "armor":10, "weight":15, "health":5},
        current_health=10
    )


table = Container(name="table", description="A solid oak table", identifiers=["table", "oak", "solid"], value=0, weight=100)
gem1 = Item(name="saphire", description="a blue gem", identifiers=["blue", "gem", "saphire"], value=50, weight=1)
gem2 = Item(name="ruby", description="a red gem", identifiers=["red", "gem", "ruby"], value=50, weight=1)
gem3 = Item(name="diamond", description="a clear gem", identifiers=["clear", "gem", "diamond"], value=50, weight=1)
cloak = Equipment(name="cloak", description="dark cloak", identifiers=["dark", "cloak"], weight=1, value=1)
armor = Equipment(name="armor", description="dark armor", identifiers=["metal", "armor"], weight=1, value=1)

entrance = Room(name="Entrance", description="The entrance to the cave.  There is a room to the east, and a hallway leading north.")
dead_end = Room(name="Dead end", description="A dead end.  The entrance lies to the west.")
hallway = Room(name="Hallway", description="A long hallway.  The entrance lies to the south and a room to the north.")
dining_room = Room(name="Dining room", description="A large dining room.  A long hallway lies to the south")

char3.set_room(entrance)
char2.set_room(entrance)
char1.set_room(dead_end)
char4.set_room(entrance)
char5.set_room(dead_end)

entrance.add_room_connection("east", dead_end)
dead_end.add_room_connection("west", entrance)
entrance.add_room_connection("north", hallway)
hallway.add_room_connection("south", entrance)
hallway.add_room_connection("north", dining_room)
dining_room.add_room_connection("south", hallway)

dining_room.add_funiture(table)
dining_room.add_item_to_floor(gem1)
dining_room.add_item_to_floor(gem2)
table.add_item_contents(gem3)

char1.set_controller(AdventurerController())
char2.set_controller(PlayerController())
char3.set_controller(Controller())
char4.set_controller(Controller())
char5.set_controller(Controller())

characters = [char1, char2, char3, char4, char5]
characters = [char2]

while True:
    for c in characters:
        c.action()
        sleep(0.25)
