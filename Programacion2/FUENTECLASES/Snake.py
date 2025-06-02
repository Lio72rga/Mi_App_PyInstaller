import pygame
import sys
import random

# Screen dimensions
screen_width = 800  # You can adjust this value as needed

# Initialize pygame and create the screen surface
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_width))

#functions
def create_tiles():
    color_one = (94, 96, 206)
    color_two = (78, 168, 222)
    tile_size = screen_width / 20
    x = 0
    y = 0

    for i in range(int(tile_size)):
        for j in range(int(tile_size)):
            
            color = 0
            if j % 2 == 0:
                color = color_one

            else:
                color = color_two

