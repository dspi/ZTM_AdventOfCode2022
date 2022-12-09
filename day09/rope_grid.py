DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
tail_visits = set()
head, tail = [0, 0], [0, 0]


def move(direction):
    global DIRECTIONS, head, tail, tail_visits
    # calc head
    if direction:
        head[0] += direction[0]
        head[1] += direction[1]
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) == 1 and abs(y_diff) == 1:  # diagonal adjacent
        pass
    elif abs(x_diff) == 2 and abs(y_diff) == 1:  # diagonal not adjacent on x
        tail[0] += direction[0]
        tail[1] = head[1]
    elif abs(x_diff) == 1 and abs(y_diff) == 2:  # diagonal not adjacent on y
        tail[0] = head[0]
        tail[1] += direction[1]
    elif abs(x_diff) == 2:  # not adjacent on x
        tail[0] += direction[0]
    elif abs(y_diff) == 2:  # not adjacent on y
        tail[1] += direction[1]
    tail_visits.add(tuple(tail))


with open("head_motions.txt", "r") as f:
    move(None)
    for line in f:
        direction = DIRECTIONS[line[:1]]
        step_count = int(line[1:].strip())
        [move(direction) for _ in range(step_count)]
    print(f"The tail has visited {len(tail_visits)} positions.")
