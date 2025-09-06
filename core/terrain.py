import pygame
import random
from perlin_noise import PerlinNoise


#Aqui tem mais comentários do que códigokkkkkk

#Configurações iniciais

width, heigh = 960, 640
tile_size = 48
chunk_size = 8
map_width = int(width / chunk_size)
map_heigth = int(heigh / chunk_size)

game_map = {} #Aqui as chunks serão adicionadas

#8 X 5

pygame.init()
tela = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("Mundo Procedural")

# Carrega a sprite sheet (toda a imagem com vários sprites)
sprite_sheet = pygame.image.load("assets/tilemap.png").convert_alpha()

#Geração do terreno
class terrain:

    # Função para cortar um sprite da sprite sheet
    def get_sprite(sheet, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)  # Permite transparência
        sprite.blit(sheet, (0, 0), (x, y, width, height))  # Copia a parte desejada
        sprite = pygame.transform.scale(sprite, (16*3, 16*3))
        return sprite

    # Cria uma matriz (lista) de sprites, cada linha é uma direção e cada coluna um frame da animação
    sprites = [
            [get_sprite(sprite_sheet, 0, 0, 16, 16)],
            [get_sprite(sprite_sheet, 16, 16, 16, 16)],
            [get_sprite(sprite_sheet, 0, 32, 16, 16), get_sprite(sprite_sheet, 0, 48, 16, 16), get_sprite(sprite_sheet, 16, 48, 16, 16), get_sprite(sprite_sheet, 32, 48, 16, 16)],
        ]

    #Obrigado @DaFluffyPotato (Thank you @DaFluffyPotato)
    def gera_chunk(seed, x, y):
        noise = PerlinNoise(octaves=6, seed=seed)
        scale = 160.0  # controla o "zoom" no mapa; Controla a densidade do ruído. Aumente se tudo estiver “granulado”; diminua se estiver “liso demais”.
        
        chunk_tiles = []
        for y_pos in range(chunk_size):
            for x_pos in range(chunk_size):
                target_x = x * chunk_size + x_pos
                target_y = y * chunk_size + y_pos

                nx = target_x / scale
                ny = target_y / scale
                #Converte coordenadas de tile (x, y) para coordenadas de ruído (nx, ny) e divide por scale, “espalhando” os pontos no espaço do ruído, suavizando o mapa.
                value = noise([nx, ny])#gera o valor do ruído (retorno ~ -1 a 1)
                h = (value + 1) / 2
                # normaliza para [0, 1]
                
                # Define tipos de tiles com base na altura
                tile_type = 0 #agua
                if h > 0.63:
                    tile_type = 2 #grama
                elif h > 0.6:
                    tile_type = 1 #areia

                tree = 0 
                chance = random.randint(0,9)
                if tile_type >= 1 and chance < 3:
                    tree = 1
                elif tile_type >= 1 and chance < 2:
                    tree = 2
                elif tile_type >= 1 and chance < 1:
                    tree = 3    
                if tile_type != 0: 
                    chunk_tiles.append([[target_x,target_y],tile_type, tree])
        return chunk_tiles

    def desenha_mundo(seed, screen, cx, cy, WIDTH, HEIGHT):
        # calcula quantos tiles cabem na tela
        tiles_x = WIDTH // tile_size + 2
        tiles_y = HEIGHT // tile_size + 2

        # converte posição da câmera para tile inicial
        start_x = cx // tile_size
        start_y = cy // tile_size

        for y in range(start_y, start_y + tiles_y):
                for x in range(start_x, start_x + tiles_x):
                    target_chunk = str(x // chunk_size) + ';' + str(y // chunk_size)

                    if target_chunk not in game_map:
                        game_map[target_chunk] = terrain.gera_chunk(seed, x // chunk_size, y // chunk_size)

                    for pos, tile, tree in game_map[target_chunk]:
                        tx, ty = pos
                        if tx == x and ty == y:  # só desenha o tile certo
                            sprite = terrain.sprites[tile][0]
                            screen.blit(sprite, (tx * tile_size - cx, ty * tile_size - cy))
                            # Se for grama e tiver árvore
                            if tile >= 1 and tree == 1:
                                screen.blit(terrain.sprites[2][1], (tx * tile_size - cx, ty * tile_size - cy))
                            if tile >= 1 and tree == 2:
                                screen.blit(terrain.sprites[2][2], (tx * tile_size - cx, ty * tile_size - cy))
                            if tile >= 1 and tree == 3:
                                screen.blit(terrain.sprites[2][3], (tx * tile_size - cx, ty * tile_size - cy))

# if __name__ == "__main__":
#     main()