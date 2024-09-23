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