HAND_SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}

LOSS, DRAW, WIN = 0, 3, 6

WINNING_COMBINATIONS = {"C": "X", "A": "Y", "B": "Z"}
LOOSING_COMBINATIONS = {"B": "X", "C": "Y", "A": "Z"}
DRAWING_COMBINATIONS = {"A": "X", "B": "Y", "C": "Z"}

STRATEGIC_LOSS, STRATEGIC_DRAW, STRATEGIC_WIN = "X", "Y", "Z"


def get_hand_shape_for_strategy(opponent, strategy):
    to_play = ""
    if strategy == STRATEGIC_LOSS:
        to_play = LOOSING_COMBINATIONS[opponent]
    elif strategy == STRATEGIC_WIN:
        to_play = WINNING_COMBINATIONS[opponent]
    elif strategy == STRATEGIC_DRAW:
        to_play = DRAWING_COMBINATIONS[opponent]
    return to_play


total_score = 0
strategic_score = 0

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

        # part 2 - "me" is actually "strategy" now, so figure out what to play:
        to_play = get_hand_shape_for_strategy(opponent, me)

        if me == STRATEGIC_WIN:
            print(f"To WIN play {to_play}")
            strategic_score += WIN
        elif me == STRATEGIC_LOSS:
            print(f"To LOOSE play {to_play}")
            strategic_score += LOSS
        elif me == STRATEGIC_DRAW:
            print(f"To DRAW play {to_play}")
            strategic_score += DRAW

        strategic_score += HAND_SHAPE_SCORE[to_play]

print(f"My Total Score: {total_score}")
print(f"My Strategic Score: {strategic_score}")
