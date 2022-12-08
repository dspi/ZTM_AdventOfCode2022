M = []
with open("treemap.txt", "r") as f:
    for line in f:
        row = [int(x) for x in list(line.strip())]
        M.append(row)

ROWS, COLS = len(M), len(M[1])
MT = list(map(list, zip(*M)))  # transpose matrix


def checkVisibilityInRow(M):
    visible_trees = []
    y_pos = 0
    for row in M[1 : (ROWS - 1)]:  # excluding edges
        y_pos += 1
        x_pos = 0
        for n in row[1 : (COLS - 1)]:  # excluding edges
            x_pos += 1
            if all(i < n for i in row[:x_pos]):
                # print(f"{n} IS VISIBLE FROM THE LEFT")
                visible_trees.append([x_pos, y_pos])
            elif all(i < n for i in row[1 + x_pos :]):
                # print(f"{n} IS VISIBLE FROM THE RIGHT")
                visible_trees.append([x_pos, y_pos])
            # else:
            # print(f"{n} IS NOT VISIBLE FROM THE LEFT OR RIGHT")
    return visible_trees


vis_M = checkVisibilityInRow(M)
vis_MT = checkVisibilityInRow(MT)
vis_edges = 2 * ROWS + 2 * COLS - 4
dups = 0
for i in vis_MT:
    if list([i[1], i[0]]) in vis_M:
        dups += 1

print(len(vis_M) + len(vis_MT) - dups + vis_edges)
