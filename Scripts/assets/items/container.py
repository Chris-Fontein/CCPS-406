'''Contains Consumable item class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.item import Item

class Container(Item):
    '''Container class'''
    def __init__(self, name, description, value, weight):
        super().__init__(name, description, value, weight)

        self._content = []
        self._open = True
        self._closed_desc = ""
        self._empty_desc = ""
        self._placement = ""
        self._content_desc = ""

    def __eq__(self, other):
        return super().__eq__(other)
    
    def get_value(self):
        '''Returns the value of the container plus the values of all items inside'''
        total_value = self._value
        for item in self._content:
            total_value += item.get_value()
        return total_value
    
    def get_weight(self):
        '''Returns the weight of the container plus the weight of all items inside'''
        total_weight = self._weight
        for item in self._content:
            total_weight += item.get_weight()
        return total_weight

    def add_item_contents(self, new_item):
        '''Adds item to the container's contents'''
        self._content.append(new_item)
    
    def remove_item_contents(self, target_item):
        '''Removes target item from the container's contents'''
        self._content.remove(target_item)
    
    def get_furniture_description(self):
        '''Returns the description of the container along with the placement of the container
        inside the room. To be implemented in a room's long description.'''
        return self._description + " " + self._placement
    
    def get_container_description(self):
        '''Returns the description of the container along with the descriptions of
        individual items inside if the container is open. To be used when the player looks
        at the specific container'''
        if not(self._open):
            look_desc = self._closed_desc + ". "
        else:
            if len(self._content) == 0:
                look_desc = self._empty_desc + ". "
            elif len(self._content) == 1:
                look_desc = self._description + ". " + self._content_desc + self._content[0].get_description() + ". "
            else:
                look_desc = self._description + ". " + self._content_desc
                for item in range(len(self._content)):
                    if item != len(self._content) - 1:
                        look_desc = look_desc + self._content[item].get_description() + ", "
                    else:
                        look_desc = look_desc + "and " + self._content[item].get_description() + ". "
        return look_desc
    
