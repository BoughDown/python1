class Item:
    """
    Represents an in-game item.

    Attributes:
        name (str): The name of the item.
        
    Methods:
        use: Narrates using the item.
    """
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f"You use {self.name}")

class Player:
    """
    Represents the player.
    
    Attributes:
        name (str): The name of the player.
        inventory (list): What the player is holding.
        active_item (item): A selected item from the players inventory.
        
    Methods:
        equip: Selects an item from their inventory.
        use_active_item: Uses the selected item.
    """
    def __init__(self, name):
        self.name = name
        self.inventory = []
        # TODO make a starter item
        self.active_item = Item("Fists")

    def equip(self):
        """Sets the active item."""
        print(f"Your inventory contains:")
        for item in self.inventory:
            print(f"\t{item.name}")
        # Collects user input. If user_input matches an item's name in the inventory, make that the active item.
        user_input = ""
        equipped = False
        while not equipped:
            user_input = input("Which item would you like to equip?\n")
            for item in self.inventory:
                if user_input.lower() == item.name.lower():
                    self.active_item = item
                    equipped = True
                    break

    def use_active_item(self):
        """Calls the active item's use method."""
        self.active_item.use()

Steve = Player("Steve")
Steve.inventory.append(Item("Sword"))
Steve.inventory.append(Item("Key"))

Steve.use_active_item()
Steve.equip()
Steve.use_active_item()