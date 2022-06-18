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

    def attack(self):
        '''Attack a random Character in the room'''
        targets = self._character.get_visible_characters()
        target = random.choice(list(targets))
        self._character.attack(target)
        self.message("%s attacks %s" %(self._character.get_name(), target.get_name()))
        self._character.set_last_action("They attacked %s" % target.get_name())
        return

    def move(self):
        '''Move to a random room'''
        connections = self._character.get_valid_connections()
        direction = random.choice(list(connections))
        new_room = connections[direction]
        message = "%s moves %s towards %s.\n" %(self._character.get_name(),
                                                direction,
                                                new_room.get_name(),
                                                )
        self._character.move(new_room)
        self._character.set_last_action("They have just arrived at %s" % new_room.get_name())
        self.message(message)
