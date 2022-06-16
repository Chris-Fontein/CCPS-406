from dataclasses import dataclass


@dataclass
class Equipment:
    name: str
    description: str
    identifiers: list[str]
    value: int
    weight: int
    slot: str
    equipValue: {}

def __init__(self,name: str, description: str,identifiers: list, value: int, weight:int, slot:str, equipvalue: {}):
        self.name = name
        self.description = description
        self.identifiers = identifiers
        self.value = value
        self.weight = weight
        self.slot = slot
        self.equipvalue = equipvalue