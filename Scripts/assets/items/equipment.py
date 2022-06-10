'''Contains generic Equipment class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.item import Item

class Equipment(Item):
    '''Generic item class.'''
    def __init__(self, name, description, identifiers, value, weight, slot, stats):
        super().__init__(name, description, identifiers, value, weight)
        self._slot = slot
        self._stats = stats

    def get_stats(self):
        """Returns Equipments's stat modifications."""
        return self._stats

    def get_slot(self):
        """Returns Equipments's stat modifications."""
        return self._slot
