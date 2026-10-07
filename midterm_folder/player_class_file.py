import os
from room import Room
from locations import *

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
            message = "You have breached the alien ship. You must destroy their king before everything you know succumbs to him.\nPress 'T' to travel, 'I' to see your inventory, 'E' to equip an item, 'A' to interact with objects, and 'B' to attack.\n"
            self.first_time = False
        else:
            message = "T/I/E/A/B? "
        
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
            # Ignores capitalization
            # if user_choice.lower() != room.name.lower():
            #     # Only occurs if a successful move has not been made.
            #     print("Invalid choice. Try again.")
            if user_choice.lower() == room.name.lower():
                self.current_room = room
                os.system("cls")
                print(f"You have arrived in the {self.current_room.name}.")

                for opponent in self.current_room.opponents:
                    print(f"You come across the {opponent.name}.")

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

                for mechanics in self.current_room.objects:
                    print(f"You have found the {mechanics.name}.")
                return None
            
        print("Invalid room choice. Try again.")

    def use_active_item(self):
        """Calls the active item's use method."""
        self.active_item.use()

    def attack(self):
        if self.active_item is None:
            print("You have nothing equipped.")
            return
        if not self.current_room.opponents:
            print("There is nothing here to attack.")
            return
        for opponent in self.current_room.opponents[:]:
            # Full damage only if the opponent has no weakness or the right item is equipped
            if opponent.weakness is None or self.active_item.name == opponent.weakness:
                damage = self.active_item.damage
            else:
                damage = 0
                print(f"Your {self.active_item.name} has no effect on the {opponent.name}.")

            opponent.health -= damage
            print(f"You hit the {opponent.name} for {damage} damage.")

            if opponent.health <= 0:
                print(f"You have slain the {opponent.name}.")
                self.current_room.opponents.remove(opponent)

                # Open the passageway once both brothers are dead
                if len(brother_light_chamber.opponents) == 0 and len(brother_darkness_chamber.opponents) == 0:
                    if passageway not in gate_room.connected_rooms:
                        print("A grinding sound echoes through the Main Cell. The Passageway has opened.")
                        gate_room.connect_room(passageway)

                        # The swords are removed from the players inventory once the brothers are killed.
                        for item in self.player_inventory[:]:
                            if item.name == "Sword of Light" or item.name == "Sword of Darkness":
                                self.player_inventory.remove(item)
                        print("Your swords crumble to dust.")
                        self.active_item = None
            else:
                print(f"The {opponent.name} has {opponent.health} HP remaining.")
                self.health -= opponent.damage
                print(f"The {opponent.name} attacks you for {opponent.damage} damage. You have {self.health} HP left.")
                if self.health <= 0:
                    self.perish()
                    return

    def activate(self):
        """Lets the player interact with objects in the room."""
        if len(self.current_room.mechanics) == 0:
            print("There is nothing here to interact with.")
        for mechanics in self.current_room.mechanics:
            mechanics.activate(self)

                
    def perish(self):
        """Kills the player and respawns them at their room's respawn point."""
        print("You have perished...")
        self.health = 100
        self.current_room = self.current_room.respawn_point
        print(f"You awaken in the {self.current_room.name}.")