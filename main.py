import pygame
from board import Board

b = Board()
pygame.init()

# set screen

size = b.getSize()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

frame = 0


# --- game loop ---
SPEED = 15
done = False
while not done:
    # --- Events loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- scene logic ---
    frame += 1
    b.setDirection()

    # --- repaints screen ---

    screen.fill((255,255,255))
    b.drawBoard(screen)
    b.drawScores(screen)

    # Updates screen with new drawings
    pygame.display.flip()

    # number of frames per second
    clock.tick(SPEED)
    b.won = 0

# Close the window and quit.
pygame.quit()