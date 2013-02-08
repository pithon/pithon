import pygame, constants
from Part import Part
class Snake:
    def __init__(self, screen, x=0, y=0, image='img/Part.bmp'):
        self.screen = screen
        self.image=image
        head=Part(self.image, x, y)
        self.direction=constants.RIGHT
        self.parts=pygame.sprite.OrderedUpdates(head)
        self.do_extend = False

    def change_direction(self, direction):
        if direction in constants.VALID_DIRECTIONS[self.direction]:
            self.direction=direction

    def update(self):
        new_direction=self.direction
        old_direction=None

        if self.do_extend:
            last_part = self.parts.sprites()[-1]
            new_part = Part(self.image, last_part.rect.x, last_part.rect.y, last_part.direction)


        for part in self.parts.sprites():
            old_direction=part.direction
            part.change_direction(new_direction)
            part.move()
            new_direction=old_direction

        if self.do_extend:
            self.parts.add(new_part)
            self.do_extend = False

    def extend(self):
        last_part = self.parts.sprites()[-1]
        part = Part(self.image, last_part.rect.x, last_part.rect.y, last_part.direction)
        self.parts.add(part)

