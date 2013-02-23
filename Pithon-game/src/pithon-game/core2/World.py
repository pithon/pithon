import pygame, Food, constants, random

class World:
    def __init__(self):
        self.players={}
        self.foods=pygame.sprite.Group()
    def get_players(self):
        return self.players.values()
    def get_foods(self):
        return self.foods
    def get_player_direction(self, player):
        return self.players[player].direction
    def add_food(self, food):
        self.foods.add(food)
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

            for s in pygame.sprite.groupcollide(pygame.sprite.Group((x.parts for x in self.get_players())), self.foods, False, True):
                s.snake.do_extend = True

            collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
            for key in collided:
                if not collided[key] == [key]:
                    pass#print "You lose!"

            if snake.hit_border:
                pass#print "You lose!"


    def get_foods(self):
        return self.foods

    def make_foods(self):
        foods = []
        while len(self.foods) < constants.MAX_FOOD:
            food = Food.Food(x=random.choice(range(constants.SCREEN_WIDTH)),
                        y=random.choice(range(constants.SCREEN_HEIGHT)))
            self.foods.add(food)
            foods.append(food)
        return foods



def draw_world(world, screen):
    for player in world.get_players():
        player.parts.draw(screen)
    world.get_foods().draw(screen)
