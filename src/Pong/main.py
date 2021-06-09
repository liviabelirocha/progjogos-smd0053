import sys
import os
import random

import pygame as pg

from sounds import set_sound

# Variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BALL_SIZE = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140

BALL_SPEED_X = 0.3
BALL_SPEED_Y = 0.3

OPPONENT_SPEED = 5

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
snd_paddle_hit = set_sound('assets/paddle_hit.wav')

def reset_ball():
    global BALL_SPEED_X

    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    BALL_SPEED_X = random.choice((-0.5, 0.5))
    BALL_SPEED_Y = random.choice((-0.5, 0.5))

def hit_paddle(paddle):
    global BALL_SPEED_X, BALL_SPEED_Y

    delta = ball.centery - paddle.centery
    BALL_SPEED_Y = delta * 0.005
    BALL_SPEED_X *= -1.03
    snd_paddle_hit.play()

def inputs():
    for event in pg.event.get():
        # Close game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Get mouse position
    (mouse_x, mouse_y) = pg.mouse.get_pos()
    player.centery = mouse_y

def update():
    global BALL_SPEED_X, BALL_SPEED_Y, OPPONENT_SPEED, SCREEN_HEIGHT

    # Move opponent
    if BALL_SPEED_X < 0:
        if opponent.bottom < ball.y:
            opponent.bottom += OPPONENT_SPEED
        elif opponent.top > ball.y:
            opponent.top -= OPPONENT_SPEED

    # Update
    dt = clock.tick(60)

    ball.x = ball.x + BALL_SPEED_X * dt
    ball.y = ball.y + BALL_SPEED_Y * dt

    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0 :
        BALL_SPEED_Y *= -1
        snd_wall_hit.play()

    # Collisions
    if ball.bottom >= opponent.top and ball.top <=opponent.bottom and ball.left <= opponent.right:
        hit_paddle(opponent)
        OPPONENT_SPEED *= 1.04

    if ball.bottom >= player.top and ball.top <= player.bottom and ball.right >= player.left:
        hit_paddle(player)


    if ball.right >= SCREEN_WIDTH or ball.left <= 0:
        reset_ball()

def draw():
    # Drawing objects
    screen.fill(RGB_BLACK)
    pg.draw.ellipse(screen, RGB_GRAY, ball)
    pg.draw.rect(screen, RGB_GRAY, player)
    pg.draw.rect(screen, RGB_GRAY, opponent)

    pg.draw.aaline(screen, RGB_GRAY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # 60 FPS
    pg.display.flip()

#Game Loop
while True:
    inputs()
    update()
    draw()
