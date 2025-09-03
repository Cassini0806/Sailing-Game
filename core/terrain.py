
from perlin_noise import PerlinNoise
import random

# define tela
WIDTH, HEIGHT = 500, 500

# Initialize Perlin noise
noise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))

# Generate noise values
noise_map = [[noise([i / WIDTH, j / HEIGHT]) for j in range(HEIGHT)] for i in range(WIDTH)]


    # Draw the noise map
    for i, row in enumerate(noise_map):
        for j, value in enumerate(row):
            # Map noise value to a color (example: grayscale)
            color_intensity = int((value + 1) * 127.5) # Scale from -1 to 1 to 0 to 255
            color = (color_intensity, color_intensity, color_intensity)
            pygame.draw.rect(screen, color, pygame.Rect(j, i, 1, 1))


