'''Controller class used to interact with the player.'''

#Imports
#Python imports
#Third party imports
#Local imports
from controllers.controller import Controller

class PlayerController(Controller):
    '''Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        valid_action = False
        while(not valid_action):
            command = input("> ")
            print(command)
            if command == "exit":
                valid_action = True

    def parse_command(self, command):
        