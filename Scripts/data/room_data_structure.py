from dataclasses import dataclass
from data.container_data_structure import Container
from data.equip_data_structure import Equipment

@dataclass
class RoomClass:
    name: str
    description: str
    identifiers: list
    characters: list[str]
    floor:list[str]
    furniture: list[str]
    connections: list[[]]
    monster_connections:list[[]]

    def __init__(self,name: str, description: str,identifiers: list,characters: list[str], floor:list[str],furniture: list[str], connections: list[[]], monster_connections:list[[]] ):
        self.name = name
        self.description = description
        self.identifiers = identifiers
        self.characters = characters
        self.floor = floor
        self.furniture = furniture
        self.connections = connections
        self.monster_connections = monster_connections