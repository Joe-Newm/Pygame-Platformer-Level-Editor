import pygame
import sys
pygame.init()

screen_width = 800
screen_height = 640
lower_margin = 100
side_margin = 300

screen = pygame.display.set_mode((screen_width + side_margin, screen_height + lower_margin))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    pygame.display.update()
pygame.quit()