with open('calories_list.txt') as f:
    elf_calories = []
    sum = 0
    for line in f.readlines():

        if not line.strip():            # strip will return en empty string for blank rows which is falsy.
            elf_calories.append(sum)
            sum = 0
        else:
            sum += int(line)
    # print(elf_calories)
    max_calories = max(elf_calories)
    elf_index = elf_calories.index(max_calories)
    print (f"Elf number {elf_index+1} has {max_calories} calories.")
