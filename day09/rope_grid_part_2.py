DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
tail_visits = set((0, 0))
rope = [[0, 0] for _ in range(10)]

with open("head_motions.txt", "r") as f:
    for line in f:
        direction = DIRECTIONS[line[:1]]
        step_count = int(line[1:].strip())
        for _ in range(int(step_count)):
            rope[0][0] += DIRECTIONS[line[:1]][0]
            rope[0][1] += DIRECTIONS[line[:1]][1]
            for i in range(1, len(rope)):
                prev, curr = rope[i - 1 : i + 1]
                x_diff = abs(curr[0] - prev[0])
                y_diff = abs(curr[1] - prev[1])
                if x_diff > 1 or y_diff > 1:
                    if not x_diff:
                        curr[1] += 1 if curr[1] < prev[1] else -1
                    elif not y_diff:
                        curr[0] += 1 if curr[0] < prev[0] else -1
                    else:
                        curr[0] += 1 if curr[0] < prev[0] else -1
                        curr[1] += 1 if curr[1] < prev[1] else -1
                    if i == 9:
                        tail_visits.add(tuple(curr))
                else:
                    break

    print(f"The tail has visited {len(tail_visits)} positions.")
