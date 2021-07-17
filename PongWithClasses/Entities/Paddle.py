import pygame as pg
from .Entity import Entity

class Paddle(Entity):
    def __init__(self, game, ball, position_x, position_y, paddle_width, paddle_height):
        self.game_ = game
        self.game_.set_sounds()
        self.sounds = self.game_.get_sounds()
        
        self.ball_ = ball
        self.body = pg.Rect(position_x, position_y, paddle_width, paddle_height)

    def update(self, dt):
        pass

    def hit_paddle(self):
        delta = self.ball_.body.centery - self.body.centery
        self.ball_.speed_y = delta * 0.005
        self.ball_.speed_x *= -1
        self.sounds[1].play()