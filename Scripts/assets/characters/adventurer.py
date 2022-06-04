'''Character class for players and AI adventurers'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.characters.character import Character

class Adventurer(Character):
    '''Adventurer class.'''
    def get_valid_connections(self):
        '''Returns the directions and rooms a Character can go.'''
        connections = self._room.get_connections()
        return connections
