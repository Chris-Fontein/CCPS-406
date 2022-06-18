'''Controller class base Adventurer AI.'''

#Imports
#Python imports
import random
#Third party imports
#Local imports
from controllers.aiController import AiController

class AdventurerController(AiController):
    '''Adventurer Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        if self._character.get_current_health() <= 0:
            return
        connections = self._character.get_valid_connections()
        direction = random.choice(list(connections))
        new_room = connections[direction]
        message = "%s moves %s towards %s.\n" %(self._character.get_name(),
                                                direction,
                                                new_room.get_name(),
                                                )
        self._character.move(new_room)
        self.message(message)

