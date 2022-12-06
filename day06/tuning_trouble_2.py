def get_unique_chars_in_sliding_window(sequence, window_size):
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i : i + window_size]
        if len(window) == len(set(window)):
            return i + window_size


with open("datastream.txt", "r") as f:
    for line in f.readlines():
        print(f"Start of packet: {get_unique_chars_in_sliding_window(line, 4)}")
        print(f"Start of message: {get_unique_chars_in_sliding_window(line, 14)}")
