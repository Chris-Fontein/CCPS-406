from dataclasses import dataclass
from data.equip_data_structure import Equipment

@dataclass
class Character:
    name: str
    description: str
    identifiers: list[str]
    current_health: int
    inventory: list[str]
    equipped:  list[str]
    effects: str
    rooms_visited: list