import pygame
from constants import D_WIDTH, D_HEIGHT
from game_view import Game_View
from menu_view import Menu_View


pygame.init()
main_window = pygame.display.set_mode((D_WIDTH, D_HEIGHT))
pygame.display.set_caption('Minesweeper')


while True:
    menu = Menu_View()
    choice = menu.run(main_window)
    if choice == "play":
        game_view = Game_View(8, 8, 10)
        game_view.run(main_window)

