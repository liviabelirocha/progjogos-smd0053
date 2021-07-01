import pygame as pg
import sys

from Constants import constants as c

from Entities.Ball import Ball
from Entities.Player import Player
from Entities.Opponent import Opponent

SCREEN_WIDTH = c.SCREEN_WIDTH
SCREEN_HEIGHT = c.SCREEN_HEIGHT

BALL_SIZE = 30
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 140

RGB_GRAY = (200, 200, 200)
RGB_BLACK = (0, 0, 0)

GAME_STATE = 'start'
WIN = False

PLAYER_POINTS = 0
OPPONENT_POINTS = 0

pg.init()

# Window
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Pong')

ball = Ball(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE)
player = Player(ball, SCREEN_WIDTH - PADDLE_WIDTH * 2, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = Opponent(ball, PADDLE_WIDTH, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

entities = []
entities.append(ball)
entities.append(player)
entities.append(opponent)

def inputs():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

def draw():
    screen.fill(RGB_BLACK)
    pg.draw.ellipse(screen, RGB_GRAY, ball.body)
    pg.draw.rect(screen, RGB_GRAY, player.body)
    pg.draw.rect(screen, RGB_GRAY, opponent.body)
    pg.display.flip()

previous = pg.time.get_ticks()
FPS = 120
MS_PER_UPDATE = 1000 / FPS
lag = 0
while True:
    current = pg.time.get_ticks()
    elapsed = current - previous
    previous = current
    lag += elapsed
    inputs()
    while lag >= MS_PER_UPDATE:
        for e in entities:
            e.update(MS_PER_UPDATE)
        lag -= MS_PER_UPDATE
    draw()
