"""
Dank Dungeon - Tommy Bough

Create a small game world to build off of in the midterm.
"""

from copy import copy
from copy import deepcopy
import os 
import platform
from utilities import *

class Item:
    """
    Represents an item that mobs drop and players may acquire.
    
    Attributes:
        name (str): The name of the item.
        current_room: Where the item is located.
        
    Methods:
        use: Ability to use the item.
    """
    def __init__ (self, name, damage):
        self.name = name
        self.damage = damage

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
    def __init__ (self, name):
        self.name = name

    def activate(self):
        pass

class Room:
    """
    Class representing the idea of a room in our world.

    Attributes: 
        name (str): The name of the room.
        nearby_rooms (list of rooms): A list of the connected rooms.

    Methods:
        connect_room: Helper method to connect a room to an existing room.
        connect_rooms: Helper method to connect a list of rooms to an existing room.
        open: Allows the rooms to open.
    """
    def __init__(self, name: str):
        self.name = name
        self.connected_rooms = []
        self.items = []
        self.objects = []
        self.opponents = []
    
    def connect_room(self, room_to_connect: Room):
        """Connects a room."""
        self.connected_rooms.append(room_to_connect)
    
    def connect_rooms(self, rooms_to_connect: Room):
        """Connects a list of rooms."""
        self.connected_rooms += rooms_to_connect
    
    def __repr__(self):
        return self.name

class Opponent:
    """
    Represents a low-level enemy
    
    Attributes:
        name (str): The name of the enemy.
        health (int): How much health the enemy has.
        
    Methods:
        attack: Allows the enemy to attack the player.
        stun: Stuns the enemy when attacked.
        perish: Kills the enemy when health = 0.
    """
    def __init__ (self, name, health, current_room: Room):
        self.name = name
        self.health = health
        self.current_room = current_room

class Player:
    """Represents the player.
    
    Attributes:
        name (str): The name of the player.
        inventory (list): What the player is holding.
        equipped_item (item): The equipped item from the players inventory.
        current_room (room): The room the player is currently in.
        health (int): How much health the player has.
        
    Methods:
        inventory: Allows the player to see their inventory.
        equip: Selects an item from their inventory.
        use_equipped: Uses the equiped item.
        move: Allows the player to move from one room to another.
        grab: Gives the player the ability to grab an item.
        perish: Kills the player when health = 0.
        attack: Allows the player to damage combatants.
        respawn: Allows the player to respawn when they perish.
        block: Allows the player to block with certain items.
    """
    def __init__(self, name, health, current_room: Room):
            self.name = name
            self.health = health
            self.current_room = current_room
            self.player_inventory = []
            self.active_item = None
            self.first_time = True

    def action(self):
        # for item in self.equipped_items:
        #     if item.special_ability:
        #         item.special_ability()
        if self.first_time:
            message = "You have breached the alien ship. You must destroy their king before everything you know succumbs to him.\nPress 'T' to travel, 'I' to see your inventory, 'E' to equip an item.\n"
            self.first_time = False
        else:
            message = "T/I/E? "
        
        # TODO look into clearing console.
        user_input = input(message)
        if user_input.lower() == "i":
            self.inventory()
        if user_input.lower() == "t":
            self.move()
        if user_input.lower() == "e":
            self.equip()

    def inventory(self):
        """Lets the player see their inventory."""
        print(f"Your inventory contains:")
        for item in self.player_inventory:
            print(f"\t{item.name}")

    def equip(self):
        """Sets active item for player."""
        print(f"Your inventory contains:")
        for item in self.player_inventory:
            print(f"\t{item.name}")

            user_equip = input("Which item do you wish to equip?\n")
            if user_equip.lower() == item.name.lower():
                self.active_item = user_equip
                print(f"You have equipped the {item.name}.")
                return
        print("Invalid Choice.")
    
    def move(self):
        """
        Offers the player a list of connected rooms to choose from, moves the player if the player selects an option.
        """
        print(f"You are located in the {self.current_room.name}. You can travel to the:")
        for room in self.current_room.connected_rooms:
            print(f"\t{room.name}")
    
        # Collects the user's choice and compare to the options. Move user if there's a match.
        user_choice = input("Where do you choose to travel?\n")
        for room in self.current_room.connected_rooms:
            # Ignores capitalization
            # if user_choice.lower() != room.name.lower():
            #     # Only occurs if a successful move has not been made.
            #     print("Invalid choice. Try again.")
            if user_choice.lower() == room.name.lower():
                self.current_room = room
                os.system("cls")
                print(f"You have arrived in the {self.current_room.name}.")
                for item in self.current_room.items:
                    for opponent in self.current_room.opponents:
                        if opponent in self.current_room.opponents:
                            print(f"You come across the {opponent.name}.")
                    print(f"You have found the {room_list(self.current_room.items)}.")
                    grab_input = input(f"Do you wish to obtain it? Yes or No.\n")
                    if grab_input.lower() == "yes":
                        bob.player_inventory.append(item)
                        self.current_room.items.remove(item)
                        print(f"You have obtained the {item.name}.")
                    elif grab_input.lower() == "no":
                        print(f"You leave the {item.name}.")
                    else:
                        print("Invalid Choice. Try again.")
                for object in self.current_room.objects:
                    if object in self.current_room.objects:
                        print(f"You have found a {room_objects(self.current_room.objects)}.")
                return None
            
        print("Invalid room choice. Try again.")

    def use_active_item(self):
        """Calls the active item's use method."""
        self.active_item.use()

    def attack(self):
        for opponent in self.current_room.opponents:
            if opponent in self.current_room.opponents > 0:
                attack_input = input(print(f"Do you wish to attack the {opponent.name}?\n"))
                if attack_input.lower == "yes":
                    int(opponent.health - self.active_item.damage)
                if attack_input.lower == "no":
                    print(f"You do not attack the {opponent.name}.")
                

    def perish(self):
        pass

    def respawn(self):
        pass

    def block(self):
        pass

breach = Room("The Breach")
hall_of_souls = Room("Hall of Souls")
chamber_of_light = Room("Chamber of Light")
chamber_of_darkness = Room("Chamber of Darkness")
portal = Room("The Portal")
gate_room = Room("Main Cell")
brother_light_chamber = Room("Cell of Light")
brother_darkness_chamber = Room("Cell of Darkness")
passageway = Room("Passageway")

breach.connect_room(hall_of_souls)
hall_of_souls.connect_rooms([chamber_of_light, chamber_of_darkness, portal])
chamber_of_light.connect_room(hall_of_souls)
chamber_of_darkness.connect_room(hall_of_souls)
portal.connect_room(gate_room)
gate_room.connect_rooms([brother_light_chamber, brother_darkness_chamber])
brother_light_chamber.connect_room(gate_room)
brother_darkness_chamber.connect_room(gate_room)

brother_of_light = Opponent("Brother of Light", 75, brother_light_chamber)
brother_of_darkness = Opponent("Brother of Darkness", 75, brother_darkness_chamber)

bob = Player("Player", 100, breach)

bob.player_inventory.append(Item("Dagger", 10))

orb_of_light = Item("Orb of Light", 0)
orb_of_darkness = Item("Orb of Darkness", 0)
sword_of_light = Item("Sword of Light", 100)
sword_of_darkness = Item("Sword of Darkness", 100)

orb_conduit = Object("Orbicular Conduit")

chamber_of_light.items.append(orb_of_light)
chamber_of_darkness.items.append(orb_of_darkness)
brother_darkness_chamber.items.append(sword_of_darkness)
brother_light_chamber.items.append(sword_of_light)

hall_of_souls.objects.append(orb_conduit)

brother_light_chamber.opponents.append(brother_of_light)
brother_darkness_chamber.opponents.append(brother_of_darkness)

while True:
    bob.action()