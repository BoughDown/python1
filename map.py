"""
Minimal working example of a map
"""

class Room:
    """
    Class representing the idea of a room in our world.

    Attributes: 
        name (str): The name of the room
        connected_rooms (list of rooms): A list of the connected rooms.


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
    """
    Class for the PC.

    Attributes:
        current_room (room): The room the player is currently in.

    Methods:
        move
    """
    def __init__(self, current_room: Room):
        self.current_room = current_room

    def move(self):
        """
        Offers the player a list of connected rooms to choose from, moves the player if the player selects an option.
        """
        print(f"You are currently in the {self.current_room.name}. You can go to the:")
        for room in self.current_room.connected_rooms:
            print(f"\t{room.name}")

        # Collects the user's choice and compare to the options. Move user if there's a match.
        user_choice = input("Where would you like to go?\n")
        for room in self.current_room.connected_rooms:
            # Ignores capitalization
            if user_choice.lower() == room.name.lower():
                self.current_room = room
                # Quitting the function if a successful move has been made.
                return None
        # Only occurs if a successful move has not been made.
        print("Sorry, that's not a valid option, please check spelling...")

hallway = Room("Hallway")
living_room = Room("Living Room")
study =  Room("Study")
dying_room =  Room("Dying Room")
basement =  Room("Basement")

# Connect the rooms to make the map
hallway.connect_rooms([living_room, basement])

living_room.connect_room(hallway)
living_room.connect_room(study)

dying_room.connect_rooms([basement, study])

study.connect_room(living_room)

basement.connect_room(dying_room)

player = Player(hallway)

# print(player.current_room.connected_rooms)

while True:
    player.move()