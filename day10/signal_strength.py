START = 20
FREQ = 40
cyc = 0
reg = 1
sig_str = 0
pix_pos = 0


def cycle(display):
    global START, FREQ, cyc, reg, sig_str

    cyc += 1
    display = set_display(display)

    if (cyc - START) % FREQ == 0 and cyc >= START:
        sig_str += cyc * reg
        # print(f"{cyc} x {reg} = {cyc * reg} : sig_str = {sig_str}")

    return display


def set_display(display):
    global cyc, reg, pix_pos
    pix_pos += 1  # pixel position
    if pix_pos == reg + 1 or pix_pos == reg or pix_pos == reg + 2:
        display += "#"
    else:
        display += "."
    if pix_pos == 40:  # initialize each display line
        pix_pos = 0
    return display


with open("cpu_instructions.txt", "r") as f:
    display = ""
    for l in f:
        ins = l.strip().split()
        if ins[0] == "noop":
            display = cycle(display)
        elif ins[0] == "addx":
            display = cycle(display)
            display = cycle(display)
            reg += int(ins[1])

# split into rows of 40
display_lines = [display[i : i + 40] for i in range(0, len(display), 40)]

print(f"Part1 - Signal Strength is: {sig_str}")
print(f"Part2 - Display is:")
for l in display_lines:
    print(l)
