sum_of_priorities = 0
with open("rucksack_items_list.txt", "r") as f:
    for line in f.readlines():
        rucksack = line.strip()
        # slice into 2 equal halves and then remove duplicates by creating sets
        compartment_1 = set(rucksack[: len(rucksack) // 2])
        compartment_2 = set(rucksack[len(rucksack) // 2 :])
        # find common item by set intersection
        common_letter = compartment_1.intersection(compartment_2).pop()

        # get ascii value of char
        common_letter_ord = ord(common_letter)

        # ascii lowercase starts on 97 and uppercase on 65
        if common_letter_ord >= 97:
            priority = common_letter_ord - 97 + 1
        else:
            priority = common_letter_ord - 65 + 27

        sum_of_priorities += priority
print(sum_of_priorities)
