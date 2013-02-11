import pygame, constants
class Part(pygame.sprite.Sprite):
    def __init__(self, color, x=0, y=0, direction=constants.RIGHT, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.direction=direction
        self.rect=pygame.rect.Rect(x,y,constants.BLOCK_SIZE, constants.BLOCK_SIZE)

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

