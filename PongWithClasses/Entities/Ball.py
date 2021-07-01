import sys
import pygame as pg
import random

sys.path.append("..") 

from .Entity import Entity
from Constants import constants as c

width = c.SCREEN_WIDTH
height = c.SCREEN_HEIGHT

class Ball(Entity):
    speed_x = 0.4
    speed_y = 0.4

    def __init__(self, position_x, position_y, size):
        self.body = pg.Rect(position_x, position_y, size, size)

    def update(self, dt):
        self.body.x = self.body.x + self.speed_x * dt
        self.body.y = self.body.y + self.speed_y * dt
        if self.body.bottom >= height or self.body.top <= 0:
            self.speed_y *= -1
        if self.body.right >= width or self.body.left <= 0:
            self.reset_ball()

    def reset_ball(self):
        self.body.center = (width/2, height/2)
        self.speed_x = random.choice((-0.5, 0.5))
        self.speed_y = random.choice((-0.5, 0.5))