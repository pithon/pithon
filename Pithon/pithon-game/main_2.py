import pygame, time
from core2 import constants
from core2 import World
from core2 import Snake

pygame.init()
screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

world=World.World()
world.add_player(Snake.Snake("singleplayersnake"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                world.set_player_direction("singleplayersnake",constants.UP)
            if event.key == pygame.K_DOWN:
                world.set_player_direction("singleplayersnake",constants.DOWN)
            if event.key == pygame.K_LEFT:
                world.set_player_direction("singleplayersnake",constants.LEFT)
            if event.key == pygame.K_RIGHT:
                world.set_player_direction("singleplayersnake",constants.RIGHT)
    screen.fill((0,0,0))
    world.update_world()
    World.draw_world(world, screen)
    pygame.display.flip()
    time.sleep(0.1)