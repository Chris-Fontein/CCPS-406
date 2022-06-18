'''Controller class base Adventurer AI.'''

#Imports
#Python imports
import random
#Third party imports
#Local imports
from assets.asset import Asset
from assets.item import Item
from assets.items.equipment import Equipment
from controllers.aiController import AiController

class AdventurerController(AiController):
    '''Adventurer Controller class.'''

    def action(self):
        '''Perform the characters actions based the Characters surrounding'''
        if self._character.get_current_health() <= 0:
            return

        actions = [self.move]

        targets = self._character.get_visible_characters()
        if targets:
            actions.append(self.attack)
        contents = self._character.get_available_contents(Item, False)
        if contents:
            actions.extend([self.look, self.pickup])

        equipment = self._character.get_inventory(Equipment)
        if equipment:
            actions.append(self.equip)

        random.choice(actions)()


    def look(self):
        '''Look at a random item in the room.'''
        contents = self._character.get_available_contents(Item, False)
        item = random.choice(list(contents))
        self.message("%s looks at %s" %(self._character.get_name(), item.get_name()))
        self._character.set_last_action("They are looking at a %s" % item.get_name())

    def pickup(self):
        '''Pick up a random item in the room.'''
        contents = self._character.get_available_contents(Item, False)
        item = random.choice(list(contents))

        result = self._character.pickup(item)
        if result:
            self._character.set_last_action("They picked up %s" % item.get_name())
            self.message("%s picked up a %s and put it in their inventory" %(
                                                                    self._character.get_name(),
                                                                    item.get_name()
                                                                    ))
        else:
            self._character.set_last_action("They tried to pick up %s but, "
                                                "couldn't" % item.get_name())
            self.message("%s tried to pick up %s but couldn't" %(self._character.get_name(),
                                                                        item.get_name()
                                                                        ))

    def equip(self):
        '''Equip a random item from inventory.'''
        equipment = self._character.get_inventory(Equipment)
        item = random.choice(list(equipment))

        result, unequipped = self._character.equip(item)

        if not result:
            self.message("%s tried to equip %s but, couldn't" %(self._character.get_name(),
                                                                item.get_name(),
                                                                ))
            self._character.set_last_action("They tried to equip %s but, couldn't" %item.get_name())
        if unequipped:
            self.message("%s removed %s and equipped %s" %(self._character.get_name(),
                                                            unequipped.get_name(),
                                                            item.get_name()
                                                            ))
            self._character.set_last_action("They removed %s and equipped %s" %(
                                                                    unequipped.get_name(),
                                                                    item.get_name(),
                                                                    ))
        else:
            self.message("%s equipped %s" %(self._character.get_name(), item.get_name()))
            self._character.set_last_action("They equipped %s" %item.get_name())
