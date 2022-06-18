'''Contains the Monster Controller class'''

import random
from controllers.aiController import AiController

class MonsterController(AiController):
    '''Monster Controller class.'''
    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        targets = self._character.get_visible_characters()
        if targets:
            self.attack()

        else:
            self.move()
