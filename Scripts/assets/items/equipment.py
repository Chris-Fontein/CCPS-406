'''Contains generic Equipment class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.item import Item

class Equipment(Item):
    '''Generic item class.'''
    def __init__(self, name, description, value, weight, slot, stats):
        super().__init__(name, description, value, weight)
        self._slot = slot
        self._stats = stats
    
    def __eq__(self, other):
        if super().__eq__(other):
            return (self._stats == other._stats
                    and self._slot == other._slot)
        return False

    def get_stats(self):
        """Returns Equipments's stat modifications."""
        return self._stats

    def get_slot(self):
        """Returns Equipments's stat modifications."""
        return self._slot
