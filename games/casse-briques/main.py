import pygame
import os
from math import cos, sin, radians

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750

RACKET_WIDTH = 80
RACKET_HEIGHT = 10
RACKET_STEP_MOVE = 25
RACKET_ALTITUDE = 150

BALL_DIAMETER = 20
BALL_STEP_MOVE = 20

SHOOTING_ANGLE = 50

BRICK_WIDTH = 50
BRICK_HEIGHT = 25
BRICK_GAP = 20
BRICK_MARGIN = 20
BRICK_PER_ROW = 11
BRICK_PER_COLUMN = 4

LIFE_NUMBER_START = 3

game_over = False

pygame.font.init()
POLICE = pygame.font.Font(
    f'{os.path.dirname(__file__)}/assets/zorque.regular.otf',
    42
)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface([BALL_DIAMETER, BALL_DIAMETER])
        # self.surf.fill((255, 0, 0))
        self.surf = pygame.image.load(
            f'{os.path.dirname(__file__)}/assets/ball.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.life_number = LIFE_NUMBER_START
        self.moving_x = BALL_STEP_MOVE * cos(radians(SHOOTING_ANGLE))
        self.moving_y = - BALL_STEP_MOVE * sin(radians(SHOOTING_ANGLE))
        self.init_position()

    def init_position(self):
        self.stick = True
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
            self.life_number -= 1
            self.init_position()

    def bounce_racket(self):
        self.moving_y = - self.moving_y

    def inverse_x(self):
        self.moving_x = - self.moving_x

    def inverse_y(self):
        self.moving_y = - self.moving_y

    def reset(self):
        self.init_position()
        self.life_number = LIFE_NUMBER_START


class Racket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface([RACKET_WIDTH, RACKET_HEIGHT])
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = SCREEN_WIDTH / 2 - RACKET_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - 2 * RACKET_HEIGHT - RACKET_ALTITUDE

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(- RACKET_STEP_MOVE, 0)
            if my_ball.stick:
                my_ball.rect.move_ip(- RACKET_STEP_MOVE, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(RACKET_STEP_MOVE, 0)
            if my_ball.stick:
                my_ball.rect.move_ip(RACKET_STEP_MOVE, 0)
        if self.rect.left < 0:
            self.rect.left = 0
            if my_ball.stick:
                my_ball.rect.left = RACKET_WIDTH / 2 - BALL_DIAMETER / 2
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            if my_ball.stick:
                my_ball.rect.right = SCREEN_WIDTH - RACKET_WIDTH / 2 + BALL_DIAMETER / 2


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # self.surf = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        # self.surf.fill((0, 0, 255))
        self.surf = pygame.image.load(
            f'{os.path.dirname(__file__)}/assets/brick.png').convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def init_brick_wall():
        y = BRICK_MARGIN
        for j in range(BRICK_PER_COLUMN):
            x = BRICK_MARGIN
            for i in range(BRICK_PER_ROW):
                brick = Brick(x, y)
                all_sprites.add(brick)
                brick_group.add(brick)
                x = BRICK_MARGIN + (BRICK_WIDTH + BRICK_GAP) * (i+1)
            y = BRICK_MARGIN + (BRICK_HEIGHT + BRICK_GAP) * (j+1)

    @staticmethod
    def reset():
        for brick in brick_group:
            brick.kill()
        Brick.init_brick_wall()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.scoreCurrent = 0
        self._setText()

    def _setText(self):
        self.surf = POLICE.render(
            f"Score : {self.scoreCurrent}", True, (150, 150, 150))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH - 200, SCREEN_HEIGHT - RACKET_ALTITUDE / 2))

    def reset(self):
        self.scoreCurrent = 0

    def update(self, pressed_keys):
        self._setText()

    def increment(self, value):
        self.scoreCurrent += value


class LivesRemaining(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._setText()

    def _setText(self):
        self.surf = POLICE.render(
            f"Vies : {my_ball.life_number}", True, (150, 150, 150)
        )
        self.rect = self.surf.get_rect(
            center=(200, SCREEN_HEIGHT - RACKET_ALTITUDE / 2)
        )

    def update(self, pressed_keys):
        self._setText()


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._setText()

    def _setText(self):
        self.surf = POLICE.render("GAME OVER", True, (150, 150, 150))
        self.surf = POLICE.render("(S pour recommencer)", True, (150, 150, 150))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

    def update(self, pressed_keys):
        self._setText()


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

my_score = Score()
all_sprites.add(my_score)

text_game_over = GameOver()

all_sprites.add(LivesRemaining())

brick_group = pygame.sprite.Group()
Brick.init_brick_wall()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((42, 42, 42))

    if pygame.sprite.spritecollideany(my_ball, group_racket):
        my_ball.bounce_racket()

    bricks_destroy = pygame.sprite.spritecollide(my_ball, brick_group, True)
    for brick in bricks_destroy:
        my_score.increment(10)
        relative_x = my_ball.rect.x - brick.rect.x
        relative_y = my_ball.rect.y - brick.rect.y
        if relative_x > 0 and relative_y > 0:
            my_ball.inverse_y()
        if relative_x > 0 > relative_y:
            my_ball. inverse_y()
        if relative_x < 0 < relative_y:
            my_ball.inverse_x()
        if relative_x > 0 > relative_y:
            my_ball.inverse_x()

    keys = pygame.key.get_pressed()

    if my_ball.life_number <=0:
        game_over = True

    if not game_over:
        for my_sprite in all_sprites:
            my_sprite.update(keys)
    else:
        all_sprites.add(text_game_over)

    if game_over and keys[pygame.K_s]:
        game_over = False
        my_ball.reset()
        my_score.reset()
        Brick.reset()
        text_game_over.kill()
        text_game_over = GameOver()

    for my_sprite in all_sprites:
        screen.blit(my_sprite.surf, my_sprite.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
