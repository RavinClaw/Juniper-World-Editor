import pygame
import json
import os

"""
The Editor

A program designed for the creation of world json files that can be used as levels in the program
!THIS IS STILL UNDER DEVELOPMENT!
"""

pygame.font.init()

def create_new_tile(x: int, y: int, material: int, layer: int = 0) -> dict:
    """
    Creates a new tile

    :x: int
    :y: int
    :material: int
    :layer: int
    """
    new_tile = {
        "x": x,
        "y": y,
        "material": material,
        "building": None,
        "npc": None,
        "layer": layer
    }
    return new_tile

def create_new_building(x: int, y: int, building: int, layer: int = 1) -> dict:
    """
    Creates a new building

    :x: int
    :y: int
    :building: int
    :layer: int
    """
    new_building = {
        "x": x,
        "y": y,
        "material": None,
        "building": building,
        "npc": None,
        "layer": layer
    }
    return new_building

def create_new_npc(x: int, y: int, npc: int, layer: int = 1) -> dict:
    """
    Creates a new npc

    :x: int
    :y: int
    :npc: int
    :layer: int
    """
    new_npc = {
        "x": x,
        "y": y,
        "material": None,
        "building": None,
        "npc": npc,
        "layer": layer
    }
    return new_npc

def delete_found_tile(world: list[dict], x: int, y: int, layer: int) -> list[dict]:
    """ Deletes the tile ath the coordinates """
    for tile in world:
        if tile["x"] == x and tile["y"] == y and tile["layer"] == layer:
            index = world.index(tile)
            world.pop(index)
    return world

def delete_found_building(world: list[dict], x: int, y: int, layer: int) -> list[dict]:
    """ Deletes the building at the coordinates """
    for building in world:
        if building["x"] == x and building["y"] == y and building["layer"] == layer:
            index = world.index(building)
            world.pop(index)
    return world

def delete_found_npc(world: list[dict], x: int, y: int, layer: int) -> list[dict]:
    """ Deletes the npc at the coordinates """
    for npc in world:
        if npc["x"] == x and npc["y"] == y and npc["layer"] == layer:
            index = world.index(npc)
            world.pop(index)
    return world

def tile_check(world: list[dict], x: int, y: int, *, layer: str = 0) -> True | False:
    """
    Checks the selected type with it's layer

    :world: list[dict]
    :x: int
    :y: int
    :layer: int
    """
    if len(world) == 0 and len(world) == 1:
        return False
    for tile in world:
        if tile["x"] == x and tile["y"] == y and tile["layer"] == layer:
            return True
    return False

def save_world(filename: str, world: list[dict]) -> None:
    """
    Saves the world to a `json` file

    :filename: str
    :world: list[dict]
    """
    try:
        with open("worlds/" + filename + ".json", "w") as file:
            json.dump(world, file, indent=4)
    except Exception as e:
        print(f"Failed to operate file:\n{e}")

def load_world(filename: str) -> list[dict] | None:
    """
    Loads the world from a `json` file

    :filename: str
    """
    try:
        with open("worlds/" + filename + ".json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to operate file:\n{e}")
        return None

class Editor:
    """
    The editor program allows for custom world creation that then can be saved to a file
    """
    def __init__(self, name: str, size_x: int, size_y: int) -> None:
        """
        Initialise the class with its parameters

        :name: str
        :size_x: int
        :size_y: int
        """
        self.size_x = size_x
        self.size_y = size_y
        self.name = name
        self.running = True
        self.world: list[dict] = []
        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Juniper World Editor")
        self.resources = [ #// All of the Resources
            pygame.image.load("resources/grass.png"),
            pygame.image.load("resources/stone.png"),
            pygame.image.load("resources/steel.png"),
            pygame.image.load("resources/oak.png"),
            pygame.image.load("resources/cape.png")
        ]
        self.buildings = [ #// All of the Buildings
            pygame.image.load("resources/buildings/store.png"),
            pygame.image.load("resources/buildings/barrel.png"),
            pygame.image.load("resources/buildings/campfire.png"),
            pygame.image.load("resources/buildings/pine.png"),
            pygame.image.load("resources/buildings/store1.png"),
            pygame.image.load("resources/buildings/tree.png"),
        ]
        self.npcs = [ #// All of the NPCS
            pygame.image.load("resources/npcs/cat.png"),
            pygame.image.load("resources/npcs/fox.png"),
            pygame.image.load("resources/npcs/npc.png"),
            pygame.image.load("resources/player.png")
        ]
        self.font = pygame.font.Font(None, 32)
        self.selected_material: int = 0 #// Selected for the material you are using
        self.selected_building: int = 0 #// Selected for the building you are using
        self.selected_npc:      int = 0 #// Selected for the npc you are using
        self.selected_type:     int = 1 #// Selects which mode you are in
        self.world_button_action_cooldown = 100
        self.border = pygame.surface.Surface((self.size_x * 32, self.size_y * 32))
        self.allow_render: bool = True
        self.display_width:  int = 20 * 32
        self.display_height: int = 20 * 32


    def run(self) -> None:
        """
        Runs the entire program
        """
        world_button_action = 0

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    elif event.key == pygame.K_LEFT:
                        if self.selected_type == 1:
                            if self.selected_material > 0:
                                self.selected_material -= 1
                        elif self.selected_type == 2:
                            if self.selected_building > 0:
                                self.selected_building -= 1
                        elif self.selected_type == 3:
                            if self.selected_npc > 0:
                                self.selected_npc -= 1

                    elif event.key == pygame.K_RIGHT:
                        if self.selected_type == 1:
                            if self.selected_material < len(self.resources) - 1:
                                self.selected_material += 1
                        elif self.selected_type == 2:
                            if self.selected_building < len(self.buildings) - 1:
                                self.selected_building += 1
                        elif self.selected_type == 3:
                            if self.selected_npc < len(self.npcs) - 1:
                                self.selected_npc += 1
                    

                    elif event.key == pygame.K_1:
                        self.selected_type = 1
                    elif event.key == pygame.K_2:
                        self.selected_type = 2
                    elif event.key == pygame.K_3:
                        self.selected_type = 3
                    
                    elif event.key == pygame.K_b:
                        self.allow_render = True
                    elif event.key == pygame.K_v:
                        self.allow_render = False

            # Renders the background grid
            for x in range(0, self.size_x, 1):
                for y in range(0, self.size_y, 1):
                    tile_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                    pygame.draw.rect(self.border, (255, 255, 255), tile_rect, 1)
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_click = pygame.mouse.get_pressed()
                    world_display_width = min(self.size_x * 32, self.display_width)
                    world_display_height = min(self.size_y * 32, self.display_height)
                    scale_x = (self.size_x * 32) / world_display_width
                    scale_y = (self.size_y * 32) / world_display_height
                    adjusted_mouse_x = mouse_pos[0] * scale_x
                    adjusted_mouse_y = mouse_pos[1] * scale_y
                    tile_x = int(adjusted_mouse_x // 32)
                    tile_y = int(adjusted_mouse_y // 32)
                    
                    if tile_rect.colliderect(pygame.Rect(mouse_pos[0] - 2, mouse_pos[1] - 1, 2, 2)):
                        
                        # Left Click Checks
                        if mouse_click[0]:
                            if self.selected_type == 1: # Selected the Material
                                check = tile_check(self.world, tile_x, tile_y, layer=0) # Layer 0 is background
                                if not check:
                                    tile = create_new_tile(tile_x, tile_y, self.selected_material, 0)
                                    self.world.append(tile)
                            
                            elif self.selected_type == 2: # Selected the Building
                                check = tile_check(self.world, tile_x, tile_y, layer=1)
                                if not check:
                                    tile = create_new_building(tile_x, tile_y, self.selected_building, 1)
                                    self.world.append(tile)
                            
                            elif self.selected_type == 3: # Selected the Npc
                                check = tile_check(self.world, tile_x, tile_y, layer=2)
                                if not check:
                                    tile = create_new_npc(tile_x, tile_y, self.selected_npc, 1)
                                    self.world.append(tile)
                        
                        # Right Click Checks
                        if mouse_click[2]:
                            if self.selected_type == 1: # Selected the Material
                                check = tile_check(self.world, tile_x, tile_y, layer=0)
                                if check:
                                    self.world = delete_found_tile(self.world, tile_x, tile_y, 0)
                            
                            elif self.selected_type == 2: # Selected the Building
                                check = tile_check(self.world, tile_x, tile_y, layer=1)
                                if check:
                                    self.world = delete_found_building(self.world, tile_x, tile_y, 1)
                            
                            elif self.selected_type == 3: # Selected the Npc
                                check = tile_check(self.world, tile_x, tile_y, layer=2)
                                if check:
                                    self.world = delete_found_npc(self.world, tile_x, tile_y, 2)

            # Get the mouse
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            mouse_rect = pygame.Rect(mouse_pos[0] - 2, mouse_pos[1] - 2, 4, 4)
            world_display_width = min(self.size_x * 32, self.display_width)
            world_display_height = min(self.size_y * 32, self.display_height)
            scale_x = (self.size_x * 32) / world_display_width
            scale_y = (self.size_y * 32) / world_display_height
            adjusted_mouse_x = mouse_pos[0] * scale_x
            adjusted_mouse_y = mouse_pos[1] * scale_y
            tile_x = int(adjusted_mouse_x // 32)
            tile_y = int(adjusted_mouse_y // 32)


            # Render of the X : Y
            textRender = self.font.render(f"{tile_x} : {tile_y}", True, (255, 255, 255))
            self.screen.blit(textRender, (self.resolution[0] - 300, 32))

            # Render the SIDE IMAGE
            if self.selected_type == 1: # Renders TILE
                self.screen.blit(pygame.transform.scale(self.resources[self.selected_material], (128, 128)), (self.resolution[0] - 400, self.resolution[1] - 450))
                textRender = self.font.render(f"{self.selected_material}", True, (255, 255, 255))
                self.screen.blit(textRender, (self.resolution[0] - 400, self.resolution[1] - 300))
            
            elif self.selected_type == 2: # Renders Buildings
                self.screen.blit(pygame.transform.scale(self.buildings[self.selected_building], (128, 128)), (self.resolution[0] - 400, self.resolution[1] - 450))
                textRender = self.font.render(f"{self.selected_building}", True, (255, 255, 255))
                self.screen.blit(textRender, (self.resolution[0] - 400, self.resolution[1] - 300))
            
            elif self.selected_type == 3: # Renders Npcs
                self.screen.blit(pygame.transform.scale(self.npcs[self.selected_npc], (128, 128)), (self.resolution[0] - 400, self.resolution[1] - 450))
                textRender = self.font.render(f"{self.selected_npc}", True, (255, 255, 255))
                self.screen.blit(textRender, (self.resolution[0] - 400, self.resolution[1] - 300))

            # Render the SAVE BUTTON
            save_button = pygame.Rect(self.resolution[0] - 400, self.resolution[1] - 100, 64, 32)
            save_button_text = self.font.render("SAVE", True, (0, 0, 0))
            pygame.draw.rect(self.screen, (0, 255, 0), save_button)
            self.screen.blit(save_button_text, (save_button.x + 1, save_button.y + 4))
            if save_button.colliderect(mouse_rect):
                if mouse_pressed[0]:
                    if self.world_button_action_cooldown <= world_button_action:
                        save_world(self.name, self.world)
                        print("Successfully Saved to File")
                        world_button_action = 0
            
            # Render the LOAD BUTTON
            load_button = pygame.Rect(self.resolution[0] - 300, self.resolution[1] - 100, 64, 32)
            load_button_text = self.font.render("LOAD", True, (0, 0, 0))
            pygame.draw.rect(self.screen, (255, 255, 0), load_button)
            self.screen.blit(load_button_text, (load_button.x + 1, load_button.y + 4))
            if load_button.colliderect(mouse_rect):
                if mouse_pressed[0]:
                    if self.world_button_action_cooldown <= world_button_action:
                        if os.path.exists(f"worlds/{self.name}.json"):
                            self.world = load_world(self.name)
                            print("Successfully Loaded File")
                            world_button_action = 0
                        else:
                            print("File Does Not Exist")
                            world_button_action = 0
            
            if self.allow_render:
                for tile in self.world: # Renders the world that has been drawn
                    if tile["npc"] is not None:
                        if tile["npc"] == 3:
                            self.border.blit(pygame.transform.scale(pygame.image.load("resources/player_marker.png"), (32, 32)), (tile["x"] * 32, tile["y"] * 32))
                        else:
                            self.border.blit(pygame.transform.scale(self.npcs[tile["npc"]], (32, 32)), (tile["x"] * 32, tile["y"] * 32))
                    if tile["building"] is not None:
                        self.border.blit(pygame.transform.scale(self.buildings[tile["building"]], (32, 32)), (tile["x"] * 32, tile["y"] * 32))
                    if tile["material"] is not None:
                        self.border.blit(pygame.transform.scale(self.resources[tile["material"]], (32, 32)), (tile["x"] * 32, tile["y"] * 32))

            self.screen.blit(pygame.transform.scale(self.border, (world_display_width, world_display_height)), (0, 0))
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            self.border.fill((0, 0, 0))
            world_button_action += 0.25

            if world_button_action > 100:
                world_button_action = 100


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Please provide 3 arguments for this game: X : Y : NAME")
        sys.exit()
    x = int(args[1])
    y = int(args[2])
    name = args[3]
    editor = Editor(name, x, y)
    editor.run()