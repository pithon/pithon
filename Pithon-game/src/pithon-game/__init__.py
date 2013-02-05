import pygame, time, core2.constants
from core2.Snake import Snake
from core2.Part import Part

pygame.init()
pygame.display.set_caption("Pithon")
screen=pygame.display.set_mode((800,600)) 

snake=Snake()

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(core2.constants.UP)
            if event.key == pygame.K_DOWN:
                snake.change_direction(core2.constants.DOWN)
            if event.key == pygame.K_LEFT:
                snake.change_direction(core2.constants.LEFT)
            if event.key == pygame.K_RIGHT:
                snake.change_direction(core2.constants.RIGHT)
            if event.key == pygame.K_SPACE:
                snake.do_extend=True
    screen.fill((0,0,0))
    snake.move()
    snake.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)