import pygame, constants
from Tail import Tail

class Player(object):
    def __init__(self, color):
        self.tail=[]
        head=Tail(pygame.color.Color(255,255,255), self, 116,100, constants.RIGHT)
        self.tail.append(head)
        self.color=color
        self.direction=constants.RIGHT
        self.extend=True
    def add_tail(self):
        self.extend=True
    def update_tail(self, direction):
        save_direction=direction
        for i in self.tail:
            save_direction=i.direction
            i.direction=direction
            direction=save_direction
            i.update()
        if self.extend:
            last_part = self.tail[-1]
            new_part = Tail(self.color, self, last_part.rect.x, last_part.rect.y, last_part.direction)
            self.tail.append(new_part)
            self.extend=False
    def render_tail(self, screen):
        for i in self.tail:
            screen.blit(i.image, i.rect)