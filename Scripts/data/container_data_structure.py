from dataclasses import dataclass

@dataclass
class Container:
    name: str
    description: str
    identifiers: list[str]
    value: int
    weight: int
    placement: str
    content: list[str]
    contents_description: str
    empty_description: str

    def __init__(self, name: str, description: str,  identifiers: list[str], value: int, weight: int,  placement: str, content: list[str],  contents_description: str, empty_description: str):
        self.name = name
        self.description = description
        self.identifiers = identifiers
        self.value = value
        self.weight = weight
        self.placement = placement
        self.content = content
        self.contents_description = contents_description
        self.empty_description = empty_description