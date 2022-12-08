# This solution uses a matrix (2D list) as well as its transpose.
# the rows of each are processed, and the results of each are combined,
# taking into account the need to transpose indices and remove duplicates.
M = []
with open("treemap.txt", "r") as f:
    for line in f:
        row = [int(x) for x in list(line.strip())]
        M.append(row)

ROWS, COLS = len(M), len(M[1])
MT = list(map(list, zip(*M)))  # transpose matrix (https://stackoverflow.com/a/6473724)


def checkVisibilityInRows(M):
    visible_trees = {}
    y_pos = 0
    for row in M[1 : (ROWS - 1)]:  # excluding edges
        y_pos += 1
        x_pos = 0
        for n in row[1 : (COLS - 1)]:  # excluding edges
            x_pos += 1
            coords = (x_pos, y_pos)
            if all(i < n for i in row[:x_pos]):
                # print(f"{n} IS VISIBLE FROM THE LEFT")
                visible_trees[coords] = n
            elif all(i < n for i in row[1 + x_pos :]):
                # print(f"{n} IS VISIBLE FROM THE RIGHT")
                visible_trees[coords] = n
            # else:
            # print(f"{n} IS NOT VISIBLE FROM THE LEFT OR RIGHT")
    return visible_trees


def calcScenicScoreInRows(M):
    scenic_scores = {}
    y_pos = 0
    for row in M:
        y_pos += 1
        x_pos = 0
        for n in row:
            x_pos += 1
            coords = (x_pos, y_pos)
            scenic_score_left = 0
            scenic_score_right = 0
            for i in reversed(row[: x_pos - 1]):  # look left
                scenic_score_left += 1
                if i >= n:
                    break
            for i in row[x_pos:]:  # look right
                scenic_score_right += 1
                if i >= n:
                    break
            scenic_scores[coords] = scenic_score_left * scenic_score_right

    return scenic_scores


vis_M = checkVisibilityInRows(M)
vis_MT = checkVisibilityInRows(MT)
vis_edges = 2 * ROWS + 2 * COLS - 4

# count duplicates
dups = 0
for i in vis_MT:
    iT = (i[1], i[0])
    if iT in vis_M:
        dups += 1

score_M = calcScenicScoreInRows(M)
score_MT = calcScenicScoreInRows(MT)

# calculate scenic_score
max_scenic_score = 0
for i in score_MT:
    iT = (i[1], i[0])
    tree_scenic_score = score_M[i] * score_MT[iT]
    max_scenic_score = max(max_scenic_score, tree_scenic_score)

print(f"Tree Visibility: {len(vis_M) + len(vis_MT) - dups + vis_edges}")
print(f"Scenic Score: {max_scenic_score}")
