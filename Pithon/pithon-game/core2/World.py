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
        self.players.pop(player, 0)
    def set_player_direction(self, player, direction):
        self.players[player].change_direction(direction)
    def update_world(self):
        tokill=[]
        for k in self.players:
            snake=self.players[k]
            snake.update()

            for food in pygame.sprite.spritecollide(snake.parts.sprites()[0], self.foods, dokill=True):
                snake.do_extend = True

            collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
            for key in collided:
                if not collided[key] == [key]:
                    print k+" died!"
                    tokill.append(k)

            if snake.hit_border:
                print k+" died!"
                self.remove_player(k)

        while len(self.foods) < constants.MAX_FOOD:
            self.foods.add(Food.Food(
                        x=multipleround(random.choice(range(constants.SCREEN_WIDTH-constants.BLOCK_SIZE)), constants.BLOCK_SIZE),
                        y=multipleround(random.choice(range(constants.SCREEN_HEIGHT-constants.BLOCK_SIZE)), constants.BLOCK_SIZE))
                           )

    def get_foods(self):
        return self.foods


def draw_world(world, screen):
    for k in world.get_players():
        player=world.get_players()[k]
        for part in player.get_parts():
            pygame.draw.rect(screen, part.color, part.rect)
    for food in world.get_foods():
        pygame.draw.rect(screen, (0,0,255), food.rect)

def multipleround(x, base=5):
    return int(base * round(float(x)/base))