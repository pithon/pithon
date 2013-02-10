import pygame, constants
from Part import Part
class Snake:
    def __init__(self, name, x=0, y=0, image='core2/img/Part.bmp'):
        self.name=name
        self.image=image
        head=Part(self.image, x, y)
        self.direction=constants.RIGHT
        self.parts=pygame.sprite.OrderedUpdates(head)
        self.do_extend = False
        self.hit_border = False

    def change_direction(self, direction):
        if direction in constants.VALID_DIRECTIONS[self.direction]:
            self.direction=direction

    def update(self):
        new_direction=self.direction
        old_direction=None

        if self.do_extend:
            last_part = self.parts.sprites()[-1]
            new_part = Part(self.image, last_part.rect.x, last_part.rect.y, last_part.direction)


        x, y  = self.parts.sprites()[0].rect.x, self.parts.sprites()[0].rect.y

        if y < 0:
            self.hit_border = True
        elif y + constants.BLOCK_SIZE > constants.SCREEN_HEIGHT:
            self.hit_border = True
        elif x < 0:
            self.hit_border = True
        elif x + constants.BLOCK_SIZE > constants.SCREEN_WIDTH:
            self.hit_border = True

        if self.hit_border:
            return

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

