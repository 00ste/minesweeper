import pygame
from field import Field
import constants
import functions



pygame.init()
main_window = pygame.display.set_mode((constants.D_WIDTH, constants.D_HEIGHT))
pygame.display.set_caption('Minesweeper')

clock = pygame.time.Clock()

tiles = []
for i in constants.TILES_PATHS:
    tiles.append(pygame.image.load(constants.IMG_ROOT + i))

f = Field(10, 10, 15)

f.console_print()

tile_size = 65
x_offset = 0
y_offset = 0



def tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exiting...")
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coords = functions.get_cell_hover(f, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], tile_size)
            if mouse_coords != "null":
                f.reveal(mouse_coords[0], mouse_coords[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_offset -= 1
            if event.key == pygame.K_RIGHT:
                x_offset += 1
            if event.key == pygame.K_UP:
                y_offset -= 1
            if event.key == pygame.K_DOWN:
                y_offset += 1



    clock.tick(60)


def render(tile_size, x_offset, y_offset):
    # BACKGROUND
    main_window.blit(pygame.transform.scale(pygame.image.load(constants.IMG_ROOT + constants.BG_PATH), (constants.D_WIDTH, constants.D_HEIGHT)), (0, 0))

    # SHOW ALL THE CELLS
    """for i in range(len(tiles)):
        main_window.blit(pygame.transform.scale(tiles[i], (tile_size, tile_size)), (i*tile_size + 10, 10))"""

    # create a surface to contain all the tiles
    tiles_grid = pygame.Surface((650, 650))
    tiles_grid.fill((200, 200, 10))
    
    # blit all the tiles to the surface
    for x in range(f.width()):
        for y in range(f.height()):
            pos = (x*tile_size + x_offset, y*tile_size + y_offset)
            if f.cell(x, y).hidden:
                if f.cell(x, y).flagged:
                    tiles_grid.blit(pygame.transform.scale(tiles[9], (tile_size, tile_size)), pos)
                else:
                    tiles_grid.blit(pygame.transform.scale(tiles[10], (tile_size, tile_size)), pos)
            else:
                tiles_grid.blit(pygame.transform.scale(tiles[f.cell(x,y).value], (tile_size, tile_size)), pos)
            pygame.draw.rect(main_window, (255, 0, 0), (x*tile_size + x_offset, y*tile_size + y_offset, 10, 10))
    
    # blit that surface onto the main window
    main_window.blit(tiles_grid, (10, 10))
    
    """
    for x in range(f.width()):
        for y in range(f.height()):
            if f.cell(x, y).hidden:
                if f.cell(x, y).flagged:
                    main_window.blit(pygame.transform.scale(tiles[9], (tile_size, tile_size)), (x*tile_size + 10, y*tile_size + 10))
                else:
                    main_window.blit(pygame.transform.scale(tiles[10], (tile_size, tile_size)), (x*tile_size + 10, y*tile_size + 10))
            else:
                main_window.blit(pygame.transform.scale(tiles[f.cell(x,y).value], (tile_size, tile_size)), (x*tile_size + 10, y*tile_size + 10))
    """
    # debug info
    functions.print_text(main_window, format(pygame.mouse.get_pos()), constants.D_WIDTH-150, constants.D_HEIGHT-50, 20)
    functions.print_text(main_window, format(functions.get_cell_hover(f, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], tile_size)), constants.D_WIDTH-150, constants.D_HEIGHT-25, 20)          
    
    # TILE HOVER INDICATOR
    mouse_coords = functions.get_cell_hover(f, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], tile_size)
    if mouse_coords != "null":
        #pygame.draw.rect(main_window, pygame.Color(255, 255, 0), pygame.Rect(10+mouse_coords[0]*tile_size, 10+mouse_coords[1]*tile_size, tile_size, tile_size), 3)
        hover_rect = pygame.Surface((tile_size, tile_size))
        hover_rect.set_alpha(128)
        hover_rect.fill((255, 240, 123))
        main_window.blit(hover_rect, (10+mouse_coords[0]*tile_size, 10+mouse_coords[1]*tile_size))
    
    """
    # SURFACES TEST
    object1 = pygame.Surface((50, 70))
    object1.fill((255, 0, 0))
    section1 = pygame.Surface((150, 180))
    section1.fill((0, 255, 255))
    section1.blit(object1, (10, 0))
    main_window.blit(section1, (800, 300))
    """



    # SHOW SOME BUTTONS
    pygame.display.update()



while not f.defeat or f.victory:
    tick()
    render(tile_size, x_offset, y_offset)