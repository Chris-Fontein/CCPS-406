'''Contains base Controller class.'''

#Imports
#Python imports
#Third party imports
#Local imports
import helper_funcs

class Controller():
    '''Controller class.'''
    def __init__(self):
        self._character = None

    def set_character(self, character):
        '''Sets the Character this Controller will manage'''
        self._character = character

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        self.message(self._character.get_name() + " does nothing")

    def attacked(self, attacker, damage):
        '''Controller response to being attacked'''

    def message(self, text):
        '''Print messages with proper formatting'''
        helper_funcs.print_text(text)