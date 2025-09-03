import pygame 
from core.player import *


pygame.init()

tamtela = (720, 480)
tela = pygame.display.set_mode(tamtela)
pygame.display.set_caption("FISH&FIGHT")
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    tela.fill("blue")
    
    # RENDER YOUR GAME HERE

    movimentacao()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(16)  # limits FPS to 12

pygame.quit()