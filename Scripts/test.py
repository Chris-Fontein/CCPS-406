"""fine"""
#from assets.item import Item
#from assets.asset import Asset
#from assets.room import Room
from assets.characters.character import Character
from controllers.controller import Controller
from controllers.playerController import PlayerController

char1 = Character(
    "bob",
    "A man in red robes",
    {"attack":1, "armor":1, "weight":15, "health":10},
    10
    )
char2 = Character(
    "gil",
    "A woman in black robes",
    {"attack":3, "armor":0, "weight":15, "health":10},
    10
    )

char1.set_controller(Controller())
char2.set_controller(PlayerController())
char1.action()
char2.action()
