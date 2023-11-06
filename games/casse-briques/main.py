import pygame

config = {
    "screen_width":  600,
    "screen_height": 600,
    "racket_width":   80,
    "racket_height":  10,
    "step_move_racket": 25,
    "ball_diameter": 20
}


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(
            [config["ball_diameter"], config["ball_diameter"]])
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.stick = True
        self.init_position()

    def init_position(self):
        self.rect.x = my_racket.rect.x + \
            config["racket_width"] / 2 - config["ball_diameter"] / 2
        self.rect.y = my_racket.rect.y - config["racket_height"] * 2


class Racket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(
            [config["racket_width"], config["racket_height"]])
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = config["screen_width"] / 2 - config["racket_width"] / 2
        self.rect.y = config["screen_height"] - 2 * config["racket_height"]

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(- config["step_move_racket"], 0)
            if my_ball.stick:
                my_ball.rect.move_ip(- config["step_move_racket"], 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(config["step_move_racket"], 0)
            if my_ball.stick:
                my_ball.rect.move_ip(config["step_move_racket"], 0)
        if self.rect.left < 0:
            self.rect.left = 0
            if my_ball.stick:
                my_ball.rect.left = config["racket_width"] / 2 - config["ball_diameter"] / 2
        if self.rect.right > config["screen_width"]:
            self.rect.right = config["screen_width"]
            if my_ball.stick:
                my_ball.rect.right = config["screen_width"] - config["racket_width"] / 2 + config["ball_diameter"] / 2


pygame.init()
pygame.display.set_caption("Casse Briques Alpha-0.0.1")
screen = pygame.display.set_mode(
    [config["screen_width"], config["screen_height"]])
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
my_racket = Racket()
all_sprites.add(my_racket)

my_ball = Ball()
all_sprites.add(my_ball)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()

    for my_sprite in all_sprites:
        my_sprite.update(keys)

    for my_sprite in all_sprites:
        screen.blit(my_sprite.surf, my_sprite.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
