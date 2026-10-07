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
        self.deposited = []

# Allows the player to activate an object by depositing orbs.
    def activate(self, player):
        # Collect every orb the player is carrying
        orbs = []
        for item in player.player_inventory:
            if "Orb" in item.name:
                orbs.append(item)

# Object doesn't activate when no orbs are given to it.
        if len(orbs) == 0:
            print(f"The {self.name} fails to respond. You have nothing to give it.")
            return


        for orb in orbs:
            player.player_inventory.remove(orb)
            self.deposited.append(orb)
            print(f"You place the {orb.name} into the {self.name}.")

            # Don't keep  an orb equipped that's been deposited inside the conduit
            if player.active_item == orb:
                player.active_item = dagger

# Gives a different reaction based on how many orbs are given.
        if len(self.deposited) == 1:
            print(f"The {self.name} glows faintly.")
        elif len(self.deposited) == 2:
            print(f"The {self.name} sparks to life.")
            hall_of_souls.connect_room(portal)
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
        self.respawn_point = None

# Connects one room to another
    def connect_room(self, room_to_connect: Room):
        """Connects a room."""
        self.connected_rooms.append(room_to_connect)

# Connects one room to a list of rooms.
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
    def __init__ (self, name, health, damage, current_room: Room, weakness = None):
        self.name = name
        self.health = health
        self.damage = damage
        self.current_room = current_room
        self.weakness = weakness

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
# If it is the players first time running the program, it gives a short narration.
        if self.first_time:
            message = "You have breached the alien ship. You must destroy their king before everything you know succumbs to him.\nPress 'T' to travel, 'I' to see your inventory, 'E' to equip an item, 'A' to interact with objects, and 'B' to attack.\n"
            self.first_time = False
# On the programs 2nd or more attempt, the narration is not repeated.
        else:
            message = "T/I/E/A/B? "

# Gives the player various functions to work with.
        # TODO look into clearing console.
        user_input = input(message)
        if user_input.lower() == "i":
            self.inventory()
        if user_input.lower() == "t":
            self.move()
        if user_input.lower() == "e":
            self.equip()
        if user_input.lower() == "a":
            self.activate()
        if user_input.lower() == "b":
            self.attack()

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
        
        for item in self.player_inventory:
            if user_equip.lower() == item.name.lower():
                self.active_item = item
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
            # Ignores capitalization.
            if user_choice.lower() == room.name.lower():
                self.current_room = room
                # Clears terminal after the player moves to a new room.
                os.system("cls")
                print(f"You have arrived in the {self.current_room.name}.")
                # Tells the player they come across an opponent if they are in the room with one.
                for opponent in self.current_room.opponents:
                    print(f"You come across the {opponent.name}.")

                # Tells the player if they come across an item.
                for item in self.current_room.items[:]:
                    print(f"You have found the {item.name}.")
                    grab_input = input("Do you wish to obtain it? Yes or No.\n")
                    if grab_input.lower() == "yes":
                        self.player_inventory.append(item)
                        self.current_room.items.remove(item)
                        print(f"You have obtained the {item.name}.")
                    elif grab_input.lower() == "no":
                        print(f"You leave the {item.name}.")
                    else:
                        print("Invalid Choice. Try again.")

                # Tells the player if they come across an object.
                for object in self.current_room.objects:
                    print(f"You have found the {object.name}.")
                return None
            
        print("Invalid room choice. Try again.")

    def use_active_item(self):
        """Calls the active item's use method."""
        self.active_item.use()

    def attack(self):
        """Allows the player to attack opponents if they have an equipped item."""
        if self.active_item is None:
            print("You have nothing equipped.")
            return
        if not self.current_room.opponents:
            print("There is nothing here to attack.")
            return
        # Gives opponents different weaknesses if they are a special enemy.
        for opponent in self.current_room.opponents[:]:
            # Full damage only if the opponent has no weakness or the right item is equipped
            if opponent.weakness is None or self.active_item.name == opponent.weakness:
                damage = self.active_item.damage
            else:
                damage = 0
                print(f"Your {self.active_item.name} has no effect on the {opponent.name}.")

            # Takes away opponents health if damaged by a players item.
            opponent.health -= damage
            print(f"You hit the {opponent.name} for {damage} damage.")

            # Kills opponents at health <= 0
            if opponent.health <= 0:
                print(f"You have slain the {opponent.name}.")
                self.current_room.opponents.remove(opponent)

                # Open the passageway once both brothers are dead
                if len(brother_light_chamber.opponents) == 0 and len(brother_darkness_chamber.opponents) == 0:
                    if passageway not in gate_room.connected_rooms:
                        print("A grinding sound echoes through the Main Cell. The Passageway has opened.")
                        gate_room.connect_room(passageway)

                        # The swords crumble once their work is done
                        for item in self.player_inventory[:]:
                            if item.name == "Sword of Light" or item.name == "Sword of Darkness":
                                self.player_inventory.remove(item)
                        print("Your swords crumble to dust.")
                        self.active_item = dagger
            else:
                print(f"The {opponent.name} has {opponent.health} HP remaining.")
                self.health -= opponent.damage
                print(f"The {opponent.name} hits you for {opponent.damage} damage. You have {self.health} HP left.")
                # Kills player when health reaches zero.
                if self.health <= 0:
                    self.perish()
                    return

    def activate(self):
        """Lets the player interact with objects in the room."""
        if len(self.current_room.objects) == 0:
            print("There is nothing here to interact with.")
        for object in self.current_room.objects:
            object.activate(self)
                
    def perish(self):
        """Kills the player and respawns them at their room's respawn point."""
        print("You have perished...")
        self.health = 100
        self.current_room = self.current_room.respawn_point
        print(f"You awaken in the {self.current_room.name}.")

    def block(self):
        pass

# Creation of different rooms and their names
breach = Room("The Breach")
hall_of_souls = Room("Hall of Souls")
chamber_of_light = Room("Chamber of Light")
chamber_of_darkness = Room("Chamber of Darkness")
portal = Room("The Portal")
gate_room = Room("Main Cell")
brother_light_chamber = Room("Cell of Light")
brother_darkness_chamber = Room("Cell of Darkness")
passageway = Room("Passageway")

# Connects the rooms together
breach.connect_room(hall_of_souls)
hall_of_souls.connect_rooms([chamber_of_light, chamber_of_darkness])
chamber_of_light.connect_room(hall_of_souls)
chamber_of_darkness.connect_room(hall_of_souls)
portal.connect_room(gate_room)
gate_room.connect_rooms([brother_light_chamber, brother_darkness_chamber])
brother_light_chamber.connect_room(gate_room)
brother_darkness_chamber.connect_room(gate_room)

# Creates opponents for the player.
acolyte = Opponent("King's Acolyte", 10, 5, hall_of_souls)
# copy.deepcopy(acolyte)
brother_of_light = Opponent("Brother of Light", 75, 100, brother_light_chamber, "Sword of Darkness")
brother_of_darkness = Opponent("Brother of Darkness", 75, 100, brother_darkness_chamber, "Sword of Light")

# Creates the player and their spawn point.
bob = Player("Player", 100, breach)
# Adds the dagger to the players inventory and sets it as the active item.
dagger = Item("Dagger", 10)
bob.player_inventory.append(dagger)
bob.active_item = dagger

# Creates different items for the player.
orb_of_light = Item("Orb of Light", 0)
orb_of_darkness = Item("Orb of Darkness", 0)
sword_of_light = Item("Sword of Light", 100)
sword_of_darkness = Item("Sword of Darkness", 100)
prismatic_sword = Item("Prismatic Sword", 200)

# Creates an object
orb_conduit = Object("Orbicular Conduit")

# Adds items to rooms
chamber_of_light.items.append(orb_of_light)
chamber_of_darkness.items.append(orb_of_darkness)
brother_darkness_chamber.items.append(sword_of_darkness)
brother_light_chamber.items.append(sword_of_light)
passageway.items.append(prismatic_sword)

# Adds objects to rooms
hall_of_souls.objects.append(orb_conduit)

# Adds opponents to rooms
hall_of_souls.opponents.append(acolyte)
brother_light_chamber.opponents.append(brother_of_light)
brother_darkness_chamber.opponents.append(brother_of_darkness)

# Dying in the chamber area sends you back to the Breach
breach.respawn_point = breach
hall_of_souls.respawn_point = breach
chamber_of_light.respawn_point = breach
chamber_of_darkness.respawn_point = breach

# Dying in the cells sends you to the Portal
gate_room.respawn_point = portal
brother_light_chamber.respawn_point = portal
brother_darkness_chamber.respawn_point = portal

# Dying in the passageway respawns you at the passageway
passageway.respawn_point = passageway

while True:
    bob.action()