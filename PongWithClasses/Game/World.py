import sys
import pygame as pg

from Entities.Ball import Ball
from Entities.Player import Player
from Entities.Opponent import Opponent
from .Game import Game

class World():
    def __init__(self):
        self.game_ = Game()
        self.screen_width, self.screen_height = self.game_.get_screen_dimentions()

        self.rgb_gray = (200, 200, 200)
        self.rgb_black = (0, 0, 0)

        self.entities = []

        self.start()

    def set_fonts(self):
        self.font = pg.font.SysFont('Fira Code', 30)

    # Game Setup
    def start(self):
        pg.init()
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption('Pong')

        self.instanciate_objects()
        self.set_fonts()

        self.game_loop()

    def instanciate_objects(self):
        swidth, sheight = self.game_.get_screen_dimentions()
        pwidth, pheight = self.game_.get_paddle_dimentions()

        self.ball_ = Ball(self.game_)
        self.player_ = Player(self.game_, self.ball_, swidth - pwidth * 2, sheight/2 - pheight/2, pwidth, pheight)
        self.opponent_ = Opponent(self.game_, self.ball_, pwidth, sheight/2 - pheight/2, pwidth, pheight)

        self.entities.append(self.ball_)
        self.entities.append(self.player_)
        self.entities.append(self.opponent_)

    def draw(self):
        screen = self.screen
        gray = self.rgb_gray

        width, height = self.game_.get_screen_dimentions()

        screen.fill(self.rgb_black)
        pg.draw.ellipse(screen, gray, self.ball_.body)
        pg.draw.rect(screen, gray, self.player_.body)
        pg.draw.rect(screen, gray, self.opponent_.body)


        if self.game_.get_game_state() == 'start':
            start_text = self.font.render("Press ENTER to start", True, gray)
            text_rect = start_text.get_rect(center=(width/2, height/2 - 60))
            screen.blit(start_text, text_rect)

        else:
            player_points = self.font.render(f'{self.game_.get_player_points()} POINTS', True, gray)
            opponent_points = self.font.render(f'{self.game_.get_opponent_points()} POINTS', True, gray)

            screen.blit(player_points, (width - 120, 20))
            screen.blit(opponent_points, (30, 20))

        if self.game_.get_game_state() == 'serve':
            serve_text = self.font.render("Press the mouse button to serve", True, gray)
            text_rect = serve_text.get_rect(center=(width/2, height/2 - 60))
            screen.blit(serve_text, text_rect)

        elif self.game_.get_game_state() == 'end':
            text = 'VICTORY !'if self.game_.get_win() else 'DEFEAT !'
            end_text = self.font.render(text, True, gray)
            text_rect = end_text.get_rect(center=(width/2, height/2 - 60))

            restart_text = self.font.render("Press ENTER to start again", True, gray)
            retext_rect = restart_text.get_rect(center=(width/2, height/2 - 20))

            screen.blit(end_text, text_rect)
            screen.blit(restart_text, retext_rect)

        pg.display.flip()

    def inputs(self):
        for event in pg.event.get():
            # Close game
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if self.game_.get_game_state() == 'start' or self.game_.get_game_state() == 'end':
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.game_.set_game_state('serve') 
                        self.player_points = self.opponent_points = 0

            if self.game_.get_game_state() == 'serve':
                if event.type == pg.MOUSEBUTTONUP:
                    self.ball_.reset_ball()
                    self.game_.set_game_state('play') 

        # Get mouse position
        if self.game_.get_game_state() == 'play':
            (mouse_x, mouse_y) = pg.mouse.get_pos()
            self.player_.centery = mouse_y

    def game_loop(self):
        previous = pg.time.get_ticks()
        FPS = 120
        MS_PER_UPDATE = 1000 / FPS
        lag = 0

        while True:
            current = pg.time.get_ticks()
            elapsed = current - previous
            previous = current
            lag += elapsed
            self.inputs()
            while lag >= MS_PER_UPDATE:
                if self.game_.get_game_state() == 'play':
                    for e in self.entities:
                        e.update(MS_PER_UPDATE)
                lag -= MS_PER_UPDATE
            self.draw()