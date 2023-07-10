class Event(list):
    """ An event is just a list of functions that you call whenever something happens."""
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:

    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, who_scored, goal_scored):
        self.who_scored = who_scored
        self.goal_scored = goal_scored

class Player:
    def __init__(self, name, game: Game):
        self.name = name
        self.game = game
        self.goal_scored = 0

    def score(self):
        self.goal_scored += 1
        args = GoalScoredInfo(self.name, self.goal_scored)
        self.game.fire(args)

class Coach:

    def __init__(self, game: Game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goal_scored > 2:
            print(f'Well donde, {args.who_scored}')