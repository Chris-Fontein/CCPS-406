'''Contains base class for all game assets.'''

#Imports
#Python imports
#Third party imports
#Local imports

class Asset:
    '''Base class for all game assets.'''
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __str__(self):
        return self.get_description()

    def __eq__(self, other):
        return (self.__class__ == other.__class__
                    and self._name == other._name
                )
    def __ne__(self, other):
        return not self.__eq__(other)

    def get_name(self):
        """Returns asset's name"""
        return self._name

    def get_description(self):
        """Returns asset's description."""
        return self._description
