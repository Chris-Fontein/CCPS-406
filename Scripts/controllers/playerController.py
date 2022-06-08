'''Controller class used to interact with the player.'''

#Imports
#Python imports
#Third party imports
#Local imports
from controllers.controller import Controller

class PlayerController(Controller):
    '''Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        valid_action = False
        while not valid_action:
            command = input("> ")
            valid_action = self.parse_command(command)

    def parse_command(self, command):
        '''Deconstruct user input to determin action'''
        if not command:
            return False

        split = command.lower().split(" ")

        action = split[0]
        details = split[1:]

        (action, details) = substitute_commands(action, details)

        actions ={
            "use": self.use,
            "look": self.look,
            "move": self.move,
            "take": self.take,
            "open": self.open,
            "close": self.close,
            "equip": self.equip,
            "attack": self.attack,
            }

        if action in actions:
            action_function = actions[action]
            return action_function(details)

        print("I don't recognise '%(action)s' as an action" %locals())
        return False

    def use(self, details):
        '''Attempt to use the specified items'''
        print("use: %s" %details)
        return True

    def open(self, details):
        '''Attempt to open the specified container'''
        print("open: %s" %details)
        return True

    def close(self, details):
        '''Attempt to close the specified container'''
        print("close: %s" %details)
        return True

    def look(self, details):
        '''Attempt to look at the specified asset'''
        print("look: %s" %details)
        return False

    def take(self, details):
        '''Attempt to pickup the specified item'''
        return True

    def move(self, details):
        '''Attempt to move in the specified direction'''
        if not details:
            print("You didn't specify a direction")
            return False

        valid_dirs = self._character.get_valid_connections()

        final_dir = None
        for direction in details:
            if direction in valid_dirs:
                final_dir = direction
                break
        if final_dir:
            self._character.move(valid_dirs[final_dir])
            print("You move %s towards %s." %(final_dir, self._character.get_room().get_name()))
            return True
        print("No valid direction specified")
        return False

    def equip(self, details):
        '''Attempt to equip the specified item'''
        print("equip: %s" %details)
        return True

    def attack(self, details):
        '''Attempt to attack the specified character'''
        print("attack: %s" %details)
        return True


def substitute_commands(action, details):
    '''Modify actions and details with synonymous command'''
    if action in {"s", "south"}:
        action = "move"
        details.insert(0, "south")
    elif action in {"n", "south"}:
        action = "move"
        details.insert(0, "north")
    elif action in {"w", "west"}:
        action = "move"
        details.insert(0, "west")
    elif action in {"e", "east"}:
        action = "move"
        details.insert(0, "east")
    elif action == "wield":
        action = "equip"
    elif action == "drink":
        action = "use"
    elif action == "fight":
        action = "attack"
    elif action == "pickup":
        action = "take"
    elif action == "grab":
        action = "take"

    return action, details
