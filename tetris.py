from values import *
import math

class Tetris:
    def __init__(self, app):
        self.app = app

    def draw_grid(self):
        for x in range(FieldW):
            for y in range(FieldH):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TileSize, y * TileSize, TileSize), 1)
                
    def update(self):
        pass

    def draw(self):
        self.draw_grid()