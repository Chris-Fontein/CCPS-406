'''Controller class base Adventurer AI.'''

#Imports
#Python imports
import random
#Third party imports
#Local imports
from controllers.controller import Controller

class AdventurerController(Controller):
    '''Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        connections = self._character.get_valid_connections()
        direction = random.choice(list(connections))
        new_room = connections[direction]
        message = "%s moves %s towards %s.\n" %(self._character.get_name(),
                                                direction,
                                                new_room.get_name(),
                                                )
        self._character.move(new_room)
        print(message)
