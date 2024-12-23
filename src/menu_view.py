from constants import D_WIDTH, D_HEIGHT, IMG_ROOT, BG_PATH, TILES_PATHS
from functions import get_cell_hover, print_text
import pygame

class Menu_View:
    def __init__(self):
        self.view = pygame.Surface((D_WIDTH, D_HEIGHT))
        self.output = "null"
    
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting...")
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                self.output = "play"
    
    def render(self, display):
        # BACKGROUND
        self.view.blit(pygame.transform.scale(pygame.image.load(IMG_ROOT + BG_PATH), (D_WIDTH, D_HEIGHT)), (0, 0))

        # TEST BUTTON
        button1 = pygame.Surface((200, 50))
        button1.fill((255, 0, 0))
        self.view.blit(button1, (20, 20))
        
        display.blit(self.view, (0, 0))
        pygame.display.update()
    
    def run(self, display):
        while True:
            self.tick()
            if self.output == "play":
                return "play"
            self.render(display)