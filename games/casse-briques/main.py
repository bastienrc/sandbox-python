import pygame

config = {
    "screen_width":  600,
    "screen_height": 600
}


pygame.init()
pygame.display.set_caption("Casse Briques Alpha-0.0.1")
screen = pygame.display.set_mode(
    [config["screen_width"], config["screen_height"]])
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.display.flip()

pygame.quit()
