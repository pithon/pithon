import pygame, Food, constants, random

class World:
    def __init__(self):
        self.players={}
        self.foods=pygame.sprite.Group()
    def get_players(self):
        return self.players
    def get_foods(self):
        return self.foods
    def add_player(self, player):
        self.players[player.name]=player
    def remove_player(self, player):
        self.players.remove(player.name)
    def set_player_direction(self, player, direction):
        self.players[player].change_direction(direction)
    def update_world(self):
        for k in self.players:
            snake=self.players[k]
            snake.update()

            for food in pygame.sprite.spritecollide(snake.parts.sprites()[0], self.foods, dokill=True):
                snake.do_extend = True
                print len(snake.parts)

            collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
            for key in collided:
                if not collided[key] == [key]:
                    print "You lose!"

            if snake.hit_border:
                print "You lose!"

        while len(self.foods) < constants.MAX_FOOD:
            self.foods.add(Food.Food(x=random.choice(range(constants.SCREEN_WIDTH)),
                        y=random.choice(range(constants.SCREEN_HEIGHT))))

    def get_foods(self):
        return self.foods


def draw_world(world, screen):
    for k in world.get_players():
        player=world.get_players()[k]
<<<<<<< HEAD
        player.parts.draw(screen)
    world.get_foods().draw(screen)
=======
        player.parts.draw(pygame.display.get_surface())
    world.get_foods().draw(pygame.display.get_surface())
>>>>>>> 8655a588e9b605ab2c763febc1560bfe67c7f392
