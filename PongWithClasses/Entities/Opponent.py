from .Paddle import Paddle

class Opponent(Paddle):
    speed = 10

    def update(self, dt):
        if self._ball.body.bottom >= self.body.top and self._ball.body.top <= self.body.bottom and self._ball.body.left <= self.body.right:
            delta = self._ball.body.centery - self.body.centery
            self._ball.speed_y = delta * 0.005
            self._ball.speed_x *= -1
        if self.body.bottom < self._ball.body.y:
            self.body.bottom += self.speed
        if self.body.top > self._ball.body.y:
            self.body.top -= self.speed