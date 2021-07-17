import pygame as pg
import random

from .Entity import Entity

class Ball(Entity):
    speed_x = 0.4
    speed_y = 0.4

    def __init__(self, game):
        self.game_ = game
        self.game_.set_sounds()
        self.sounds = self.game_.get_sounds()
        
        self.width, self.height = self.game_.get_screen_dimentions()
        size = self.game_.get_ball_size()

        self.body = pg.Rect(self.width/2 - size/2, self.height/2 - size/2, size, size)

    def update(self, dt):
        self.body.x = self.body.x + self.speed_x * dt
        self.body.y = self.body.y + self.speed_y * dt
        if self.body.bottom >= self.height or self.body.top <= 0:
            self.speed_y *= -1
            self.sounds[0].play()
        if self.body.left >= self.width:
            self.game_.opponent_point()
        if self.body.right <= 0:
            self.game_.player_point()

    def reset_ball(self):
        self.body.center = (self.width/2, self.height/2)
        self.speed_x = random.choice((-0.5, 0.5))
        self.speed_y = random.choice((-0.5, 0.5))