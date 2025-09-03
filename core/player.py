import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))

# Carrega a sprite sheet (toda a imagem com vários sprites)
sprite_sheet = pygame.image.load("assets/boat.png").convert_alpha()

class player:

    global sprite_sheet

    def __init__(self):
        pass

    # Função para cortar um sprite da sprite sheet
    def get_sprite(sheet, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Permite transparência
        sprite.blit(sheet, (0, 0), (x, y, width, height))  # Copia a parte desejada
        sprite = pygame.transform.scale(sprite, (16*3, 16*3))
        return sprite

    # Criamos uma tabela (lista) de sprites
    sprites = [
            [
                get_sprite(sprite_sheet, 0, 0, 16, 16),
                get_sprite(sprite_sheet, 0, 16, 16, 16),
            ],
            [
                get_sprite(sprite_sheet, 16, 0, 16, 16),
                get_sprite(sprite_sheet, 16, 16, 16, 16),
            ],
            [
                get_sprite(sprite_sheet, 32, 0, 16, 16),
                get_sprite(sprite_sheet, 32, 16, 16, 16),
            ],
            [
                get_sprite(sprite_sheet, 48, 0, 16, 16),
                get_sprite(sprite_sheet, 48, 16, 16, 16),
            ],
        ]
    
    tabela = [0,1,2,3]

    # Posição do sprite atual
    table = 0
    current_sprite = 0
    x, y = 100, 100
    speed = 8

    def navegar():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
            player.table -= player.table
            player.table *= -1
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
            player.table -= player.table + 3
            player.table *= -1
        if keys[pygame.K_UP]:
            player.y -= player.speed
            player.table -= player.table + 2 
            player.table *= -1
        if keys[pygame.K_DOWN]:
            player.y += player.speed
            player.table -= player.table + 1 
            player.table *= -1

def movimentacao():
    player.navegar()
    # Desenha o sprite atual
    screen.blit(player.sprites[player.table][player.current_sprite], (player.x, player.y))
    # Alterna o sprite para animar (simplesmente trocando o índice)
    player.current_sprite = (player.current_sprite + 1) % len(player.sprites[player.table])



