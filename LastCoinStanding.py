import LastCoinStanding
from easyAI import TwoPlayersGame, id_solve, Human_Player, AI_Player
from easyAI.AI import TT


class LastCoinStanding(TwoPlayersGame):
    def __init__(self, players):
        self.players = players
        self.nplayer = 1
        self.num_coins = 30
        self.max_coins = 4

    def possible_moves(self):
        return [str(x) for x in range(1, self.max_coins + 1)]

    def make_move(self, move):
        self.num_coins -= int(move)

    def win(self):
        return self.num_coins <= 0

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def show(self):
        print(self.num_coins, 'monet zostalo na stosie')

if __name__ == '__main__':
    tt = TT()
    LastCoinStanding.ttentry = lambda self: self.num_coins
    result, depth, move = id_solve(LastCoinStanding,
                                   range(2, 20), win_score=100, tt=tt)
    print(result, depth, move)
    game = LastCoinStanding([AI_Player(tt), Human_Player()])
    game.play()