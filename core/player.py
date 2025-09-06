import pygame
#from main import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((720, 480))

# Carrega a sprite sheet (toda a imagem com vários sprites)
sprite_sheet = pygame.image.load("assets/boat.png").convert_alpha()

class player:

    # Função para cortar um sprite da sprite sheet
    def get_sprite(sheet, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Permite transparência
        sprite.blit(sheet, (0, 0), (x, y, width, height))  # Copia a parte desejada
        sprite = pygame.transform.scale(sprite, (16*3, 16*3))
        return sprite

    # Cria uma matriz (lista) de sprites, cada linha é uma direção e cada coluna um frame da animação
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
    table = 0 #Linha atual
    current_sprite = 0 #Coluna atual
    x, y = 100, 100 #Coordenadas Player
    speed = 8 #Velocidade do Player(tornar modificavel pela gameplay futuramente)

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




