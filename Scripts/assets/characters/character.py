'''Contains base Character class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

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

    def move():
        pass

    def attack(target):
        pass

    def action():
        do action
        if always_print || player in room:
            print action

