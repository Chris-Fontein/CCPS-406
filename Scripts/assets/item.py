'''Contains generic item class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Item(Asset):
    '''Generic item class.'''
    def __init__(self, name, description, identifiers, value, weight):
        super().__init__(name, description, identifiers)
        self._value = value
        self._weight = weight

    def get_value(self):
        """Returns item's value."""
        return self._value

    def get_weight(self):
        """Returns item's weight."""
        return self._weight
