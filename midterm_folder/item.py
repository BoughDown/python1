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