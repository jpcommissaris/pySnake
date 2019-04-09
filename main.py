import pygame
from board import Board

b = Board()
pygame.init()

# set screen

size = b.getSize()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# --- game loop ---
WAIT = 5 # determines speed of game
done = False
while not done:
    # --- Events loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- scene logic ---
    b.setDirection()

    # --- repaints screen ---
    if WAIT > 5:
        screen.fill((255,255,255))
        b.drawBoard(screen)
        wait = 0
    WAIT += 1
    # Updates screen with new drawings
    pygame.display.flip()

    # number of frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()