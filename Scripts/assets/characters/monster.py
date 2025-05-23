'''Character class for monsters'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.characters.character import Character

class Monster(Character):
    '''Monster class.'''
    def get_valid_connections(self):
        '''Returns the directions and rooms a Character can go.'''
        connections = self._room.get_connections()
        monster_connections = self._room.get_monster_connections()

        all_connections = {}
        for con in connections:
            all_connections[con] = connections[con]
        for con in monster_connections:
            all_connections[con] = monster_connections[con]

        return all_connections

    def attacked(self, attack_value, attacker):
        '''Monsters don't take damage'''
        return 0
