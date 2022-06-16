'''Contains Consumable item class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.items.container import Container
from assets.asset import Asset

class OpenableContainer(Container):
    '''Container class'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._open = kwargs.get("open")
        self._closed_desc = kwargs.get("closed_description")

    def get_container_description(self):
        '''Returns the description of the container along with the descriptions of
        individual items inside if the container is open. To be used when the player looks
        at the specific container'''
        if not self._open:
            return self._closed_desc + ". "

        return super().get_container_description()

    def get_contents(self, instance):
        '''Returns all items that are instances of the specified class'''
        if self._open:
            return super().get_contents(instance)
        return []
    def search_contents(self, identifiers, instance = Asset, min_match = 1):
        '''Searches the contents of the container for the best matches to the identifier'''
        if not self._open:
            return []
        return super().search_contents(identifiers, instance, min_match)
