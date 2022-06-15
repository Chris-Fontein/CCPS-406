'''Contains generic Equipment class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.item import Item

class Equipment(Item):
    '''Generic item class.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._slot = kwargs.get("slot")
        self._stats = kwargs.get("equipValue")

    def get_stats(self):
        """Returns Equipments's stat modifications."""
        return self._stats

    def get_slot(self):
        """Returns Equipments's stat modifications."""
        return self._slot
