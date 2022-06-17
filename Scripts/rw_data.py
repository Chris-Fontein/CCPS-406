''' data connections : read/write textual data files'''

import os
import os.path
#import pprint
import yaml

#check if the file to save has been created
working_direcotry = os.path.abspath(os.getcwd())
cfile_exists = os.path.isfile(working_direcotry+"\\data\\saved_characters.yml")
ifile_exists = os.path.isfile(working_direcotry+"\\data\\saved_items.yml")
rfile_exists = os.path.isfile(working_direcotry+"\\data\\saved_rooms.yml")

class Data:
    """ Read/Write textual data files """
    def __init__(self):
        super().__init__()

    def read_yaml(self,file_name):
        """ A function to read YAML file"""
        with open(f"Data/{file_name}.yml") as file:
            data_list = yaml.safe_load(file)
        return data_list

    #save the file
    def write_yaml(self, data, file_name):
        """ A function to write YAML file"""
        #serialize a Python dictionary and store it into a YAML formatted file
        with open(f'Data/{file_name}.yml', 'w') as file:
            yaml.dump(data, file)

    #load the text data file
    def load(self):
        """This method reads yaml files and returns them for the system.

        Returns:
            dictionary: characters
            dictionary: items
            dictionary: rooms
        """
        characters_data=[]
        items_data=[]
        rooms_data=[]

        #print(os.path.dirname(os.path.abspath(__file__)))
        #print(os.path.abspath(os.getcwd()))

        if cfile_exists:
            characters_data=self.read_yaml('saved_characters')
        else:
            characters_data=self.read_yaml('characters')
            #self.write_yaml(characters_data, 'saved_characters')

        if ifile_exists:
            items_data=self.read_yaml('saved_items')
        else:
            items_data=self.read_yaml('items')
            #self.write_yaml(items_data, 'saved_items')

        if rfile_exists:
            rooms_data=self.read_yaml('saved_rooms')
        else:
            rooms_data=self.read_yaml('rooms')
            #self.write_yaml(rooms_data, 'saved_rooms')

        return characters_data, items_data, rooms_data
