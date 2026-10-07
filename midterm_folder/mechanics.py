from locations import hall_of_souls, dagger, portal

class Mechanics:
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
            if player.activate():
                pass

orb_conduit = Mechanics("Orbicular Conduit")
ctotem = Mechanics("Central Statue")
ltotem = Mechanics("Statue of Light")
dtotem = Mechanics("Statue of Darkness")