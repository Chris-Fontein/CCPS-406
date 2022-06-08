'''Contains base Character class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset

class Character(Asset):
    '''Character class.'''

    #stat keys
    ARMOR = "armor"
    ATTACK = "attack"
    MAX_HEALTH = "health"
    WEIGHT_LIMIT = "weight"

    #damgage message keys
    KILL = "kill"
    DAMAGE = "damage"
    NO_DAMAGE = "no_damage"

    def __init__(self, name, description, base_stats, current_health):
        super().__init__(name, description)

        self._weight = 0
        self._base_stats = base_stats
        self._stat_modifiers = {
            Character.ARMOR:0,
            Character.ATTACK:0,
            Character.MAX_HEALTH:0,
            Character.WEIGHT_LIMIT:0,
        }
        self._current_health = current_health

        self._effects = []
        self._inventory = []
        self._controller = None

        self._room = None
        self._rooms_visited = set()

        self._damage_messages = {
            Character.KILL: "and hit dealing {1} damage, killing them.",
            Character.DAMAGE: "and hit dealing {1} damage.",
            Character.NO_DAMAGE: "but {1} are unable to penetrate {2} armor."
            }

    def get_name(self):
        '''Returns the name of the Character'''
        return self._name

    def get_current_health(self):
        '''Returns current health'''
        return self._current_health

    def get_base_stats(self):
        '''Returns current base stats'''
        return self._base_stats

    def get_room(self):
        '''Returns the room the Character is in'''
        return self._room

    def set_room(self, room):
        '''Sets the room the Character is currently located in.'''
        self._room = room
        room.add_character(self)

    def get_valid_connections(self):
        '''Returns the directions and rooms a Character can go'''
        return {}

    def set_controller(self, controller):
        '''Set a new Controller for the Character'''
        if self._controller:
            self._controller.set_character = None
        self._controller = controller
        self._controller.set_character(self)

    def add_item(self, item):
        '''Add item to Character inventory'''
        self.adjust_weight(item.get_weight())
        self._inventory.append(item)

    def remove_item(self, item):
        '''Remove item to Character inventory'''
        self.adjust_weight(-item.get_weight())
        self._inventory.remove(item)

    def adjust_weight(self, adjustment):
        '''Adjust the character's weight load by the specified amount.'''
        self._weight += adjustment

    def search(self, identifiers):
        '''Pass identifying keys to the room and returns the Asset found'''
        return self._room.search(identifiers)

    def move(self, room):
        '''Move to a new room'''
        current_room = self._room
        room.add_character(self)
        current_room.remove_character(self)
        self._room = room

    def attack(self, character):
        '''Attack the target Character'''
        attack = (self._base_stats[Character.ATTACK]
                  + self._stat_modifiers[Character.ATTACK]
                )
        character.attacked(attack)

    def attacked(self, attack_value):
        '''Receive damage from an attack'''
        armor = self._base_stats[Character.ARMOR] + self._stat_modifiers[Character.ARMOR]
        damage = max(attack_value - armor, 0)
        self.modify_health(-damage)
        return damage

    def modify_health(self, value):
        '''Adjust health of Character'''
        health = self._current_health + value
        health = max(health, 0)
        health = min(health, self._base_stats[Character.MAX_HEALTH])
        self._current_health = health

    def action(self):
        '''Gets the controller to select the next action'''
        self._controller.action()
