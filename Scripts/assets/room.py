'''Contains room class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Room(Asset):
    '''Room class.'''
    def __init__(self, name, description):
        super().__init__(name, description)

        self._floor = []
        self._furniture = []
        self._characters = set()
        self._connections = {}
        self._monster_connections = {}

    def get_description(self):
        """Returns room's short description."""
        return "".join(["[", self._name, "]"])

    def get_long_description(self):
        """Returns room's long description."""
        short_desc = self.get_description()

        return "\n".join([short_desc, self._description])

    def add_item_to_floor(self, new_item):
        '''Adds the specified item to the floor list.'''
        self._floor.append(new_item)

    def remove_item_from_floor(self, target_item):
        '''Removes the specified item to the floor list.'''
        self._floor.remove(target_item)

    def add_funiture(self, furniture):
        '''
        Adds the specified item to the furniture list.
        Furniture cannot be removed.  This function should only be used during level creation.
        '''
        self._furniture.append(furniture)

    def add_room_connection(self, direction, room, monster_connection = False):
        ''' Adds connection to the specified room.
        Monster connections can only be navigated by the monster while regular connections
        can be navigated by all Characters.
        '''
        connections = monster_connection if self._monster_connections else self._connections
        connections[direction] = room
