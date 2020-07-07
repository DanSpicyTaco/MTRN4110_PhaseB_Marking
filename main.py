import platform
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

###
# Helpers for all tasks
###


def print_map(map):
    for row in map:
        print(f'{row}\n')


def compare_maps(soln_map, stu_map):
    # Compare current stu_path with current soln_path
    for i, soln_row in enumerate(soln_map):
        if soln_row != stu_map[i]:
            return False

    return True


def validate_map(m, steps=None, path=None):
    print_map(m)
    if steps is not None:
        print(f'Steps: {steps}')
    if path is not None:
        print(f'Path: {path}')

    ans = input("Is this map valid? [y/Y/n/N] ")

    while True:
        if ans == "y" or ans == "n":
            break
        ans = input("Please enter y/Y/n/N ")

    return True if ans.lower() == "y" else False

###
# Task A: check that input and map match
###


def taskA(solution, answer):
    # Get our solution's map, without outer walls
    soln_map = []
    if(solution.readline().rstrip() == "--- Task 1 ---"):
        line = solution.readline().rstrip()
        while line != "--- Task 2 ---":
            soln_map.append(line)
            line = solution.readline().rstrip()

    # Get the student's map
    stu_map = []
    if(answer.readline().rstrip() == "--- Task 1 ---"):
        line = answer.readline().rstrip()
        while line != "--- Task 2 ---":
            stu_map.append(line)
            line = answer.readline().rstrip()

    # Check if they're the same
    correct_rows = 0
    for i, row in enumerate(soln_map):
        if(row == stu_map[i]):
            correct_rows += 1
        else:
            print(f'{bcolors.FAIL} Row {i} is incorrect! {bcolors.ENDC}')
            print(f'\tExpected:\n\t{row}\n\tGot:\n\t{stu_map[i]}\n')

    if(correct_rows == 11):
        # Full marks
        a_mark = 10
        colour = bcolors.OKGREEN
    elif(correct_rows > 0):
        # Maximum mark of 8
        a_mark = correct_rows * 2
        if(correct_rows > 8):
            a_mark = 8
        colour = bcolors.WARNING
    else:
        # Hardcoded or just incorrect map
        a_mark = 0
        colour = bcolors.FAIL

    print(f'{colour} Task A: {a_mark}/10 {bcolors.ENDC}')

###
# Task B: check all paths are provided
###


def get_paths(f):
    first_path = True
    paths = []
    line = f.readline().rstrip()
    while line != "--- Task 3 ---":
        # New path has started
        if "--- Path" in line:
            if first_path == True:
                # Ignore the first "--- Path" we encounter - path will be []
                first_path = False
            else:
                paths.append(path)

            path = []
        else:
            path.append(line)

        line = f.readline().rstrip()
    paths.append(path)  # Append final path
    return paths


def remove_duplicate_paths(paths):
    # Just remove duplicates manually
    new_paths = []
    for path in paths:
        if path not in new_paths:
            new_paths.append(path)

    return new_paths


def taskB(solution, answer):
    #! Note: this removes duplicate shortest paths from the students answer

    # Get all the shortest paths printed out in the solution
    soln_paths = get_paths(solution)

    # Get all the shortest paths printed out in the student answer
    stu_paths = get_paths(answer)

    # Remove duplicate paths in stu_paths
    stu_paths = remove_duplicate_paths(stu_paths)

    # Find the correct paths (in RIP time complexity)
    actual_correct_paths = len(soln_paths)
    correct_paths = 0
    for i, soln_path in enumerate(soln_paths):
        match_found = False

        # Find the same path in stu_paths, if it exists
        for stu_path in stu_paths:
            if compare_maps(soln_path, stu_path) == True:
                stu_paths.remove(stu_path)
                match_found = True
                break

        if match_found == True:
            correct_paths += 1
        else:
            print(
                f'{bcolors.FAIL} Could not find solution path {i+1} in student paths {bcolors.ENDC}')

    # If there are leftover paths - deal with this manually
    # All paths here are not the shortest, but you may be able to get marks anyway
    valid_paths = 0
    if len(stu_paths) != 0:
        print(
            f'{len(stu_paths)} paths in the student answer are either invalid or not the shortest path')

        for path in stu_paths:
            if validate_map(path):
                valid_paths += 1

    # Calculate the mark for this phase
    if correct_paths == actual_correct_paths:
        # Full marks
        b_mark = 50
        colour = bcolors.OKGREEN
    elif correct_paths > 0 or valid_paths > 0:
        # Partial marks
        b_mark = 0

        # +20 for the first shortest path, +4 for every shortest path after that
        first_path = True
        for i in range(correct_paths):
            b_mark += 20 if first_path else 4
            first_path = False

        # +10 for the first valid path, +2 for every one after that
        first_path = True
        for i in range(valid_paths):
            b_mark += 10 if first_path else 2
            first_path = False

        # Maximum marks obtainable is 40
        if(b_mark > 40):
            b_mark = 40

        colour = bcolors.WARNING
    else:
        # No marks
        b_mark = 0
        colour = bcolors.FAIL

    print(f'{colour} Task B: {b_mark}/50 {bcolors.ENDC}')


###
# Task C: check the least turns path is valid
###


def get_paths_and_steps(f):
    paths = []
    m = []
    line = f.readline().rstrip()

    while line != "--- Task 4 ---":
        if "Path: " in line:
            path = line.replace("Path: ", "")
            paths.append({
                "map": m,
                "path": path,
                "steps": steps,
            })
            m = []
        elif "Steps: " in line:
            steps = line.replace("Steps: ", "")
        else:
            m.append(line)

        line = f.readline().rstrip()

    return paths


def taskC(solution, answer):
    # Get all possible maps, paths and steps from the solution
    soln_paths = get_paths_and_steps(solution)

    # Get the least turns map from the student answer
    stu_paths = get_paths_and_steps(answer)

    if len(stu_paths) == 0:
        # No attempt made
        print(f'{bcolors.FAIL} Task C: 0/50 {bcolors.ENDC}')
        return

    stu_map = stu_paths[0]["map"]
    stu_steps = stu_paths[0]["steps"]
    stu_path = stu_paths[0]["path"]
    c_mark = 0

    for i in soln_paths:
        soln_map = i["map"]
        soln_steps = i["steps"]
        soln_path = i["path"]

        # Found a matching maze!
        if compare_maps(soln_map, stu_map):
            # Double check the path and steps are the same as well
            if soln_steps == stu_steps:
                if soln_path == stu_path:
                    # Everything is correct!
                    c_mark += 30
                else:
                    print(
                        f'{bcolors.FAIL} Wrong path. Got {stu_path}. Expected {soln_path} {bcolors.ENDC}')
                    # +5% for every 3 correct steps (consecutive)
                    for s_index, s in enumerate(stu_path):
                        if s == soln_path[s_index]:
                            if s_index % 3 == 0:
                                c_mark += 5
                        else:
                            break
                    c_mark = 15 if c_mark > 15 else c_mark
            else:
                # +10 for finding a shortest path with least turns
                print(
                    f'{bcolors.FAIL} Wrong number of steps. Got {stu_steps}. Expected {soln_steps} {bcolors.ENDC}')
                c_mark += 10

    # No match found - manually check if it is correct
    if c_mark == 0:
        print(
            f'Least turns path in the student answer is either invalid or not the shortest path')
        print(f'For reference, expecting {soln_steps} turns in the path')
        if validate_map(stu_map, steps=stu_steps, path=stu_path):
            c_mark += 20

    colour = bcolors.OKGREEN if c_mark == 30 else bcolors.WARNING
    colour = bcolors.FAIL if c_mark == 0 else colour

    print(f'{colour} Task C: {c_mark}/30 {bcolors.ENDC}')


###
# Task D: given the absolute path of the file, check if the path is correct
###

def taskD(answer):
    f = answer.readline().rstrip()
    path = answer.readline().rstrip()

    if "File: " not in f or "Path: " not in path:
        d_mark = 0
    else:
        d_mark = 0
        f = "./PathPlanFound.txt"
        path = path.replace("Path: ", "")
        with open(f, "r") as stu_file:
            stu_path = stu_file.readline().rstrip()
            if stu_path == path:
                d_mark += 10
            else:
                print(
                    f'{bcolors.FAIL} Wrong path. Got {stu_path}. Expected {path} {bcolors.ENDC}')
                # +2% for every 3 correct steps (consecutive)
                for s_index, s in enumerate(stu_path):
                    if s == path[s_index]:
                        if s_index % 3 == 0:
                            d_mark += 2
                    else:
                        break

                d_mark = 8 if d_mark > 8 else d_mark

    colour = bcolors.OKGREEN if d_mark == 10 else bcolors.WARNING
    colour = bcolors.FAIL if d_mark == 0 else colour
    print(f'{colour} Task D: {d_mark}/10 {bcolors.ENDC}')


# Generate our own answer
if platform.system() == 'Windows':
    os.system("winsln.exe > solution.txt")
elif platform.system() == 'Linux':
    os.system("./linuxsln > solution.txt")
else:
    os.system("./sln > solution.txt")

# This is where the actual marking happens
with open("solution.txt", "r") as solution:
    with open("answer.txt", "r") as answer:
        taskA(solution, answer)
        taskB(solution, answer)
        taskC(solution, answer)
        taskD(answer)
