import pygame
from math import cos, sin, radians


SCREEN_WIDTH     = 600
SCREEN_HEIGHT    = 600
RACKET_WIDTH     = 80
RACKET_HEIGHT    = 10
STEP_MOVE_RACKET = 25
BALL_DIAMETER    = 20
STEP_MOVE_BALL   = 20
SHOOTING_ANGLE   = 50


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface([BALL_DIAMETER, BALL_DIAMETER])
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.stick = True
        self.moving_x = STEP_MOVE_BALL * cos(radians(SHOOTING_ANGLE))
        self.moving_y = - STEP_MOVE_BALL * sin(radians(SHOOTING_ANGLE))
        self.init_position()

    def init_position(self):
        self.rect.x = my_racket.rect.x + RACKET_WIDTH / 2 - BALL_DIAMETER / 2
        self.rect.y = my_racket.rect.y - RACKET_HEIGHT * 2

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_SPACE]:
            self.stick = False
        if not self.stick:
            self.rect.x += self.moving_x
            self.rect.y += self.moving_y
        if self.rect.y < 0:
            self.moving_y = - self.moving_y
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - BALL_DIAMETER / 2:
            self.moving_x = - self.moving_x
        if self.rect.y > SCREEN_HEIGHT:
            self.init_position()

    def bounce_racket(self):
        self.moving_y = - self.moving_y


class Racket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface([RACKET_WIDTH, RACKET_HEIGHT])
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = SCREEN_WIDTH / 2 - RACKET_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - 2 * RACKET_HEIGHT

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(- STEP_MOVE_RACKET, 0)
            if my_ball.stick:
                my_ball.rect.move_ip(- STEP_MOVE_RACKET, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(STEP_MOVE_RACKET, 0)
            if my_ball.stick:
                my_ball.rect.move_ip(STEP_MOVE_RACKET, 0)
        if self.rect.left < 0:
            self.rect.left = 0
            if my_ball.stick:
                my_ball.rect.left = RACKET_WIDTH / 2 - BALL_DIAMETER / 2
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            if my_ball.stick:
                my_ball.rect.right = SCREEN_WIDTH - RACKET_WIDTH / 2 + BALL_DIAMETER / 2


pygame.init()
pygame.display.set_caption("Casse Briques Alpha-0.0.1")
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
my_racket = Racket()
group_racket = pygame.sprite.Group()
group_racket.add(my_racket)
all_sprites.add(my_racket)

my_ball = Ball()
all_sprites.add(my_ball)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    if pygame.sprite.spritecollideany(my_ball, group_racket):
        my_ball.bounce_racket()

    keys = pygame.key.get_pressed()

    for my_sprite in all_sprites:
        my_sprite.update(keys)

    for my_sprite in all_sprites:
        screen.blit(my_sprite.surf, my_sprite.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
