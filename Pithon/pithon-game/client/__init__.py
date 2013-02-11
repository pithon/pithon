import pygame, time, Pyro4, sys, copy
sys.path.append("..")
from core2 import constants
from core2 import World
from core2 import Snake



name=raw_input("Name>> ")
ip=raw_input("Server IP>> ")
port=raw_input("Server Port>> ")
color=eval(raw_input("Color (in format '(RED,GREEN,BLUE')>> "))
pygame.init()
screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
world=Pyro4.Proxy("PYRO:WORLD@"+ip+":"+port)
world.add_player(Snake.Snake(name, color=color))

while True:
    
    if not name in world.get_players().keys():
        print "Game Over"
        pygame.quit()
        quit()
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                world.set_player_direction(name,constants.UP)
            if event.key == pygame.K_DOWN:
                world.set_player_direction(name,constants.DOWN)
            if event.key == pygame.K_LEFT:
                world.set_player_direction(name,constants.LEFT)
            if event.key == pygame.K_RIGHT:
                world.set_player_direction(name,constants.RIGHT)
    
    
    
    screen.fill((0,0,0))
    World.draw_world(world, screen)
    
    
    
    pygame.display.flip()
    time.sleep(0.1)