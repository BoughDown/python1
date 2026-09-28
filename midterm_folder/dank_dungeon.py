"""
Dank Dungeon - Tommy Bough

Create a small game world to build off of in the midterm.
"""

from copy import copy
from copy import deepcopy

class Item:
    """
    Represents an item that mobs drop and players may acquire.
    
    Attributes:
        name (str): The name of the item.
        current_room: Where the item is located.
        
    Methods:
        use: Ability to use the item.
    """
    def __init__ (self, name, current_room):
        self.name = name
        self.current_room = current_room

    def use(self):
        print(f"You use the {self.name}")

class Object:
    """
    An object in rooms the player could interact with.

    Attributes:
        name (str): The name of the object.
        current_room: Where the object is located.

    Methods:
        activate: Allows the object to activate.
    """

class Room:
    """
    Class representing the idea of a room in our world.

    Attributes: 
        name (str): The name of the room.
        nearby_rooms (list of rooms): A list of the connected rooms.


    Methods:
        connect_room: Helper method to connect a room to an existing room.
        connect_rooms: Helper method to connect a list of rooms to an existing room.
    """
    def __init__(self, name: str):
        self.name = name
        self.connected_rooms = []
    
    def connect_room(self, room_to_connect: Room):
        """Connects a room."""
        self.connected_rooms.append(room_to_connect)
    
    def connect_rooms(self, rooms_to_connect: Room):
        """Connects a list of rooms."""
        self.connected_rooms += rooms_to_connect
    
    def __repr__(self):
        return self.name

class Player:
    """Represents the player.
    
    Attributes:
        name (str): The name of the player.
        inventory (list): What the player is holding.
        equipped_item (item): The equipped item from the players inventory.
        current_room (room): The room the player is currently in.
        health (int): How much health the player has.
        
    Methods:
        equip: Selects an item from their inventory.
        use_equipped: Uses the equiped item.
        move: Allows the player to move from one room to another.
        perish: Kills the player when health = 0.
        attack: Allows the player to damage combatants.
        respawn: Allows the player to respawn when they perish.
        block: Allows the player to block with certain items.
    """
    def __init__(self, name, health, current_room: Room):
            self.name = name
            self.health = health
            self.current_room = current_room
            self.inventory = []
            self.active_item = Item("Dagger")

    def action(self):

        # for item in self.equipped_items:
        #     if item.special_ability:
        #         item.special_ability()

        user_input = input("Move or equip?\n")
        if user_input.lower() == "equip":
            self.equip()
        if user_input.lower() == "move":
            self.move()

    def equip(self):
        """Sets the active item."""
        print(f"Your inventory contains:")
        for item in self.inventory:
            print(f"\t{item.name}")
        # Collects user input. If user_input matches an item's name in the inventory, make that the active item.
        user_input = ""
        equipped = False
        while not equipped:
            user_input = input("Which item do you choose to equip?\n")
            for item in self.inventory:
                if user_input.lower() == item.name.lower():
                    self.active_item = item
                    equipped = True
                    break
    
    def move(self):
        """
        Offers the player a list of connected rooms to choose from, moves the player if the player selects an option.
        """
        print(f"You have arrived in the {self.current_room.name}. You can travel to the:")
        for room in self.current_room.connected_rooms:
            print(f"\t{room.name}")
    
        # Collects the user's choice and compare to the options. Move user if there's a match.
        user_choice = input("Where do you choose to travel?\n")
        for room in self.current_room.connected_rooms:
            # Ignores capitalization
            if user_choice.lower() == room.name.lower():
                self.current_room = room
                # Quitting the function if a successful move has been made.
                return None
        # Only occurs if a successful move has not been made.
        print("Invalid choice. Try again.")

    def use_active_item(self):
        """Calls the active item's use method."""
        self.active_item.use()

    def attack(self):
        pass

class Minor:
    """
    Represents a low-level enemy
    
    Attributes:
        name (str): The name of the minor enemy.
        health (int): How much health the minor enemy has.
        
    Methods:
        attack: Allows the minor enemy to attack the player.
        stun: Stuns the minor enemy when attacked.
        perish: Kills the minor enemy when health = 0.
    """
    def __init__ (self, name, health, current_room: Room):
        self.name = name
        self.health = health
        self.current_room = current_room

hall_of_souls = Room("Hall of Souls")
chamber_of_light = Room("Chamber of Light")
chamber_of_darkness = Room("Chamber of Darkness")
portal = Room("The Portal")
gate_room = Room("Main Cell")
brother_light_chamber = Room("Cell of Light")
brother_darkness_chamber = Room("Cell of Darkness")
passageway = Room("Passageway")

hall_of_souls.connect_rooms([chamber_of_light, chamber_of_darkness, portal])
chamber_of_light.connect_room(hall_of_souls)
chamber_of_darkness.connect_room(hall_of_souls)
portal.connect_room(gate_room)
gate_room.connect_rooms([brother_light_chamber, brother_darkness_chamber, passageway])
brother_light_chamber.connect_room(gate_room)
brother_darkness_chamber.connect_room(gate_room)

bob = Player("Player", 100, hall_of_souls)

bob.inventory.append(Item("Dagger"))

orb_of_light = Item("Orb of Light", chamber_of_light)
orb_of_darkness = Item("Orb of Darkness", chamber_of_darkness)

while True:
    bob.action()