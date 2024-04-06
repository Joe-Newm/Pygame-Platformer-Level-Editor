import pygame
import sys
pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 800
screen_height = 640
lower_margin = 100
side_margin = 300

screen = pygame.display.set_mode((screen_width + side_margin, screen_height + lower_margin))
pygame.display.set_caption("Level Editor")

#define game variables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

ROWS = 20
COLUMNS = 150
TILE_SIZE = screen_height // ROWS

def draw_grid():
    # vertical lines 
    for c in range(COLUMNS + 1):
        pygame.draw.line(screen, "white", (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, screen_height))
    # horizontal lines 
    for c in range(ROWS + 1):
        pygame.draw.line(screen, "white", (0, c* TILE_SIZE), (screen_width, c * TILE_SIZE))

run = True
while run:
    clock.tick(60)
    screen.fill((112, 217, 255))
    draw_grid()
    # scroll the map
    if scroll_right:
        scroll += 5 * scroll_speed
    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()
pygame.quit()