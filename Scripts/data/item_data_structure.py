from dataclasses import dataclass

@dataclass
class Item:
    name: str
    description: str
    identifiers: list[str]
    value: int
    weight: int