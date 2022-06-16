'''Contains base class for all game assets.'''

#Imports
#Python imports
#Third party imports
#Local imports

class Asset:
    '''Base class for all game assets.'''
    def __init__(self, **kwargs):
        self._name = kwargs.get("name")
        self._description = kwargs.get("description")
        self._identifiers = set(kwargs.get("identifiers"))

    def __str__(self):
        return "".join([self._name, ":", self.get_description()])
    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__
                    and self._identifiers == other._identifiers
                )
    def __ne__(self, other):
        return not self.__eq__(other)

    def get_name(self):
        '''Returns asset's name'''
        return self._name

    def get_identifiers(self):
        '''Returns Assets identifiers'''
        return self._identifiers

    def get_description(self):
        '''Returns asset's description.'''
        return self._description

    def get_long_description(self):
        '''Returns asset's description.'''
        return self._description

    def match_identifiers(self, identifiers):
        '''Returns the number of identifiers that match the identifiers being searched'''
        return len(self._identifiers & identifiers)
