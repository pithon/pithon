import pygame
import pygnetic as net
import pygnetic.event as net_events
from pygame.time import Clock
from core2 import constants
from core2 import World
from core2 import Snake
from core2 import Food
import time


pygame.init()
net.init(events=True)


snake_msg = net.register('snake_msg', ('snake',))
direction_msg = net.register('direction_msg', ('name', 'direction'))
food_msg = net.register('food_msg', ('food',))

client = net.Client()
connection = client.connect("localhost", 31415)

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

world = World.World()
snake = Snake.Snake("My snake")
world.add_player(snake)

connection.net_snake_msg((snake.name,))

clock = Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            direction = world.get_player_direction(snake.name)
            if event.key == pygame.K_UP:
                world.set_player_direction(snake.name,constants.UP)
            if event.key == pygame.K_DOWN:
                world.set_player_direction(snake.name,constants.DOWN)
            if event.key == pygame.K_LEFT:
                world.set_player_direction(snake.name,constants.LEFT)
            if event.key == pygame.K_RIGHT:
                world.set_player_direction(snake.name,constants.RIGHT)
            if direction is not world.get_player_direction(snake.name):
                connection.net_direction_msg(snake.name, snake.direction)
        if event.type == net_events.NETWORK:
            if event.net_type == net_events.NET_RECEIVED:
                if event.msg_type == snake_msg:
                    world.add_player(Snake.Snake(*event.message.snake))
                elif event.msg_type == direction_msg:
                    world.set_player_direction(event.message.name, event.message.direction)
                elif event.msg_type == food_msg:
                    world.add_food(Food.Food(*event.message.food))


    screen.fill((0,0,0))
    world.update_world()
    World.draw_world(world, screen)
    pygame.display.flip()
    client.update()
    clock.tick(10)


