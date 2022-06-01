'''Contains base Character class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset
from assets.room import Room
from assets.item import Item
from assets.items.container import Container

class Character(Asset):
    '''Character class.'''
    def __init__(self, name, description, base_stats, current_health, controller):
        super().__init__(name, description)
        self._base_stats = base_stats
        self._stat_modifiers = {}
        self._current_health = current_health
        self._room = None
        self._weight = 0
        self._effects = []
        self._inventory = []
        self._controller = controller
        self._rooms_visited = set()


    def __hash__(self):
        return hash(repr(self))

    def set_room(self, room):
        '''Sets the room the Character is currently located in.'''
        self._room = room

    def adjust_weight(self, adjustment):
        '''Adjust the character's weight load by the specified amount.'''
        self._weight += adjustment
    
    def look(self, target):
        '''Returns the description of the target.'''
        if isinstance(target, Room) and (self._room == target):
            return target.get_long_description()
        elif isinstance(target, Container) and (target in self._room._furniture):
            target_desc = target.get_container_description()
            return target_desc[0].upper() + target_desc[1:]
        elif isinstance(target, Character) and (target in self._room._characters):
            target_desc = target._description
            return target_desc[0].upper() + target_desc[1:]
        elif isinstance(target, Item):
            if (target in self._room._floor) or (target in self._inventory):
                target_desc = target._description
                return target_desc[0].upper() + target_desc[1:]
            else:
                for x in self._room._furniture:
                    if target in (x._content) and (x._open):
                        target_desc = target._description
                        return target_desc[0].upper() + target_desc[1:]
                return "You cannot see anything like that."
        else:
            return "You cannot see anything like that."


    def move():
        pass

    def attack(target):
        pass

   # def action():
        #do action
        #f always_print or player in room:
        #   print action

