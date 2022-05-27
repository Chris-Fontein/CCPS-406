'''Contains generic item class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Item(Asset):
    '''Generic item class.'''
    def __init__(self, name, description, value, weight):
        super().__init__(name, description)
        self._value = value
        self._weight = weight

    def __eq__(self, other):
        if super().__eq__(other):
            return (self._value == other._value
                    and self._weight == other._weight)
        return False

    def get_value(self):
        """Returns item's value."""
        return self._value

    def get_weight(self):
        """Returns item's weight."""
        return self._weight
