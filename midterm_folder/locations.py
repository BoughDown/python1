# from room import Room
from opponent import Opponent
from item import Item
from mechanics import *
from room import Room
from copy import copy

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


orb_of_light = Item("Orb of Light", 0)
orb_of_darkness = Item("Orb of Darkness", 0)
sword_of_light = Item("Sword of Light", 100)
sword_of_darkness = Item("Sword of Darkness", 100)
prismatic_sword = Item("Prismatic Sword", 200)

chamber_of_light.items.append(orb_of_light)
chamber_of_darkness.items.append(orb_of_darkness)
brother_darkness_chamber.items.append(sword_of_darkness)
brother_light_chamber.items.append(sword_of_light)
passageway.items.append(prismatic_sword)

hall_of_souls.opponents.append(acolyte)
brother_light_chamber.opponents.append(brother_of_light)
brother_darkness_chamber.opponents.append(brother_of_darkness)
mid_plate.opponents.append(knight)
left_plate.opponents.append(copy(knight))
right_plate.opponents.append(copy(knight))
warpriest_room.opponents.append(warpriest)

# Dying in the chamber area sends you back to the Breach
breach.respawn_point = breach
hall_of_souls.respawn_point = breach
chamber_of_light.respawn_point = breach
chamber_of_darkness.respawn_point = breach

# Dying in the cells sends you to the Portal
gate_room.respawn_point = portal
brother_light_chamber.respawn_point = portal
brother_darkness_chamber.respawn_point = portal

passageway.respawn_point = passageway
warpriest_room.respawn_point = passageway
mid_plate.respawn_point = passageway
left_plate.respawn_point = passageway
right_plate.respawn_point = passageway
threshold.respawn_point = threshold