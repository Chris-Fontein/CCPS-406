'''Contains the Monster Controller class'''

import random
from controllers.aiController import AiController

class MonsterController(AiController):
    '''Monster Controller class.'''
    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        targets = self._character.get_visible_characters()
        if targets:
            target = random.choice(list(targets))
            self._character.attack(target)
            self.message("%s attacks %s" %(self._character.get_name(), target.get_name()))
            self._character.set_last_action("It attacked %s" % target.get_name())
            return

        connections = self._character.get_valid_connections()
        direction = random.choice(list(connections))
        new_room = connections[direction]
        message = "%s moves %s towards %s.\n" %(self._character.get_name(),
                                                direction,
                                                new_room.get_name(),
                                                )
        self._character.move(new_room)
        self._character.set_last_action("It has just arrived at %s" % new_room.get_name())
        self.message(message)
