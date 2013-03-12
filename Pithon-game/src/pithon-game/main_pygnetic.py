import pygame
import pygnetic as net
import pygnetic.event as net_events
from pygame.time import Clock
from core2 import constants
from core2 import World
from core2 import Snake

pygame.init()
net.init(events=True)


snake_msg = net.register('snake_msg', ('snake',))
direction_msg = net.register('direction_msg', ('name', 'direction'))
new_food_msg = net.register('new_food_msg', ('food',))
remove_food_msg = net.register('remove_food_msg', 'food_id')
extend_msg = net.register('extend_msg')


server = net.Server(port=31415)



screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

world = World.World()
snake = Snake.Snake("Server snake")
world.add_player(snake)

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
                for client in server.connections():
                    client.net_direction_msg(snake.name, snake.direction)
        if event.type == net_events.NETWORK:
            if event.net_type == net_events.NET_CONNECTED:
                print 'Connected'
                for food in world.get_foods():
                    event.connection.net_new_food_msg((food.rect.x, food.rect.y))
                event.connection.net_snake_msg((snake.name, snake.head.rect.x, snake.head.rect.y))
            if event.net_type == net_events.NET_DISCONNECTED:
                print 'Disconnected'
            if event.net_type == net_events.NET_RECEIVED:
                if event.msg_type == snake_msg:
                    world.add_player(Snake.Snake(*event.message.snake, connection=event.connection))
                elif event.msg_type == direction_msg:
                    world.set_player_direction(event.message.name, event.message.direction)

    screen.fill((0,0,0))
    world.update_world()

    for player in world.food_collide():
        player.send(extend_msg)

    for food in world.get_remove_foods():
        for client in server.connections():
            print "Id: ",food.id
            client.net_remove_food_msg((food.id,))
        food.kill()

    for food in world.make_foods():
        for client in server.connections():
            print "Sending food"
            client.net_new_food_msg((food.rect.x, food.rect.y))

    World.draw_world(world, screen)
    pygame.display.flip()
    server.update()
    clock.tick(10)
