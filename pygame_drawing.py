# Wildlife survival
# Author: Justin L
# Date:

import pygame


def game():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, (WIDTH / 2 - 440, HEIGHT / 2 + 200, 1000, 300))

        pygame.display.flip()

        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
