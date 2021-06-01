from classes.player import Player
from classes.frame import Frame


class Game:
    def __init__(self):
        self.players = [Player("Jerry"), Player(
            "John"), Player("Jenna"), Player("Ellie")]
        self.current_scores = []
        self.current_frame = 0

    def play(self):
        for i in range(10):
            print(f"Round {i + 1}")
            print("--------")

            for player in self.players:
                player.frames.append(Frame())
                current_frame = player.frames[-1]
                current_frame.deliver()
                print(
                    f"{player.name}: {current_frame.delivery_1}, {current_frame.delivery_2}", end="")
                if current_frame.strike:
                    print("  Strike!")
                elif current_frame.spare:
                    print("  Spare!")
                else:
                    print()

            self.update_current_scores()
            for score in self.current_scores:
                print(score)

            print()

            # for i in range(4):
            #     print(f"Name: {self.players[i]}  |  Score: {self.current_scores[i]}")
            # self.update_current_scores()

    def update_current_scores(self):
        self.current_scores = []
        for player in self.players:
            self.current_scores.append(player.return_current_score())


game_1 = Game()
game_1.play()
