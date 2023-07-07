
class Creature:

    def __init__(self, name, attack, defense) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f'{self.name} has ({self.attack} / {self.defense})'
    
class CreatureModifier:

    def __init__(self, creature: Creature) -> None:
        self.creature = creature
        self.next_modifier: CreatureModifier = None               # Next modifier in the chain

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier=modifier)
        else:
            self.next_modifier = modifier

    def handle_modifier(self): 
        if self.next_modifier:
            self.next_modifier.handle_modifier()

class Sword(CreatureModifier):

    def handle_modifier(self):
        self.creature.attack *= 3
        super().handle_modifier()

class Shield(CreatureModifier):

    def handle_modifier(self):
        self.creature.defense += 8
        super().handle_modifier()
    
if __name__ == '__main__':

    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root_modifier = CreatureModifier(goblin)
    root_modifier.add_modifier(Sword(goblin))
    root_modifier.add_modifier(Shield(goblin))

    root_modifier.handle_modifier()
    print(goblin)