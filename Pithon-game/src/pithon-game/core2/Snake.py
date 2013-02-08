import pygame, constants
from Part import Part
class Snake:
    def __init__(self, name, x=0, y=0, color=pygame.color.Color(0,255,0)):
        self.color=color
        self.name=name
        head=Part(self.color, x, y)
        self.direction=constants.RIGHT
        self.parts=[head]
        self.do_extend=False
    
    def change_direction(self, direction):
        self.direction=direction
    
    def move(self):
        new_direction=self.direction
        old_direction=None
        new_part=None
        
        if self.do_extend:
            last_part=self.parts[-1]
            new_part = Part(self.color,last_part.rect.x, last_part.rect.y, last_part.direction)
        
        for part in self.parts:
            old_direction=part.direction
            part.change_direction(new_direction)
            part.move()
            new_direction=old_direction
        
        if self.do_extend:
            self.extend(new_part)
    
    def extend(self, part):
        self.parts.append(part)
        self.do_extend=False
    
    def draw(self, screen):
        for part in self.parts:
            screen.blit(part.image, part.rect)