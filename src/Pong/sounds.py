import pygame as pg
import os
import sys

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

set_sound = lambda path: pg.mixer.Sound(os.path.join(APP_FOLDER, path))
