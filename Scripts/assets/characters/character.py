'''Contains base Character class.'''

#Imports
#Python imports
#Third party imports
#Local imports
from assets.asset import Asset
from assets.room import Room
from assets.items.container import Container

class Character(Asset):
    '''Character class.'''

    #stat keys
    ARMOR = "armor"
    ATTACK = "attack"
    MAX_HEALTH = "health"
    WEIGHT_LIMIT = "weight"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._weight = 0
        self._base_stats = kwargs.get("base_stats")
        #print(self._base_stats)
        self._stat_modifiers = {
            Character.ARMOR:0,
            Character.ATTACK:0,
            Character.MAX_HEALTH:0,
            Character.WEIGHT_LIMIT:0,
        }

        self._equipment = {}
        self._current_health = kwargs.get("current_health")

        self._effects = kwargs.get("effects")
        self._inventory = [] #kwargs.get("inventory")
        self._controller = None

        self._room = kwargs.get("room")
        self._rooms_visited = set(kwargs.get("rooms_visited", []))

    def get_name(self):
        '''Returns the name of the Character'''
        return self._name

    def get_inventory(self):
        '''Returns the inventory of the Character'''
        return self._inventory

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

    def get_controller(self):
        '''Returns the controller of the character'''
        return self._controller

    def get_visible_characters(self):
        '''Returns all visible Characters in the room excluding themselves'''
        return self._room.get_characters() - set([self])

    def get_valid_connections(self):
        '''Returns the directions and rooms a Character can go'''
        return {}

    def get_equipment(self):
        '''Returns the Characters equipment'''
        return self._equipment

    def get_contents(self, instance):
        '''Returns all items that are instances of the specified class'''
        items = []
        for item in self._inventory:
            if isinstance(item, instance):
                items.append(item)
            if isinstance(item, Container):
                items.extend(item.get_contents(instance))
        return items

    def has_visited(self):
        '''Checks if the current room has been visited'''
        if self._room in self._rooms_visited:
            return True
        self._rooms_visited.add(self._room)
        return False

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
        item_parent =  item.get_parent()
        item.set_parent(self)
        if item_parent:
            if isinstance(item_parent, Container):
                item_parent.remove_item_contents(item)
            if isinstance(item_parent, Room):
                item_parent.remove_item_from_floor(item)

    def remove_item(self, item):
        '''Remove item to Character inventory'''
        self.adjust_weight(-item.get_weight())
        self._inventory.remove(item)

    def pickup(self, item):
        '''Pick up the specified item if you can carry it'''
        weight = self._weight
        max_weight = (self._stat_modifiers[Character.WEIGHT_LIMIT]
                     + self._base_stats[Character.WEIGHT_LIMIT])

        if weight + item.get_weight() > max_weight:
            return False

        self.add_item(item)
        return True

    def drop_item(self, item, destination):
        self.remove_item(item)

        if isinstance(destination,  Room):
            destination.add_item_to_floor(item)
        else:
            destination.add_item_contents(item)

    def adjust_weight(self, adjustment):
        '''Adjust the character's weight load by the specified amount.'''
        self._weight += adjustment

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
        damage = character.attacked(attack, self)

        return damage

    def attacked(self, attack_value, attacker):
        '''Receive damage from an attack'''
        armor = self._base_stats[Character.ARMOR] + self._stat_modifiers[Character.ARMOR]
        damage = max(attack_value - armor, 0)
        self.modify_health(-damage)

        if self._current_health <= 0:
            body = Container(name = "%s's body" %self._name,
                                description = "%s's body. They were alive "
                                                "until recently" %self._name,
                                identifiers = ["body", self._name],
                                value = 0,
                                weight = 100
                                )
            for item in self._inventory:
                body.add_item_contents(item)
            for slot in self._equipment:
                item = self._equipment[slot]
                if item:
                    body.add_item_contents(item)

            self._room.add_item_to_floor(body)
            self._room.remove_character(self)

        self._controller.attacked(attacker, damage)
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

    def get_available_contents(self, instance):
        '''Gets all the contents the character can access'''
        items = self.get_contents(instance)
        items.extend(self._room.get_room_contents(instance))
        return items

    def equip(self, item):
        '''Unequips Equipment in slot and equips item.'''
        slot = item.get_slot()
        unequipped = None

        if slot not in self._equipment:
            return False, unequipped

        #Slot is full
        unequipped = self.unequip(slot)

        self._equipment[slot] = item
        item_stats = item.get_stats()

        for stat in item_stats:
            self._stat_modifiers[stat] += item_stats[stat]

        if item.get_parent():
            self._inventory.remove(item)
        else:
            item.set_parent(self)
            self.adjust_weight(item.get_weight())

        return True, unequipped

    def unequip(self, slot):
        '''Unequips the Equipent in the specified slot placing it in inventory.'''
        if not self._equipment[slot]:
            return None

        item = self._equipment[slot]
        self._equipment[slot] = None

        item_stats = item.get_stats()
        for stat in item_stats:
            self._stat_modifiers[stat] -= item_stats[stat]

        self._inventory.append(item)

        return item
