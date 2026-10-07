from room import Room

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
