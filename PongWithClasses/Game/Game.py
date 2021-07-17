import pygame as pg
import os
import sys

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

class Game():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720

        self.paddle_width = 10
        self.paddle_height = 140

        self.ball_size = 30

        self.win = False
        self.game_state = 'start'

        self.player_points = 0
        self.opponent_points = 0

        self.sounds = []
    
    # Getters
    def get_screen_dimentions(self):
        return (self.screen_width, self.screen_height)

    def get_ball_size(self):
        return self.ball_size

    def get_paddle_dimentions(self):
        return (self.paddle_width, self.paddle_height)

    def get_sounds(self):
        return self.sounds

    def get_game_state(self):
        return self.game_state

    def get_player_points(self):
        return self.player_points

    def get_opponent_points(self):
        return self.opponent_points

    def get_win(self):
        return self.win

    def set_sound(self, path):
        return pg.mixer.Sound(os.path.join(APP_FOLDER, path))

    def set_sounds(self):
        snd_wall_hit = self.set_sound('assets/wall_hit.wav')
        snd_paddle_hit = self.set_sound('assets/paddle_hit.wav')
        snd_score = self.set_sound('assets/score.wav')

        self.sounds.append(snd_wall_hit)
        self.sounds.append(snd_paddle_hit)
        self.sounds.append(snd_score)

    def set_game_state(self, state):
        self.game_state = state

    def opponent_point(self):
        self.opponent_points += 1
        self.sounds[2].play()

        if self.opponent_points == 7:
            self.set_game_state('end')
            self.win = False
            return
        self.set_game_state('serve')

    def player_point(self):
        self.player_points += 1
        self.sounds[2].play()

        if self.player_points == 7:
            self.set_game_state('end')
            self.win = True
            return
        self.set_game_state('serve')

    