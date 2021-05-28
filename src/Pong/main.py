import pygame as pg
import sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

BALL_SIZE = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140

RGB_GRAY = (200, 200, 200)

# Instanciating Pygame
pg.init()
clock = pg.time.Clock()

# Window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Pong')

# Objects
ball = pg.Rect(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)
player = pg.Rect(SCREEN_WIDTH - PADDLE_WIDTH * 2, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pg.Rect(PADDLE_WIDTH, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

#Game Loop
while True:
    for event in pg.event.get():
        # Close game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Drawing objects
    pg.draw.rect(screen, RGB_GRAY, ball)
    pg.draw.rect(screen, RGB_GRAY, player)
    pg.draw.rect(screen, RGB_GRAY, opponent)

    # 60 FPS
    pg.display.flip()
    clock.tick(60)