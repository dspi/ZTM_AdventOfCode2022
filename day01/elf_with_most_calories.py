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

    # part 2
    # convert list to dictionary: 
    elf_calories_dict = dict(enumerate(elf_calories))
    #https://stackoverflow.com/questions/16772071/sort-dict-by-value-python/16772088#16772088
    reverse_sorted = sorted(elf_calories_dict.items(), key=lambda x:x[1], reverse=True)
    #print(reverse_sorted)
    top3 = list(reverse_sorted)[:3]
    for elf_num, calories in top3:
        print (f"Elf number {elf_num+1} has {calories} calories.")