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

    def activate(self, player):
        # Collect every orb the player is carrying if the object requires orbs.
        orbs = []
        if "Orbicular" in self.name:
            for item in player.player_inventory:
                if "Orb" in item.name:
                    orbs.append(item)
            if len(orbs) == 0:
                print(f"The {self.name} fails to respond. You have nothing to give it.")
                return
            for orb in orbs:
                player.player_inventory.remove(orb)
                self.deposited.append(orb)
                print(f"You place the {orb.name} into the {self.name}.")

                # Don't keep holding an orb that's now inside the conduit
                if player.active_item == orb:
                    player.active_item = dagger

        if len(self.deposited) == 1:
            print("The conduit glows faintly.")
        elif len(self.deposited) == 2:
            print(f"The {self.name} sparks to life.")
            hall_of_souls.connect_room(portal)

        if "Statue" in self.name:
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
        self.respawn_point = None
    
    def connect_room(self, room_to_connect: Room):
        """Connects a room."""
        self.connected_rooms.append(room_to_connect)
    
    def connect_rooms(self, rooms_to_connect: Room):
        """Connects a list of rooms."""
        self.connected_rooms += rooms_to_connect
    
    def __repr__(self):
        return self.name

breach = Room("The Breach")
hall_of_souls = Room("Hall of Souls")
chamber_of_light = Room("Chamber of Light")
chamber_of_darkness = Room("Chamber of Darkness")
portal = Room("The Portal")
gate_room = Room("Main Cell")
brother_light_chamber = Room("Cell of Light")
brother_darkness_chamber = Room("Cell of Darkness")
passageway = Room("Passageway")
mid_plate = Room("Central Tomb")
left_plate = Room("Tomb of Light")
right_plate = Room("Tomb of Darkness")
warpriest_room = Room("Warpriest's Chamber")
threshold = Room("The Threshold")

breach.connect_room(hall_of_souls)
hall_of_souls.connect_rooms([chamber_of_light, chamber_of_darkness])
chamber_of_light.connect_room(hall_of_souls)
chamber_of_darkness.connect_room(hall_of_souls)
portal.connect_room(gate_room)
gate_room.connect_rooms([brother_light_chamber, brother_darkness_chamber])
brother_light_chamber.connect_room(gate_room)
brother_darkness_chamber.connect_room(gate_room)
passageway.connect_room(mid_plate)
warpriest_room.connect_rooms([mid_plate, left_plate, right_plate])
mid_plate.connect_rooms([left_plate, right_plate, warpriest_room, passageway])
left_plate.connect_rooms([mid_plate, warpriest_room])
right_plate.connect_rooms([mid_plate, warpriest_room])

acolyte = Opponent("King's Acolyte", 10, 5, hall_of_souls, None)
knight = Opponent("Revenant Knight", 250, 20, mid_plate, None)
brother_of_light = Opponent("Brother of Light", 75, 100, brother_light_chamber, "Sword of Darkness")
brother_of_darkness = Opponent("Brother of Darkness", 75, 100, brother_darkness_chamber, "Sword of Light")
warpriest = Opponent("Warpriest", 1000, 30, warpriest_room, "Orb of Light")

dagger = Item("Dagger", 10)