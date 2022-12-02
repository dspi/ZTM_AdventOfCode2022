HAND_SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}

LOSS, DRAW, WIN = 0, 3, 6

WINNING_COMBINATIONS = {"C": "X", "A": "Y", "B": "Z"}
LOOSING_COMBINATIONS = {"B": "X", "C": "Y", "A": "Z"}

total_score = 0

with open("strategy_guide.txt", "r") as f:
    for line in f.readlines():

        opponent, me = line.strip().split()

        if WINNING_COMBINATIONS[opponent] == me:
            print(f"WIN: {line}")
            total_score += WIN

        elif LOOSING_COMBINATIONS[opponent] == me:
            print(f"LOSS: {line}")
            total_score += LOSS
        else:
            print(f"DRAW: {line}")
            total_score += DRAW

        total_score += HAND_SHAPE_SCORE[me]

print(f"My Total Score: {total_score}")
