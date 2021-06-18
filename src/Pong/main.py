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

BALL_SPEED_X = 0.5
BALL_SPEED_Y = 0.5

OPPONENT_SPEED = 5

RGB_GRAY = (200, 200, 200)
RGB_BLACK = (0, 0, 0)

FPS = 60
MS_PER_UPDATE = 1000 / FPS

GAME_STATE = 'start'
WIN = False

PLAYER_POINTS = 0
OPPONENT_POINTS = 0

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

# Sounds
snd_wall_hit = set_sound('assets/wall_hit.wav')
snd_paddle_hit = set_sound('assets/paddle_hit.wav')
snd_score = set_sound('assets/score.wav')

# Font
font = pg.font.SysFont('Fira Code', 30)

def reset_ball():
    global BALL_SPEED_X, GLOBAL_SPEED_Y, OPPONENT_SPEED

    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    BALL_SPEED_X = random.choice((-0.5, 0.5))
    BALL_SPEED_Y = random.choice((-0.5, 0.5))
    OPPONENT_SPEED = 5


def hit_paddle(paddle):
    global BALL_SPEED_X, BALL_SPEED_Y

    delta = ball.centery - paddle.centery
    BALL_SPEED_Y = delta * 0.005
    BALL_SPEED_X *= -1.03
    snd_paddle_hit.play()


def inputs():
    global GAME_STATE, PLAYER_POINTS, OPPONENT_POINTS

    for event in pg.event.get():
        # Close game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if GAME_STATE == 'start' or GAME_STATE == 'end':
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    GAME_STATE = 'serve'
                    PLAYER_POINTS = OPPONENT_POINTS = 0


        if GAME_STATE == 'serve':
            if event.type == pg.MOUSEBUTTONUP:
                reset_ball()
                GAME_STATE = 'play'

    # Get mouse position
    if GAME_STATE == 'play':
        (mouse_x, mouse_y) = pg.mouse.get_pos()
        player.centery = mouse_y


def update(dt):
    global BALL_SPEED_X, BALL_SPEED_Y, OPPONENT_SPEED, SCREEN_HEIGHT, GAME_STATE, PLAYER_POINTS, OPPONENT_POINTS, WIN

    if GAME_STATE == 'play':
        # Move opponent
        if opponent.bottom < ball.y:
            opponent.bottom += OPPONENT_SPEED
        elif opponent.top > ball.y:
            opponent.top -= OPPONENT_SPEED

        ball.x = ball.x + BALL_SPEED_X * dt
        ball.y = ball.y + BALL_SPEED_Y * dt

        # Hit wall
        if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0 :
            BALL_SPEED_Y *= -1
            snd_wall_hit.play()

        # Collisions
        if ball.bottom >= opponent.top and ball.top <=opponent.bottom and ball.left <= opponent.right:
            if BALL_SPEED_X < 0:
                hit_paddle(opponent)
                OPPONENT_SPEED *= 1.03

        if ball.bottom >= player.top and ball.top <= player.bottom and ball.right >= player.left:
            if BALL_SPEED_X > 0:
                hit_paddle(player)

        # Opponent point
        if ball.left >= SCREEN_WIDTH:
            OPPONENT_POINTS += 1
            snd_score.play()

            if OPPONENT_POINTS == 7:
                GAME_STATE = 'end'
                WIN = False
                return
            GAME_STATE = 'serve'

        # Player point
        if ball.right <= 0:
            PLAYER_POINTS += 1
            snd_score.play()
            if PLAYER_POINTS == 7:
                GAME_STATE = 'end'
                WIN = True
                return
            GAME_STATE = 'serve'


def draw():
    # Drawing objects
    screen.fill(RGB_BLACK)

    pg.draw.ellipse(screen, RGB_GRAY, ball)
    pg.draw.rect(screen, RGB_GRAY, player)
    pg.draw.rect(screen, RGB_GRAY, opponent)

    if GAME_STATE == 'start':
        start_text = font.render("Press ENTER to start", True, RGB_GRAY)
        text_rect = start_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60))
        screen.blit(start_text, text_rect)

    else:
        player_points = font.render(f'{PLAYER_POINTS} POINTS', True, RGB_GRAY)
        opponent_points = font.render(f'{OPPONENT_POINTS} POINTS', True, RGB_GRAY)

        screen.blit(player_points, (SCREEN_WIDTH - 120, 20))
        screen.blit(opponent_points, (10, 20))

    if GAME_STATE == 'serve':
        serve_text = font.render("Press the mouse button to serve", True, RGB_GRAY)
        text_rect = serve_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60))
        screen.blit(serve_text, text_rect)

    elif GAME_STATE == 'end':
        text = 'VICTORY !'if WIN else 'DEFEAT !'
        end_text = font.render(text, True, RGB_GRAY)
        text_rect = end_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60))

        restart_text = font.render("Press ENTER to start again", True, RGB_GRAY)
        retext_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20))

        screen.blit(end_text, text_rect)
        screen.blit(restart_text, retext_rect)

    # Updating window
    pg.display.flip()


#Game Loop

previous = pg.time.get_ticks()
dt = 0

while True:
    current = pg.time.get_ticks()
    if current >= previous + MS_PER_UPDATE:
        dt += current - previous
        previous = current

        inputs()

        while dt >= MS_PER_UPDATE:
            update(dt)
            dt = dt - MS_PER_UPDATE

        draw()
