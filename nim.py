import random

from functools import reduce

class Game:

    def __init__(self, opponent, piles, pile_max, state=None, start_player=None):
        if state is None:
            self.state = state
        else:
            self.state = random.choices(range(1, pile_max + 1), k=piles)

        if start_player is None:
            self.start_player = random.choice([0, 1])
        else:
            self.start_player = start_player

        self.opponent = opponent

    def __repr__(self):
        return f"Game({self.opponent}, state={self.state})"

    def is_endgame(self):
        # endgame is when only 1 pile has more than one stone
        # strategy needs to change for these situations
        return sum([p > 1 for p in self.state]) <= 1

    def best_move(self):
        s = self.nimsum()
        if self.is_endgame():
            odd_turns_left = sum([bool(p) for p in self.state]) % 2
            biggest = max(self.state)
            idx_max = self.state.index(biggest)
            if biggest == 1:
                return idx_max, 1
            else:
                if odd_turns_left:
                    return idx_max, biggest - 1
                else:
                    return idx_max, biggest
        if s == 0:
            # take 1 from the biggest pile
            biggest = max(self.state)
            idx_max = self.state.index(biggest)
            return idx_max, 1

        for idx, pile in enumerate(self.state):
            comp = pile ^ s
            if comp < pile:
                return idx, pile - comp

    def game_over(self):
        return not any(self.state)

    def take(self, pile, n):
        self.state[pile] -= n

    def nimsum(self):
        return reduce(lambda x, y: x^y, self.state)



