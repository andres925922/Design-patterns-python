"""
Chain of Responsibility Coding Exercise
You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:

A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.  -> Done

When the Goblin King is in play, every other goblin gets +1 Attack.

Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:

Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus).

A goblin king comes into play. Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.

"""

class Game:
    def __init__(self):
        self.creatures = []

class Creature:

    def __init__(self, game, attack, defense, name) -> None:
        self.game = game
        self.attack = attack
        self.defense = defense
        self.name = name

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        Creature.__init__(self, game, attack, defense, 'goblin')

    def __str__(self) -> str:
        return f'{self.name} ({self.attack} / {self.defense})'
        
class GoblinKing(Goblin):
    def __init__(self, game):
        # todo
        self.game = game 
        self.attack = 3
        self.defense = 3
        self.name = 'king Goblin'


    def __str__(self) -> str:
        return f'{self.name} ({self.attack} / {self.defense})'

class kingGoblin_GoblinModifier:

    # When the Goblin King is in play, every other goblin gets +1 Attack.

    def __init__(self, game: Game) -> None:
        self.game = game

    def increase_attack_by_one(self):
        if len(self.game.creatures) <= 0:
            return
        
        king_goblin_in_play = False

        for creature in self.game.creatures:
            if isinstance(creature, GoblinKing):
                king_goblin_in_play = True

        if king_goblin_in_play == True:
            for creature in self.game.creatures:
                if isinstance(creature, Goblin):
                    creature.attack += 1



    


if __name__ == '__main__':

    game = Game()

    kgm = kingGoblin_GoblinModifier(game)

    goblin = Goblin(game)
    king_goblin = GoblinKing(game)

    kgm.increase_attack_by_one()

    # print(goblin.attack, king_goblin.attack)
    print(goblin)
    