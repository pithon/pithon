import pygame, constants

class Tail(pygame.sprite.Sprite):
    def __init__(self, color, player, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        surface=pygame.surface.Surface((constants.BLOCK_SIZE,constants.BLOCK_SIZE))
        self.rect=pygame.rect.Rect(x,y,constants.BLOCK_SIZE,constants.BLOCK_SIZE)
        surface.fill(color)
        self.image=surface.convert()
        self.player=player
        self.direction=direction
    def update(self):
        if self.direction==constants.UP:
            self.rect.y -= constants.BLOCK_SIZE
        if self.direction==constants.DOWN:
            self.rect.y += constants.BLOCK_SIZE
        if self.direction==constants.LEFT:
            self.rect.x -= constants.BLOCK_SIZE
        if self.direction==constants.RIGHT:
            self.rect.x += constants.BLOCK_SIZE