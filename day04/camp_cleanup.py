fully_contained_pairs, any_overlap = 0, 0
with open("section_pairs.txt", "r") as f:
    for line in f.readlines():
        range_pair = line.strip().split(",")
        rp_list = [item.split("-") for item in range_pair]  # [['2','4'], ['6','8']]

        # values need to be converted to type 'int' before comparison
        # otherwise the char ascii values are compared (bitwise comparison)
        # eg: 100" < "50" => True, and "99" < "50" => False
        # need an 'elif', not an 'if' to prevent double counting in cases like: 1-4,1-4

        # If first pair includes second pair:
        if int(rp_list[0][0]) <= int(rp_list[1][0]) and int(rp_list[0][1]) >= int(
            rp_list[1][1]
        ):
            fully_contained_pairs += 1
            any_overlap += 1
        # If first pair is included by second pair
        elif int(rp_list[0][0]) >= int(rp_list[1][0]) and int(rp_list[0][1]) <= int(
            rp_list[1][1]
        ):
            fully_contained_pairs += 1
            any_overlap += 1

        # # If start of first pair within the second pair
        # elif int(rp_list[0][0]) >= int(rp_list[1][0]) and int(rp_list[0][0]) <= int(
        #     rp_list[1][1]
        # ):
        #     any_overlap += 1

        # # If start of second pair within the first pair
        # elif int(rp_list[1][0]) >= int(rp_list[0][0]) and int(rp_list[1][0]) <= int(
        #     rp_list[0][1]
        # ):
        #     any_overlap += 1

        # More simple than above:
        # If start of first pair is after end of second pair, OR
        # start of second pair is after end of first pair, no overlap
        elif not (
            int(rp_list[0][0]) > int(rp_list[1][1])
            or int(rp_list[1][0]) > int(rp_list[0][1])
        ):
            any_overlap += 1

print(fully_contained_pairs)
print(any_overlap)
