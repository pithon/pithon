import pygame, time, core2.constants
from core2.Snake import Snake
from core2.Part import Part
from core2.Food import Food
import random

pygame.init()
pygame.display.set_caption("Pithon")
screen=pygame.display.set_mode((800,600))

snake=Snake(screen)
foods = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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
                snake.do_extend = True
    while len(foods) < core2.constants.MAX_FOOD:
        foods.add(Food(random.choice(range(screen.get_width())), random.choice(range(screen.get_height()))))

    for food in pygame.sprite.spritecollide(snake.parts.sprites()[0], foods, dokill=True):
        snake.update()
        snake.do_extend = True

    collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
    for key in collided:
        if not collided[key] == [key]:
            print "You lose!"
            pygame.quit()
            quit()

    if snake.hit_border:
        print "You lose!"
        pygame.quit()
        quit()


    screen.fill((0,0,0))
    snake.update()
    snake.parts.draw(screen)
    foods.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)
