'''Contains generic item class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Item(Asset):
    '''Generic item class.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._value = kwargs.get("value")
        self._weight = kwargs.get("weight")
        self._parent = None

    def get_value(self):
        """Returns item's value."""
        return self._value

    def get_weight(self):
        """Returns item's weight."""
        return self._weight

    def get_parent(self):
        """Returns the containing asset."""
        return self._parent

    def set_parent(self, parent):
        """Set the Asset that contains this item"""
        self._parent = parent
