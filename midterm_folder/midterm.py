"""
Midterm - Tommy Bough

Build off of the Dank Dungeon to make a better product.
"""

from copy import copy
from copy import deepcopy
import os
from utilities import room_list, room_objects
from item import Item
from opponent import Opponent
from mechanics import Mechanics, orb_conduit, ctotem, ltotem, dtotem
from room import Room
from player_class_file import Player
from locations import *

bob = Player("Player", 200, passageway)
bob.player_inventory.append(dagger)
bob.active_item = dagger

hall_of_souls.mechanics.append(orb_conduit)
mid_plate.mechanics.append(ctotem)
left_plate.mechanics.append(ltotem)
right_plate.mechanics.append(dtotem)

while True:
    bob.action()