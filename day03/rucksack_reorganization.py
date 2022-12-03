sum_of_priorities = 0
rucksack_number = 0
group_rucksack1, group_rucksack2, group_rucksack3 = (set() for _ in range(3))
sum_of_badges = 0


def get_priority(letter: str):
    # get ascii value of char
    letter_ord = ord(letter)

    # ascii lowercase starts on 97 and uppercase on 65
    if letter_ord >= 97:
        priority = letter_ord - 97 + 1
    else:
        priority = letter_ord - 65 + 27
    return priority


with open("rucksack_items_list.txt", "r") as f:
    for line in f.readlines():
        rucksack_number += 1
        rucksack = line.strip()

        # slice into 2 equal halves and then remove duplicates by creating sets
        compartment_1 = set(rucksack[: len(rucksack) // 2])
        compartment_2 = set(rucksack[len(rucksack) // 2 :])
        # find common item by set intersection
        common_letter = compartment_1.intersection(compartment_2).pop()

        sum_of_priorities += get_priority(common_letter)

        # keep track of the 3 rucksacks per group
        if rucksack_number % 3 == 0:
            group_rucksack3 = set(rucksack)
            # once 3 rucksacks are set, find common item
            common_badge = (
                group_rucksack1.intersection(group_rucksack2)
                .intersection(group_rucksack3)
                .pop()
            )
            sum_of_badges += get_priority(common_badge)
        elif rucksack_number % 2 == 0:
            group_rucksack2 = set(rucksack)
        else:
            group_rucksack1 = set(rucksack)

print(f"Sum of priorities: {sum_of_priorities}")
print(f"Sum of badges: {sum_of_badges}")

# For part 2, a generator could be used to read three lines at a time,
# without loading the whole file into memory, as per this link
# https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time/5832971#5832971
# However, I'll just work with lines in multiples of 3 in the above.
