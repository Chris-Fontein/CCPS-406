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

        print("%s moves %s towards %s." %(self._character.get_name(),
                                            direction,
                                            self._character.get_room().get_name(),
                                            ))
        self._character.move(connections[direction])
