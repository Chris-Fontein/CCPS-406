'''Character class for players and AI adventurers'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.items.equipment import Equipment
from assets.characters.character import Character

class Adventurer(Character):
    '''Adventurer class.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._equipment = {
                            "head": None,
                            "body": None,
                            "weapon": None,
                            "shield": None
                            }


    def get_valid_connections(self):
        '''Returns the directions and rooms a Character can go.'''
        connections = self._room.get_connections()
        return connections

    def equip(self, item):
        '''Unequips Equipment in slot and equips item.'''
        slot = item.get_slot()
        message = []
        weight_limit = self._stat_modifiers[Character.WEIGHT_LIMIT]

        if not isinstance(item, Equipment):
            return "That item cannot be equipped."
        if slot not in self._equipment:
            return "Can't equip that."

        #Slot is full. Figure out where to put it
        if self._equipment[slot]:
            current_equip = self._equipment[slot]
            total_weight = item.get_weight() + self._weight

            if total_weight < weight_limit:
                message = [self.unequip(slot)]
            elif total_weight - current_equip.get_weight() < weight_limit:
                message = [self.unequip(slot, True)]
            else:
                return "You are unable to carry that item."

        self._equipment[slot] = item
        message.append("Equip %s." %item.get_name())
        item_stats = item.get_stats()
        self.adjust_weight(item.get_weight())

        for stat in item_stats:
            self._stat_modifiers[stat] += item_stats[stat]

        return " ".join(message)

    def unequip(self, slot, floor = False):
        '''Unequips the Equipent in the specified slot placing it in inventory or on the floor.'''
        if slot not in self._equipment:
            return "That slot doesn't exist."
        if not self._equipment[slot]:
            return "There is nothing equipped in that slot."

        item = self._equipment[slot]
        self._equipment[slot] = None
        self.adjust_weight(-item.get_weight())

        item_stats = item.get_stats()
        for stat in item_stats:
            self._stat_modifiers[stat] -= item_stats[stat]

        message = ["Remove", item.get_name()]
        if floor:
            self._room.add_item_to_floor(item)
            message.append("and place it on the floor.")
        else:
            self.add_item(item)
            message.append("and place it in bag.")

        return " ".join(message)
