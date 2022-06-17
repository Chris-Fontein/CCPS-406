'''Controller class base Adventurer AI.'''

#Imports
#Python imports
import random
#Third party imports
#Local imports
from controllers.controller import Controller

class AiController(Controller):
    '''Base AiController class.'''

    def attacked(self, attacker, damage):
        '''Controller response to being attacked'''
        if isinstance(attacker.get_controller, AiController):
            message = [attacker.get_name(), "attacked", self._character.get_name()]
            if damage > 0:
                message.extend(["dealing", str(damage), "damage"])
                if self._character.get_current_health() <= 0:
                    message.append(", killing them")
            else:
                message.append("but, was not able to penetrate their defences")

            self.message("%s." %" ".join(message))