fully_contained_pairs = 0
with open("section_pairs.txt", "r") as f:
    for line in f.readlines():
        range_pair = line.strip().split(",")
        rp_list = [item.split("-") for item in range_pair]  # [['2','4'], ['6','8']]

        # values need to be converted to type 'int' before comparison
        # otherwise the char ascii values are compared (bitwise comparison)
        # eg: 100" < "50" => True, and "99" < "50" => False
        if int(rp_list[0][0]) <= int(rp_list[1][0]) and int(rp_list[0][1]) >= int(
            rp_list[1][1]
        ):
            fully_contained_pairs += 1
        # need an 'elif', not an 'if' to prevent double counting in cases like: 1-4,1-4
        elif int(rp_list[0][0]) >= int(rp_list[1][0]) and int(rp_list[0][1]) <= int(
            rp_list[1][1]
        ):
            fully_contained_pairs += 1

print(fully_contained_pairs)
