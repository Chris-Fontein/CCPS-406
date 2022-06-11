'''Contains room class.'''

#Imports
#Python imports
#Third party imports
#Local imports
#from controllers.playerController import PlayerController
from assets.asset import Asset

class Room(Asset):
    '''Room class.'''
    def __init__(self, name, description):
        super().__init__(name, description, set())

        self._floor = []
        self._furniture = []
        self._characters = set()
        self._connections = {}
        self._monster_connections = {}

    def get_description(self):
        """Returns room's short description."""
        short_desc = "".join(["[", self._name, "]"])
        return " ".join([short_desc, self.build_character_names()])

    def get_long_description(self):
        """Returns room's long description."""
        short_desc = "".join(["[", self._name, "]"])

        return " ".join([short_desc, self._description, self.build_character_description(), self.build_furniture_description(), self.build_item_description()])

    def get_connections(self):
        '''return the connections any Character can take'''
        return self._connections

    def get_monster_connections(self):
        '''return the connections the Monster can take'''
        return self._monster_connections

    def add_character(self, character):
        self._characters.add(character)

    def remove_character(self, character):
        self._characters.remove(character)

    def add_item_to_floor(self, new_item):
        '''Adds the specified item to the floor list.'''
        self._floor.append(new_item)

    def remove_item_from_floor(self, target_item):
        '''Removes the specified item to the floor list.'''
        self._floor.remove(target_item)

    def add_funiture(self, furniture):
        '''
        Adds the specified item to the furniture list.
        Furniture cannot be removed.  This function should only be used during level creation.
        '''
        self._furniture.append(furniture)

    def add_room_connection(self, direction, room, monster_connection = False):
        ''' Adds connection to the specified room.
        Monster connections can only be navigated by the monster while regular connections
        can be navigated by all Characters.
        This function should only be used during level creation.
        '''
        #connections = monster_connection if self._monster_connections else self._connections
        if monster_connection:
            connections = self._monster_connections
        else:
            connections = self._connections

        connections[direction] = room

    def build_item_description(self):
        '''Synthesizes various descriptions of items on the floor into one description.
        To be used for the long description of a room.'''
        items_on_floor = self._floor
        if len(items_on_floor) == 1:
            add_item_desc = "\n" + "On the floor, you notice " + items_on_floor[0].get_description() + ". "
        elif len(items_on_floor) > 1:
            add_item_desc = "\n" + "On the floor, you notice "
            for item in range(len(items_on_floor)):
                if item != len(items_on_floor)-1:
                    add_item_desc = add_item_desc + items_on_floor[item].get_description() + ", "
                else:
                    add_item_desc = add_item_desc + "and " + items_on_floor[item].get_description() + ". "
        else:
            add_item_desc = ""
        return add_item_desc

    def build_character_description(self):
        '''Synthesizes various descriptions of characters in a room into one description.
        To be used for the long and the short description of a room.'''
        others_in_room = list(self._characters)
        for person in others_in_room:
            if isinstance(person._controller, PlayerController):
                others_in_room.remove(person)
        if len(others_in_room) == 1:
            add_char_desc = "\n" + "Inside, you see " + others_in_room[0].get_description() + ". "
        elif len(others_in_room) > 1:
            add_char_desc = "\n" + "Inside, you see "
            for other in range(len(others_in_room)):
                if other != len(others_in_room)-1:
                    add_char_desc = add_char_desc + others_in_room[other].get_description() + ", "
                else:
                    add_char_desc = add_char_desc + "and " + others_in_room[other].get_description() + ". "
        else:
            add_char_desc = ""
        return add_char_desc

    def build_character_names(self):
        '''Synthesizes various descriptions of characters in a room into one description.
        To be used for the long and the short description of a room.'''
        others_in_room = list(self._characters)
        for person in others_in_room:
            if isinstance(person._controller, PlayerController):
                others_in_room.remove(person)
        if len(others_in_room) == 1:
            add_char_desc = "\n" + "Inside, you see " + others_in_room[0].get_name() + ". "
        elif len(others_in_room) > 1:
            add_char_desc = "\n" + "Inside, you see "
            for other in range(len(others_in_room)):
                if other != len(others_in_room)-1:
                    add_char_desc = add_char_desc + others_in_room[other].get_name() + ", "
                else:
                    add_char_desc = add_char_desc + "and " + others_in_room[other].get_name() + ". "
        else:
            add_char_desc = ""
        return add_char_desc

    def build_furniture_description(self):
        '''Synthesizes various descriptions of the furniture and their locations in a room into one description.
        To be used for the long of a room.'''
        furnishings = self._furniture
        if len(furnishings) == 1:
            add_furn_desc = "\n" + "There is " + furnishings[0].get_furniture_description() + ". "
        elif len(furnishings) > 1:
            add_furn_desc = "\n" + "There is "
            for furniture in range(len(furnishings)):
                if furniture != len(furnishings)-1:
                    add_furn_desc = add_furn_desc + furnishings[furniture].get_furniture_description() + ", "
                else:
                    add_furn_desc = add_furn_desc + "and " + furnishings[furniture].get_furniture_description() + ". "
        else:
            add_furn_desc = ""
        return add_furn_desc



