# A number of monkeys
# turn = a turn of throwing all items per monkey
# round = round of all turns
# items (starting_items) = item-worry level queues
# operation = calculation of new worry level for items
# test = determination of which monkey to throw to
# inspection_count = total number of times a monkey inspects items
# monkey business = highest inspection_count X second highest inspection_count

monkeys = []
round = 0
turn = 0
with open("monkey_notes.txt", "r") as f:
    ml = []  # monkey line
    for l in f.readlines():
        sl = l.strip()
        if sl:
            ml.append(sl)
            if len(ml) == 6:
                monkey = {}
                monkey["number"] = int(ml[0][7:-1])
                monkey["item_queue"] = list(ml[1][16:].split(","))
                monkey["operation"] = list(ml[2][17:].split())
                monkey["div_by_test"] = int(ml[3][19:])
                monkey["throw_true"] = int(ml[4][25:])
                monkey["throw_false"] = int(ml[5][26:])
                monkey["inspections"] = 0
                monkeys.append(monkey)
                ml = []

for _ in range(20):  # round
    round += 1
    for m in monkeys:  # turn
        while len(m["item_queue"]):
            # print(m["item_queue"])
            item = m["item_queue"].pop(0)
            # print(item)
            # print(m["item_queue"])
            op = m["operation"]
            # op param1
            if op[0] == "old":
                param1 = int(item)
            else:
                param1 = int(op[0])
            # op param2
            if op[2] == "old":
                param2 = int(item)
            else:
                param2 = int(op[2])
            # operation
            if op[1] == "+":
                worry1 = param1 + param2
            elif op[1] == "*":
                worry1 = param1 * param2
            worry2 = worry1 // 3
            # action
            if worry2 % m["div_by_test"] == 0:
                monkeys[m["throw_true"]]["item_queue"].append(worry2)
            else:
                monkeys[m["throw_false"]]["item_queue"].append(worry2)
            m["inspections"] += 1

# calc monkey business
largest = 0
second_largest = 0
for m in monkeys:
    if second_largest > largest:
        largest, secondlargest = second_largest, largest
    if m["inspections"] > second_largest:
        second_largest = m["inspections"]
print(largest * second_largest)
