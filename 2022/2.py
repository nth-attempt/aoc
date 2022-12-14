inp1 = """A Y
B X
C Z"""

# Part 1

class RPS:
    maps = {"X": "R", "Y": "P", "Z": "S", "A": "R", "B": "P", "C": "S"}

    def __init__(self, turn):
        self.turn = self.maps[turn]

    def __eq__(self, other):
        return self.turn == other.turn

    def __gt__(self, other):
        return ((self.turn == "R" and other.turn == "S") or
                (self.turn == "S" and other.turn == "P") or
                (self.turn == "P" and other.turn == "R"))


def score(inp):
    rounds = [line.split(" ") for line in inp.splitlines()]
    score_map = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0
    for you, me in rounds:
        total_score += score_map[me]
        you, me = RPS(you), RPS(me)
        if you == me:
            total_score += 3
        elif me > you:
            total_score += 6
    return total_score


print(score(inp1))


# Part 2

def score2(inp):
    rounds = [line.split(" ") for line in inp.splitlines()]
    res_map = {"X": 0, "Y": 3, "Z": 6}
    score_map = {"A": 1, "B": 2, "C": 3}
    draw_map = {"A": "A", "B": "B", "C": "C"}
    win_map = {"A": "B", "B": "C", "C": "A"}
    lose_map = {"A": "C", "B": "A", "C": "B"}
    total_score = 0
    for you, result in rounds:
        total_score += res_map[result]
        if result == "X":
            total_score += score_map[lose_map[you]]
        elif result == "Y":
            total_score += score_map[draw_map[you]]
        else:
            total_score += score_map[win_map[you]]
    return total_score


print(score2(inp1))
