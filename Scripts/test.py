"""fine"""
from assets.item import Item
from assets.asset import Asset
from assets.room import Room

plate = Item("plate", "A wooden plate", 1, 1)
plate2 = Item("plate", "A wooden plate", 1, 1)
rock = Item("rock", "A rock", 0, 0)
rock3 = Item("rock", "A rock", 0, 0)
rock2 = Asset("rock", "A rock")
room = Room("entrance", "A dark cavern lies before you.  To the East and South passage lead deeper into the dungeon.  To the south lies the exit to the cave")

print(room.get_description())
print(room.get_long_description())
