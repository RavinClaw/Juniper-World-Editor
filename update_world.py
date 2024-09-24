"""
This file is not a library
all this file does it allow you to reformat a world file it does not load in the editor

use: `python update_world.py world_you_want_to_update`
"""
import sys
import json


args = sys.argv

filename: str = args[1]


with open(filename, "r") as file:
    world = json.load(file)


for tile in world:
    if not "material" in tile:
        tile["material"] = None
    
    if not "building" in tile:
        tile["building"] = None
    
    if not "npc" in tile:
        tile["npc"] = None

    if not "layer" in tile:
        tile["layer"] = 0


with open(filename, "w") as file:
    json.dump(world, file)
