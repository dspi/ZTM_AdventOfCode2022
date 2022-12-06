with open("datastream.txt", "r") as f:
    for line in f.readlines():
        c_pos, start = 0, 0
        memo = []
        packet_found = False
        for c in line:
            c_pos += 1
            if c in memo:
                memo_pos_of_c = memo.index(c)
                memo = memo[memo_pos_of_c + 1 :]
            memo.append(c)
            if len(memo) == 4:
                if not packet_found:
                    packet_found = True
                    print(f"Start of packet: {c_pos}")
                    # break
            if len(memo) == 14:
                print(f"Start of message: {c_pos}")
                break
