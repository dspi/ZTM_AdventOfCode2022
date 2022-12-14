from copy import deepcopy

crates_with_positions = []
stacks_with_positions = []
software_stacks = []
do_once = True

with open("crates_input.txt", "r") as f:
    # FORMAT DATA FROM WHOLE FILE:
    for line in f.readlines():
        sline = line.strip()
        # crates with positions
        if sline and sline[0] == "[":
            positions = [c + 1 for (c, e) in enumerate(line) if e == "["]
            crates = [c for c in line if c.isalpha()]
            crate_positions = dict(zip(positions, crates))
            crates_with_positions.append(crate_positions)
        # stack numbers with positions
        elif sline and sline[0] == "1" and stacks_with_positions == []:
            stacks = [int(c) for c in str.split(line) if c.isdigit()]
            positions = [c for (c, e) in enumerate(line) if e.isalnum()]
            stacks_with_positions = dict(zip(positions, stacks))
        # moves:
        elif sline:

            if do_once:  # ...just before processing the moves
                # BUILD STACKS
                for s in stacks_with_positions:
                    software_stack = []
                    cwpdc = deepcopy(crates_with_positions)
                    while len(cwpdc) > 0:
                        cwp = cwpdc.pop()
                        if s in cwp:
                            software_stack.append(cwp[s])
                    software_stacks.append(software_stack)
                do_once = False

            move = [int(c) for c in str.split(sline) if c.isdigit()]

            # For Part2, introducing an intermediate_stack, will change the order as needed:
            intermediate_stack = []
            for _ in range(move[0]):  # quantity
                crane_lift = software_stacks[move[1] - 1].pop()  # from
                # software_stacks[move[2] - 1].append(crane_lift)  # to
                intermediate_stack.append(crane_lift)
            while len(intermediate_stack):
                crane_lift2 = intermediate_stack.pop()
                software_stacks[move[2] - 1].append(crane_lift2)  # to

    # TOP OF EACH STACK
    ans = ""
    for s in software_stacks:
        ans += s.pop()
    print(ans)
