'''Controller class used to interact with the player.'''

#Imports
#Python imports
#Third party imports
#Local imports
from controllers.controller import Controller

from assets.items.equipment import Equipment
from assets.characters.character import Character


class PlayerController(Controller):
    '''Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        if self._character.has_visited():
            print(self._character.get_room().get_description())
        else:
            print(self._character.get_room().get_long_description())

        valid_action = False
        while not valid_action:
            command = input("\n> ")
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
            "open": self.open,
            "close": self.close,
            "equip": self.equip,
            "pickup": self.pickup,
            "attack": self.attack,
            }

        if action in actions:
            action_function = actions[action]
            return action_function(details)

        print("I don't recognise '%(action)s' as an action." %locals())
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

    def pickup(self, details):
        '''Attempt to pickup the specified item'''
        print("pickup: %s" %details)
        return True

    def move(self, details):
        '''Attempt to move in the specified direction'''
        if not details:
            print("You didn't specify a direction.")
            return False

        valid_dirs = self._character.get_valid_connections()

        dir_conversion = {
            "n":"north",
            "s":"south",
            "e":"east",
            "w":"west",
            }

        final_dir = None
        for direction in details:
            direction = dir_conversion.get(direction, direction)
            if direction in valid_dirs:
                final_dir = direction
                break
        if final_dir:
            self._character.move(valid_dirs[final_dir])
            print("You move %s towards %s." %(final_dir, self._character.get_room().get_name()))
            return True
        print("You did not specify a valid direction.")
        return False

    def equip(self, details):
        '''Attempt to equip the specified item'''
        print("equip: %s" %details)
        return True

    def attack(self, details):
        '''Attempt to attack the specified character'''
        room = self._character.get_room()
        characters = room.get_characters() - set([self._character])

        if not characters:
            print("There is no one else in the room with you.")
            return False
        matches = search_contents(details, characters)
        if not matches:
            print("There is no one like that in the room.")
            return False
        if len(matches) > 1:
            print("There is more then one person in the room that matches that description")
            return False

        target = matches[0]
        damage = self._character.attack(target)

        message = ["You attack", target.get_name()]

        if damage > 0:
            message.extend(["dealing", str(damage), "damage"])
            if target.get_current_health() <= 0:
                message.append(", killing them")
        else:
            message.append("but, are not able to penetrate their defences.")
            print(" ".join(message))
            return False

        print("%s." %" ".join(message))
        return True


def search_contents(identifiers, items):
    '''Returns the best matches in a list of items'''
    id_set = set(identifiers)
    match_value = 1
    matches = []
    for item in items:
        match_number = item.match_identifiers(id_set)
        if match_number >= match_value:
            if match_number > match_value:
                matches = []
                match_value = match_number
            matches.append(item)

    return matches


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
    elif action == "take":
        action = "pickup"
    elif action == "grab":
        action = "pickup"
    elif action == "search":
        action = "look"

    return action, details
