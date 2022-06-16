import os
import os.path
import pprint
import yaml
from data.room_data_structure import RoomClass

#check if the file to save has been created
working_direcotry = os.path.abspath(os.getcwd())
cfile_exists = os.path.isfile(working_direcotry+"\data\text_files\saved_characters.yml")
ifile_exists = os.path.isfile(working_direcotry+"\data\text_files\saved_items.yml")
rfile_exists = os.path.isfile(working_direcotry+"\data\text_files\saved_rooms.yml")

class Data:
    def __init__(self):
        super().__init__()

    def read_yaml(self,file_name):
        """ A function to read YAML file"""
        with open(f"data/text_files/{file_name}.yml") as file:
            # config = yaml.safe_load(f)
            data_list = yaml.safe_load(file)
            # print(roomsList)
        return data_list  # config

    #save the file
    def write_yaml(self, data, file_name):
        """ A function to write YAML file"""
        #serialize a Python dictionary and store it into a YAML formatted file
        with open(f'data/text_files/{file_name}.yml', 'w') as file:
            yaml.dump(data, file)

    #load the text data file
    def load(self):
        characters_data=[]
        items_data=[]
        rooms_data=[]

        #print(os.path.dirname(os.path.abspath(__file__)))
        #print(os.path.abspath(os.getcwd()))

        if cfile_exists:
            characters_data=self.read_yaml('saved_characters')
        else:
            characters_data=self.read_yaml('characters')
            self.write_yaml(characters_data, 'saved_characters')

        if ifile_exists:
            items_data=self.read_yaml('saved_items')
        else:
            items_data=self.read_yaml('items')
            self.write_yaml(items_data, 'saved_items')

        if rfile_exists:
            rooms_data=self.read_yaml('saved_rooms')
        else:
            rooms_data=self.read_yaml('rooms')
            self.write_yaml(rooms_data, 'saved_rooms')

        return characters_data, items_data, rooms_data


    def data_mapping(self, room_data_list):
        rooms_list = []
        rooms_dict= {}
        room_keys = list(room_data_list.keys())
        for r_key in room_keys:
            room_obj=RoomClass(room_data_list[r_key]['name'],
                      room_data_list[r_key]['description'],
                      room_data_list[r_key]['identifiers'],
                      room_data_list[r_key]['characters'],
                      room_data_list[r_key]['floor'],
                      room_data_list[r_key]['furniture'],
                      room_data_list[r_key]['connections'],
                      room_data_list[r_key]['monster_connections'])
            rooms_list.append(room_obj)
            rooms_dict[r_key]=room_obj

        rooms_list[0].name = "Start"
        rooms_dict[list(room_data_list.keys())[0]].name= "Start"

        with open(r'./data/text_files/saved_rooms.yml','w') as file:
            document=yaml.dump(rooms_dict, file)

        return rooms_list