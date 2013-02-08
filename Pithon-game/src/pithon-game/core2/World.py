
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
    def add_food(self, food):
        self.foods.append(food)
    def set_player_direction(self, player, direction):
        self.players[player.name].change_direction(direction)