import pygame
import constants


class Food(pygame.sprite.Sprite):
    def __init__(self, color=pygame.color.Color(0,0,255), x=0, y=0, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.color = color
        self.image = pygame.surface.Surface((constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect().move(x,y)

