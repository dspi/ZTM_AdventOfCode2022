START = 20
FREQ = 40
cyc = 0
reg = 1
sig_str = 0


def cycle():
    global START
    global FREQ
    global cyc
    global reg
    global sig_str

    cyc += 1
    if (cyc - START) % FREQ == 0 and cyc >= START:
        sig_str += cyc * reg
        # print(f"{cyc} x {reg} = {cyc * reg} : sig_str = {sig_str}")


with open("cpu_instructions.txt", "r") as f:
    for l in f:
        ins = l.strip().split()
        if ins[0] == "noop":
            cycle()
        elif ins[0] == "addx":
            cycle()
            cycle()
            reg += int(ins[1])

print(f"Part1 - Signal Strength is: {sig_str}")
