import pygame, constants
class Part:
    def __init__(self, color, x=0, y=0, direction=constants.RIGHT):
        self.direction=direction
        self.image=pygame.surface.Surface((constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        self.image.fill(color)
        self.rect=self.image.get_rect().move(x,y)
    def change_direction(self, direction):
        self.direction=direction
    def move(self):
        if self.direction==constants.UP:
            self.rect=self.rect.move(0, -constants.BLOCK_SIZE)
        if self.direction==constants.DOWN:
            self.rect=self.rect.move(0, constants.BLOCK_SIZE)
        if self.direction==constants.LEFT:
            self.rect=self.rect.move(-constants.BLOCK_SIZE, 0)
        if self.direction==constants.RIGHT:
            self.rect=self.rect.move(constants.BLOCK_SIZE, 0)
            