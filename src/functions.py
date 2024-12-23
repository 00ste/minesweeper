import pygame

def print_text(display, text, x, y, size):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, pygame.Color(255, 255, 0))
    display.blit(img, (x, y))


def get_cell_hover(field, x, y, pixel_size):
    if x < 10 or y < 10:            # x or y are out (before pixels)
        return "null"
    if x > 10+field.width()*pixel_size:         # x is out (after pixels)
        return "null"
    if y > 10+field.height()*pixel_size:        # y is out (after pixels)
        return "null"
    return ((x-10)//pixel_size, (y-10)//pixel_size)