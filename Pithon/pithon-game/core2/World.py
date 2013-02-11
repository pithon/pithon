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
                    print k+" died!"
                    self.remove_player(k)

            if snake.hit_border:
                print k+" died!"
                self.remove_player(k)

        while len(self.foods) < constants.MAX_FOOD:
            self.foods.add(Food.Food(x=random.choice(range(constants.SCREEN_WIDTH)),
                        y=random.choice(range(constants.SCREEN_HEIGHT))))

    def get_foods(self):
        return self.foods


def draw_world(world, screen):
    for k in world.get_players():
        player=world.get_players()[k]
        for part in player.get_parts():
            pygame.draw.rect(screen, part.color, part.rect)
    #local_draw_spritegroup(world.get_foods(), screen