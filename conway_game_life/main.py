import pygame

pygame.init()

# RGB contant
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)

# make these to be divisable by the tiles easily
WIDTH,HEIGHT = 800,800
TILE_SIZE = 20
GRID_WIDTH = WIDTH// TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

#initilize the pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):
    # positions-  in the grid not pixels so need to translate those to pixels to draw
    for position in positions:
        col,row = position         # decomposing to positions
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (top_left, (TILE_SIZE, TILE_SIZE)))

    # draw the grid lines
    for row in range(GRID_HEIGHT):
        # y is increasing going down the rows
        pygame.draw.line(screen, "BLACK",(0 , row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        # y is increasing going down the rows
        pygame.draw.line(screen, "BLACK", (col * TILE_SIZE, 0 ), (col * TILE_SIZE, HEIGHT))



def main():
    running = True

    positions = set()
    positions.add((10,10))
    while running:
        clock.tick(FPS)                           # when active, the loop run at max 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:         # IF USER EXIT THE WINDOW
                running = False
        screen.fill(GREY)                         # bg color
        draw_grid(positions)                      # rendering in order so bg before gridline, or bg will voer it
        pygame.display.update()                   # update the screen after the changes.or redrawing

    pygame.quit()

if __name__ == "__main__":
    main()