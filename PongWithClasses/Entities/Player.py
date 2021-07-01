import pygame as pg
from .Paddle import Paddle

class Player(Paddle):
    def update(self, dt):
        if self._ball.body.bottom >= self.body.top and self._ball.body.top <= self.body.bottom and self._ball.body.right >= self.body.left:
            delta = self._ball.body.centery - self.body.centery
            self._ball.speed_y = delta * 0.005
            self._ball.speed_x = self._ball.speed_x * -1
        (x, y) = pg.mouse.get_pos()
        self.body.y = y - 70