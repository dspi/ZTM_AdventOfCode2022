# The input ("terminal_output.txt") appears to be a depth-first search, with results.
# Since the size of a dir can only be calculated from the sizes of its children,
# it'll be useful to keep a record of every dir, its size, and its single parent.

# The root dir might be structured like:
#   {"size": 0, "parent": None}
# So all the dirs might be structured like:
dirs = {"/": {"size": 0, "parent": None}}

cur_dir = dirs["/"]
# dir_sizes = {}  # usefull to store all data in a flat dict - Nope...keys may be duplicated.


def change_dir(to_dir):
    global cur_dir
    if to_dir == "..":  # change to parent
        cur_dir = cur_dir["parent"]
    elif to_dir == "/":  # change to root
        cur_dir = dirs["/"]
    else:  # a dir name - add it if it doesn't exist, and change to it
        # Add the dir to CURRENT dir NOT ALL dirs, if it doesn't exist in current dir.
        # Only check against the CURRENT dir, NOT ALL dirs!
        if to_dir not in cur_dir:  # DON'T DO:  if to_dir not in dirs
            # dirs[to_dir] = {"size": 0, "parent": cur_dir}
            cur_dir[to_dir] = {"size": 0, "parent": cur_dir}
            cur_dir = cur_dir[to_dir]


def calc_dir_size(file_size):
    cur_dir["size"] += file_size  # add the file_size to the current dir.
    parent = cur_dir["parent"]
    while parent:  # Add file size to all ancestors
        parent["size"] += file_size
        parent = parent["parent"]


def sum_of_dirs_recursive(dir):
    sum = 0
    if dir["size"] <= 100_000:  # sum all dir sizes that are 100000 or smaller
        sum += dir["size"]
    for sub_dir in dir:
        if sub_dir in ("size", "parent"):
            continue  ## only want item of dir that has size and parent
            # Else TypeError: 'int' object is not subscriptable
        sum += sum_of_dirs_recursive(dir[sub_dir])
    return sum


def smallest_to_be_deleted_recursive(dir, SPACE_TO_BE_DELETED):
    if dir["size"] < SPACE_TO_BE_DELETED:
        return None  # (This only ends one of the recursive branches.)

    smallest_minimum = dir["size"]
    for subdir in dir:
        if subdir in ("size", "parent"):
            continue
        potential_smallest_minimum = smallest_to_be_deleted_recursive(
            dir[subdir], SPACE_TO_BE_DELETED
        )
        if potential_smallest_minimum and potential_smallest_minimum < smallest_minimum:
            smallest_minimum = potential_smallest_minimum
    return smallest_minimum


with open("terminal_output.txt", "r") as f:
    for line in f:  # .readlines():
        tokens = line.strip().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                change_dir(tokens[2])
            elif tokens[1] == "ls":
                pass
        elif tokens[0] != "dir":
            file_size = int(tokens[0])
            calc_dir_size(file_size)

# Recursively sum each dir from root
print(sum_of_dirs_recursive(dirs["/"]))

# In the dir structure...each dict contains its parent
# It can't be a flat dict because there could possibly be duplicate keys.
# Maybe a different structure is better?
# print(dirs)


# Part2:
TOTAL_SYSTEM_SPACE = 70_000_000
SPACE_NEEDED = 30_000_000
SPACE_USED = dirs["/"]["size"]
SPACE_TO_BE_DELETED = SPACE_NEEDED - (TOTAL_SYSTEM_SPACE - SPACE_USED)

# Recursively from root, find the smallest directory space to be deleted:
print(smallest_to_be_deleted_recursive(dirs["/"], SPACE_TO_BE_DELETED))
