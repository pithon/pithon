
class World:
    def __init__(self):
        self.players={}
        self.foods=[]
    def get_players(self):
        return self.players
    def get_foods(self):
        return self.foods
    def add_player(self, player):
        self.players[player.name]=player
    def set_player_direction(self, player, direction):
        self.players[player.name].change_direction(direction)
    def update_world(self):
        for snake in self.players:
            snake.update()
            for food in pygame.sprite.spritecollide(snake.parts.sprites()[0], foods, dokill=True):
                snake.update()
                snake.do_extend = True
                print len(snake.parts)
        
            collided = pygame.sprite.groupcollide(snake.parts, snake.parts, False, False)
            for key in collided:
                if not collided[key] == [key]:
                    print "You lose!"
        
            if snake.hit_border:
                print "You lose!"