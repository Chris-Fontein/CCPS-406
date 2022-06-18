import random
from controllers.aiController import AiController

class MonsterController(AiController):
    '''Monster Controller class.'''
    def __init__(self):
        self._character = None

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        targets = self._character.get_room().get_characters()

        if targets:
            target = random.choice(list(targets))
            self._character.attack(target)
            self.message("%s attacks %s" %(self._character.get_name(), target.get_nam()))
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
