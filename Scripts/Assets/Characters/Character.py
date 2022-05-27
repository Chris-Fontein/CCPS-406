'''Contains base Character class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Character(Asset):
    '''Character class.'''
    def __init__(self, name, description, stats, weight_limit):
        super().__init__(name, description)
        self._stats = stats
        self._weight_limit = weight_limit

        self._room = None
        self._weight = 0
        self._effects = []
        self._inventory = []

    def __hash__(self):
        return hash(repr(self))

    def set_room(self, room):
        '''Sets the room the Character is currently located in.'''
        self._room = room

    def adjust_weight(self, adjustment):
        '''Adjust the character's weight load by the specified amount.'''
        self._weight += adjustment