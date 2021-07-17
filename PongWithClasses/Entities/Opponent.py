from .Paddle import Paddle

class Opponent(Paddle):
    speed = 10

    def update(self, dt):
        if self.ball_.body.bottom >= self.body.top and self.ball_.body.top <= self.body.bottom and self.ball_.body.left <= self.body.right:
            self.hit_paddle()
        if self.body.bottom < self.ball_.body.y:
            self.body.bottom += self.speed
        if self.body.top > self.ball_.body.y:
            self.body.top -= self.speed