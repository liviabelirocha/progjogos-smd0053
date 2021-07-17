import pygame as pg
from .Paddle import Paddle

class Player(Paddle):
    def update(self, dt):
        if self.ball_.body.bottom >= self.body.top and self.ball_.body.top <= self.body.bottom and self.ball_.body.right >= self.body.left:
            self.hit_paddle()
        (x, y) = pg.mouse.get_pos()
        self.body.y = y - 70