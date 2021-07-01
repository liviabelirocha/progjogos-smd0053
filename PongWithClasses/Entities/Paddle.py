import pygame as pg
from .Entity import Entity

class Paddle(Entity):
    def __init__(self, ball, position_x, position_y, paddle_width, paddle_height):
        self._ball = ball
        self.body = pg.Rect(position_x, position_y, paddle_width, paddle_height)

    def update(self, dt):
        pass