with open("datastream.txt", "r") as f:
    for line in f.readlines():
        packet = ""
        for i in range(len(line) - 4):
            window_packet = line[i : i + 4]
            window_message = line[i : i + 14]
            if len(window_packet) == len(set(window_packet)) and packet == "":
                packet = f"Start of packet: {i+4}"
            if len(window_message) == len(set(window_message)):
                print(packet)
                print(f"Start of message: {i+14}")
                break
