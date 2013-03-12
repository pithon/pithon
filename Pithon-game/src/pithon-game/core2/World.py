import pygame, Food, constants, random

class World:
    def __init__(self):
        self.players={}
        self.foods=pygame.sprite.OrderedUpdates()
        self.food_dict = {}
        self.extend_snakes = set()
        self.remove_foods = pygame.sprite.Group()
    def get_players(self):
        return self.players.values()
    def get_foods(self):
        return self.foods
    def get_food(self, food_id):
        return self.food_dict[food_id]
    def get_player_direction(self, player):
        return self.players[player].direction
    def get_remove_foods(self):
        return self.remove_foods

    def add_food(self, food):
        self.foods.add(food)
        self.food_dict[food.id] = food
    def remove_food(self, food):
        self.foods.remove(food)
        del self.food_dict[food.id]
    def add_player(self, player):
        self.players[player.name]=player
    def remove_player(self, player):
        self.players.remove(player.name)
    def set_player_direction(self, player, direction):
        self.players[player].change_direction(direction)
    def update_world(self):
        for snake in self.get_players():
            snake.update()

            collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
            for key in collided:
                if not collided[key] == [key]:
                    pass#print "You lose!"

            if snake.hit_border:
                pass#print "You lose!"

    def food_collide(self):
        self.extend_snakes = set()
        for snake in self.get_players():
            foods = pygame.sprite.groupcollide(snake.parts, self.foods, False, False)
            for s in foods:
                s.snake.do_extend = True
                self.extend_snakes.add(s.snake)
                for f in foods[s]:
                    self.remove_foods.add(f)
        return self.extend_snakes


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
