import pygame
import constants


class Food(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.rect = pygame.rect.Rect(x, y, 16, 16)

