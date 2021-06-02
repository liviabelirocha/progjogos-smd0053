import pygame as pg
import sys
import os

from sounds import set_sound

# Variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BALL_SIZE = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140

BALL_SPEED_X = 0.3
BALL_SPEED_Y = 0.3

RGB_GRAY = (200, 200, 200)
RGB_BLACK = (0, 0, 0)

# Instanciating Pygame
pg.init()
pg.mixer.init()
clock = pg.time.Clock()

# Window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Pong')

# Objects
ball = pg.Rect(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)
player = pg.Rect(SCREEN_WIDTH - PADDLE_WIDTH * 2, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pg.Rect(PADDLE_WIDTH, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

#Sounds
snd_wall_hit = set_sound('assets/wall_hit.wav')

#Game Loop
while True:
    for event in pg.event.get():
        # Close game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Update
    dt = clock.tick(60)

    ball.x = ball.x + BALL_SPEED_X * dt
    ball.y = ball.y + BALL_SPEED_Y * dt

    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0 :
        BALL_SPEED_Y *= -1
        snd_wall_hit.play()

    # Drawing objects
    screen.fill(RGB_BLACK)
    pg.draw.ellipse(screen, RGB_GRAY, ball)
    pg.draw.rect(screen, RGB_GRAY, player)
    pg.draw.rect(screen, RGB_GRAY, opponent)

    pg.draw.aaline(screen, RGB_GRAY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # 60 FPS
    pg.display.flip()
