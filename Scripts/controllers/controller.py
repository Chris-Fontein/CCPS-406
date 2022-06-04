'''Contains base Controller class.'''

#Imports
#Python imports
#Third party imports
#Local imports

class Controller():
    '''Controller class.'''
    def __init__(self):
        self._character = None

    def set_character(self, character):
        '''Sets the Character this Controller will manage'''
        self._character = character

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        print(self._character.get_name() + " does nothing")

    def search(self, identifiers):
        '''Search Room Character is in for asset matching identifiers'''
        return self._character.search(identifiers)
