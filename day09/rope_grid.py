DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
tail_visits = set()
rope = [[0, 0] for _ in range(2)]


def move(direction, knot, following_knot):
    global rope, tail_visits
    # calc head
    if direction:
        knot[0] += direction[0]
        knot[1] += direction[1]
    x_diff = knot[0] - following_knot[0]
    y_diff = knot[1] - following_knot[1]
    if abs(x_diff) == 1 and abs(y_diff) == 1:  # diagonal adjacent
        pass
    elif abs(x_diff) == 2 and abs(y_diff) == 1:  # diagonal not adjacent on x
        following_knot[0] += direction[0]
        following_knot[1] = knot[1]
    elif abs(x_diff) == 1 and abs(y_diff) == 2:  # diagonal not adjacent on y
        following_knot[0] = knot[0]
        following_knot[1] += direction[1]
    elif abs(x_diff) == 2:  # not adjacent on x
        following_knot[0] += direction[0]
    elif abs(y_diff) == 2:  # not adjacent on y
        following_knot[1] += direction[1]
    tail_visits.add(tuple(rope[-1]))


with open("head_motions.txt", "r") as f:
    for line in f:
        initial_direction = DIRECTIONS[line[:1]]
        step_count = int(line[1:].strip())
        for _ in range(step_count):
            # knot = rope[0]
            # following_knot = rope[1]
            for i in range(len(rope) - 1):
                knot = rope[i]
                following_knot = rope[i + 1]
                if i == 0:
                    direction = initial_direction
                else:

                    # IT SEEMS THAT USING direction LIKE THIS IS MORE COMPLEX THAN NEEDED FOR
                    # PART 2.

                    # A BETTER MOVE WOULD BE TO USE direction ONLY FOR THE FIRST KNOT MOVE, AND
                    # BUILD THE CALC RULES FOR THE OTHER KNOTS BASED ON THE PREV KNOTS POSITION.
                    # AND NOT TRY TO RECALC THE direction ONLY TO THEN REUSE THE RULES OF PART 1.

                    # calculate a knock-on direction
                    prev_knot = rope[i - 1]
                    x_diff = prev_knot[0] - knot[0]
                    y_diff = prev_knot[1] - knot[1]

                    if abs(x_diff) == 1 and abs(y_diff) == 1:  # diagonal adjacent
                        # pass
                        direction = (0, 0)
                    elif (
                        abs(x_diff) == 2 and abs(y_diff) == 1
                    ):  # diagonal not adjacent on x
                        direction = (-x_diff, 0)
                    elif (
                        abs(x_diff) == 1 and abs(y_diff) == 2
                    ):  # diagonal not adjacent on y
                        direction = (0, -y_diff)

                    elif (
                        abs(x_diff) == 2 and abs(y_diff) == 2
                    ):  # diagonal not adjacent on x or y
                        direction = (-x_diff, -y_diff)
                    elif abs(x_diff) == 2:  # not adjacent on x
                        direction = (-x_diff, 0)
                    elif abs(y_diff) == 2:  # not adjacent on y
                        direction = (0, -y_diff)

                move(direction, knot, following_knot)
    print(f"The tail has visited {len(tail_visits)} positions.")
    print("THIS WORK FOR PART 1, NOT PART 2")
