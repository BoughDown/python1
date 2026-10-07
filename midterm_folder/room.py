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
