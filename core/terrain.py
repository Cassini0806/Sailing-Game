import pygame
import random
from perlin_noise import PerlinNoise

#Aqui tem mais comentários do que códigokkkkkk

#Configurações iniciais

width, heigh = 720, 480
tile_size = 16
map_width = int(width / tile_size)
map_heigth = int(heigh / tile_size)

pygame.init()
screen = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("Mundo Procedural")

#Geração do terreno

class terrain:

    global map_heigth
    global map_width
    global tile_size
    global width
    global heigh

    def __init__(self):
        pass    
        
    def terrain_manager(seed):
        # cria o gerador de ruído
        noise = PerlinNoise(octaves=6, seed=seed)
        
        world = []
        scale = 50.0  # controla o "zoom" no mapa

        for y in range(map_heigth):
            row = []
            for x in range(map_width):
                nx = x / scale
                ny = y / scale

                # gera o valor do ruído (retorno ~ -1 a 1)
                value = noise([nx, ny])
                row.append(value)
            world.append(row)
        return world

    def gera_biomas(value):
        #Define qual ruído é qual bioma (Tile)
        h = (value + 1) / 2
        if h < 0.5:
            return (0,0,255) #Mar
        if h == 0.5:
            return (240,240,64) #Praia
        else:
            return (0,255,0) #Grama
        
    def desenha_mundo(mundo):
        for y in range(map_heigth):
            for x in range(map_width):
                tile = terrain.gera_biomas(mundo[y][x])
                pygame.draw.rect(screen, tile, (x*tile_size, y*tile_size, tile_size, tile_size))

def main():
    clock = pygame.time.Clock()
    seed = random.randint(0, 1000)
    world = terrain.terrain_manager(seed)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        terrain.desenha_mundo(world)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()