import pygame 
from core.player import *
from core.terrain import *


pygame.init()

WIDTH = 960
HEIGHT = 640

tamtela = (WIDTH, HEIGHT)
tela = pygame.display.set_mode(tamtela)
pygame.display.set_caption("FISH&FIGHT")
clock = pygame.time.Clock()
running = True

# Mundo maior que a tela
WORLD_WIDTH, WORLD_HEIGHT = 2000, 2000

cx = player.x -  WIDTH // 2
cy = player.y - HEIGHT // 2

def movimentacao():

    global cx, cy

    camera_x = player.x -  WIDTH // 2
    camera_y = player.y - HEIGHT // 2

    cx = camera_x
    cy = camera_y

    # Mantém o player dentro do mundo
    player_x = player.x
    player_y = player.y

    player.navegar()#Movimenta o jogador
    screen.blit(player.sprites[player.table][player.current_sprite], (player_x - camera_x, player_y - camera_y,))# Desenha o sprite atual
    player.current_sprite = (player.current_sprite + 1) % len(player.sprites[player.table])# Alterna o sprite para animar (simplesmente trocando o índice)

seed = random.randint(0, 1000)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    tela.fill("blue")
    terrain.desenha_mundo(seed, tela, cx, cy, WIDTH, HEIGHT)

    movimentacao()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(16)  # limits FPS to 12

pygame.quit()