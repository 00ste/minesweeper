from field import Field
from constants import D_WIDTH, D_HEIGHT, IMG_ROOT, BG_PATH, TILES_PATHS
from functions import get_cell_hover, print_text
import pygame

class Game_View:
    def __init__(self, width, height, mines):
        self.tile_size = 65
        self.x_offset = 0
        self.y_offset = 0
        self.exit = False
        self.field = Field(width, height, mines)
        self.view = pygame.Surface((D_WIDTH, D_HEIGHT))
        self.tiles = []
        for i in TILES_PATHS:
            self.tiles.append(pygame.image.load(IMG_ROOT + i))
    
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting...")
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coords = get_cell_hover(self.field, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.tile_size)
                if mouse_coords != "null":
                    self.field.reveal(mouse_coords[0], mouse_coords[1])
                    print("reveal!")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_offset -= 1
                if event.key == pygame.K_RIGHT:
                    self.x_offset += 1
                if event.key == pygame.K_UP:
                    self.y_offset -= 1
                if event.key == pygame.K_DOWN:
                    self.y_offset += 1
    
    def render(self, display):
        # BACKGROUND
        self.view.blit(pygame.transform.scale(pygame.image.load(IMG_ROOT + BG_PATH), (D_WIDTH, D_HEIGHT)), (0, 0))

        # SHOW ALL THE CELLS
        # create a surface to contain all the tiles
        tiles_grid = pygame.Surface((650, 650))
        tiles_grid.fill((200, 200, 10))
        
        # blit all the tiles to the surface
        for x in range(self.field.width()):
            for y in range(self.field.height()):
                pos = (x*self.tile_size + self.x_offset, y*self.tile_size + self.y_offset)
                if self.field.cell(x, y).hidden:
                    if self.field.cell(x, y).flagged:
                        tiles_grid.blit(pygame.transform.scale(self.tiles[9], (self.tile_size, self.tile_size)), pos)
                    else:
                        tiles_grid.blit(pygame.transform.scale(self.tiles[10], (self.tile_size, self.tile_size)), pos)
                else:
                    tiles_grid.blit(pygame.transform.scale(self.tiles[self.field.cell(x,y).value], (self.tile_size, self.tile_size)), pos)
                pygame.draw.rect(self.view, (255, 0, 0), (x*self.tile_size + self.x_offset, y*self.tile_size + self.y_offset, 10, 10))
        
        # blit that surface onto the main window
        self.view.blit(tiles_grid, (10, 10))

        # DEBUG INFO
        print_text(self.view, format(pygame.mouse.get_pos()), D_WIDTH-150, D_HEIGHT-50, 20)
        print_text(self.view, format(get_cell_hover(self.field, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.tile_size)), D_WIDTH-150, D_HEIGHT-25, 20)          
        
        # TILE HOVER INDICATOR
        mouse_coords = get_cell_hover(self.field, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.tile_size)
        if mouse_coords != "null":
            #pygame.draw.rect(main_window, pygame.Color(255, 255, 0), pygame.Rect(10+mouse_coords[0]*tile_size, 10+mouse_coords[1]*tile_size, tile_size, tile_size), 3)
            hover_rect = pygame.Surface((self.tile_size, self.tile_size))
            hover_rect.set_alpha(128)
            hover_rect.fill((255, 240, 123))
            self.view.blit(hover_rect, (10+mouse_coords[0]*self.tile_size, 10+mouse_coords[1]*self.tile_size))
        
        display.blit(self.view, (0, 0))
        pygame.display.update()
    
    def run(self, display):
        while True:
            self.tick()
            if self.field.victory:
                return "victory"
            elif self.field.defeat:
                return "defeat"
            self.render(display)