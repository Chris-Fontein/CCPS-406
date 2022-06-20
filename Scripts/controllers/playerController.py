'''Controller class used to interact with the player.'''

#Imports
#Python imports
import sys
from time import sleep
#Third party imports
#Local imports
from controllers.controller import Controller

from assets.asset import Asset
from assets.item import Item
from assets.items.equipment import Equipment
from assets.items.container import Container
from assets.items.openable_container import OpenableContainer


class PlayerController(Controller):
    '''Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''

        if self._character.has_visited():
            self.message(self._character.get_room().get_description())
        else:
            self.message(self._character.get_room().get_long_description())

        if self._character.get_room().get_exit():
            self.win()

        valid_action = False
        while not valid_action:
            command = input("\n> ")
            valid_action = self.parse_command(command)

    def win(self):
        '''Check if the player would like to end the game'''
        yes = ["yes", "y"]
        cont = ["no", "n"]
        self.message("You have made it to the outside.  Would you like to leave with your loot?")
        while True:
            response = input("> ").lower()
            if response in yes:
                inventory = self._character.get_inventory()
                equipment = self._character.get_equipment()

                value = 0
                for item in inventory:
                    value += item.get_value()

                for slot in equipment:
                    if equipment[slot]:
                        value += equipment[slot].get_value()

                self.message("You have survived the caverns.  You head off back to civilization "
                                "with your newly aquired loot.")
                self.message("You aquired loot totaling %s gold coins in value." %value)
                sleep(5)
                sys.exit()

            elif response in cont:
                self.message("The adventure continues.")
                break

    def parse_command(self, command):
        '''Deconstruct user input to determin action'''
        if not command:
            return False

        split = command.lower().split(" ")

        action = split[0]
        details = split[1:]

        if action in ["quit", "exit"]:
            sys.exit()

        (action, details) = substitute_commands(action, details)

        actions ={
            "use": self.use,
            "look": self.look,
            "move": self.move,
            "open": self.open,
            "close": self.close,
            "equip": self.equip,
            "unequip": self.unequip,
            "pickup": self.pickup,
            "place": self.place,
            "attack": self.attack,
            }


        if action in actions:
            action_function = actions[action]
            return action_function(details)

        self.message("I don't recognise '%(action)s' as an action." %locals())
        return False

    def use(self, details):
        '''Attempt to use the specified items'''
        self.message("use: %s" %details)
        return True

    def open(self, details):
        '''Attempt to open the specified container'''
        container = self.get_container(details)
        if not container:
            return False

        result = container.open_close_container(close = False)

        if not result:
            self.message("You open the %s." %container.get_name())
        else:
            self.message("You can't open the %s because it is %s." %(container.get_name(), result))

        return True

    def close(self, details):
        '''Attempt to close the specified container'''
        container = self.get_container(details)
        if not container:
            return False

        result = container.open_close_container(close = True)
        if not result:
            self.message("You close the %s" %container.get_name())
        else:
            self.message("You can't close the %s because it is %s." %(container.get_name(), result))

        return True

    def get_container(self, details):
        '''Search for container matching details'''
        available = self._character.get_available_contents(OpenableContainer)
        matches = find_nested_item(details, available, OpenableContainer)

        if not matches:
            self.message("There are no items in the room like that you can open.")
            return None
        if len(matches) > 1:
            if not check_same(matches):
                self.message("There more then one item that matches that description.")

        return matches[0]

    def look(self, details):
        '''Attempt to look at the specified asset'''
        if not details or details[0] == "room":
            self.message(self._character.get_room().get_long_description())
            return False
        if details[0] in ["me", "self"]:
            self.message(self._character.get_description())
            return False

        characters = self._character.get_visible_characters()
        available = self._character.get_available_contents(Asset)
        available.extend(characters)
        items = find_nested_item(details, available)

        same = check_same(items)
        if not items:
            self.message("There is nothing in the room that matches that description.")
        elif same:
            item = items[0]
            if isinstance(item, Container):
                self.message(item.get_container_description())
            elif isinstance(item, Asset):
                self.message(item.get_description())
        else:
            self.message("More then one thing in the room matches that description.")
        return False

    def pickup(self, details):
        '''Attempt to pickup the specified item'''
        available = self._character.get_available_contents(Item, False)
        items = find_nested_item(details, available)

        if not items:
            self.message("There is nothing in the room that matches that description.")
            return False

        same = check_same(items)

        if same:
            item = items[0]
            result = self._character.pickup(item)
            if result:
                self.message("You pick up the %s." %item.get_name())
                return True

            self.message("With everything you are carrying you wouldn't be able to carry that.")
        return False

    def place(self, details):
        '''Take item from inventory and place it on the ground'''
        inventory = self._character.get_inventory()
        target = None

        if not target:
            target = self._character.get_room()
        matches = search_contents(details, inventory)

        if not matches:
            self.message("You don't have anything like that in your inventory.")
            return False

        item = matches[0]
        self._character.drop_item(item, target)
        self.message("You place your %s on the floor" %item.get_name())
        return True

    def move(self, details):
        '''Attempt to move in the specified direction'''
        if not details:
            self.message("You didn't specify a direction.")
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
            #if direction in valid_dirs:
            if direction in list(valid_dirs.keys()):
                final_dir = direction
                break
        if final_dir:
            self._character.move(valid_dirs[final_dir])
            self.message("You move %s towards %s." %(final_dir,
                                                    self._character.get_room().get_name()
                                                    ))
            return True
        self.message("You did not specify a valid direction.")
        return False

    def equip(self, details):
        '''Attempt to equip the specified item'''
        if not details:
            self.message("Please specify what you would like to equip.")
            return False

        contents = self._character.get_contents(Equipment)

        matches = search_contents(details, contents)

        if not matches:
            self.message("You don't have anything that matches that description.")
            return False

        if not check_same(matches):
            return False

        item = matches[0]
        result, unequipped = self._character.equip(item)

        if not result:
            self.message("You can't equip that item.")
            return False
        if unequipped:
            self.message("You remove your %s and equip your %s." %(unequipped.get_name(),
                                                                    item.get_name(),
                                                                    ))
        else:
            self.message("You equip your %s." %item.get_name())

        return True

    def unequip(self, details):
        '''Attempt to unequip the specified item'''
        equipment = self._character.get_equipment()
        equipment_items = []
        for slot in equipment:
            if slot in details:
                item = self._character.unequip(slot)
                if item:
                    self.message("You unequipped your %s." %item.get_name())
                    return True
                self.message("You have nothing equipped to %s." %slot)
                return False
            if equipment[slot]:
                equipment_items.append(equipment[slot])

        matches = search_contents(details, equipment_items)

        if matches:
            item = matches[0]
            for slot in equipment:
                if equipment[slot] == item:
                    item = self._character.unequip(slot)
                    self.message("You unequipped your %s." %item.get_name())
                    return True

        return False

    def attack(self, details):
        '''Attempt to attack the specified character'''
        characters = self._character.get_visible_characters()

        if not characters:
            self.message("There is no one else in the room with you.")
            return False
        matches = search_contents(details, characters)
        if not matches:
            self.message("There is no one like that in the room.")
            return False

        if len(matches) > 1:
            if all(matches[0] == m for m in matches):
                target = matches[0]
            else:
                self.message("There is more then one person in the "
                                "room that matches that description")
                return False
        else:
            target = matches[0]
        damage = self._character.attack(target)

        message = ["You attack", target.get_name()]

        if damage > 0:
            message.extend(["dealing", str(damage), "damage"])
            if target.get_current_health() <= 0:
                message.append(", killing them")
        else:
            message.append("but, are not able to penetrate their defences")

        self.message("%s." %" ".join(message))
        return True

    def attacked(self, attacker, damage):
        health = self._character.get_current_health()
        message = [attacker.get_name(), "attacked you"]
        if damage > 0:
            message.extend(["dealing", str(damage), "damage"])
            if health <= 0:
                message.append(", killing you")
        else:
            message.append("but, was not able to penetrate your defences")

        self.message("%s." %" ".join(message))

        if health <= 0:
            sleep(3)
            sys.exit()

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

def find_nested_item(details, items, instance = Asset):
    '''
        Parse details to handle instructions indicating items in a container to identify matching
        items.
    '''
    sections = []
    current_section = []

    for detail in details:
        if detail in set(["in", "on"]):
            sections.append(current_section)
            current_section = []
        current_section.append(detail)

    sections.append(current_section)
    current_items = items
    sections.reverse()
    for i in range(len(sections)):
        level = sections[i]
        item_matches = search_contents(level, current_items)
        if not item_matches:
            current_items = []
            break
        if i < len(sections) - 1:
            current_items = []
            for item in item_matches:
                if isinstance(item, Container):
                    current_items.extend(item.get_contents(instance))
        else:
            current_items = item_matches

    return current_items

def check_same(items):
    '''checks if all items are equivalent'''
    if not items:
        return False
    same = True
    first_item = items[0]
    for item in items:
        same = same and (item == first_item)
    return same

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
    elif action == "remove":
        action = "unequip"
    elif action == "drink":
        action = "use"
    elif action == "fight":
        action = "attack"
    elif action in ["take", "grab", "pick"]:
        action = "pickup"
    elif action in ["search", "examin"]:
        action = "look"
    elif action in ["drop", "put"]:
        action = "place"

    return action, details
