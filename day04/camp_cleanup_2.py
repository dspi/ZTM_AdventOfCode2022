sum_fully_containing_pairs, sum_overlapping_pairs = 0, 0
with open("section_pairs.txt", "r") as f:
    for line in f.readlines():
        section_numbers = line.rstrip().replace("-", ",").split(",")
        A, B, C, D = list(map(int, section_numbers))
        if (
            (A <= C and C <= B)
            or (A <= D and D <= B)
            or (C <= A and A <= D)
            or (C <= B and B <= D)
        ):
            sum_overlapping_pairs += 1
            if (A >= C and B <= D) or (C >= A and D <= B):
                sum_fully_containing_pairs += 1

print(f"fully contained: {sum_fully_containing_pairs}")
print(f"some overlap: {sum_overlapping_pairs}")
