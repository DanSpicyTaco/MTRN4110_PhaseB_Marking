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


# Generate our own answer
os.system("./sln > solution.txt")


###
# Task A: check that input and map match
###
def taskA(solution, answer):
    # Get our solution's map, without outer walls
    soln_map = []
    if(solution.readline().rstrip() == "Start - Read map:"):
        line = solution.readline().rstrip()
        while line != "Done - Map read!":
            soln_map.append(line)
            line = solution.readline().rstrip()

    # Get the student's map
    stu_map = []
    if(answer.readline().rstrip() == "Start - Read map:"):
        line = answer.readline().rstrip()
        while line != "Done - Map read!":
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


def printMap(map):
    for row in map:
        print(f'{row}\n')


def compare_maps(soln_map, stu_map):
    # Compare current stu_path with current soln_path
    for i, soln_row in enumerate(soln_map):
        if soln_row != stu_map[i]:
            return False

    return True


def taskB(solution, answer):
    #! Note: this removes duplicate shortest paths from the students answer
    # Throw away first line - should be "Start - Find shortest paths:"
    solution.readline()
    answer.readline()

    # Get all the shortest paths printed out in the solution
    soln_paths = []
    line = solution.readline().rstrip()
    while line != "Done - Find shortest paths":
        # New path has started
        if "start path -" in line:
            soln_path = []
        elif "done path -" in line:
            soln_paths.append(soln_path)
        else:
            soln_path.append(line)

        line = solution.readline().rstrip()

    # Get all the shortest paths printed out in the student answer
    stu_paths = []
    line = answer.readline().rstrip()
    while line != "Done - Find shortest paths":
        # New path has started
        if "start path -" in line:
            stu_path = []
        elif "done path -" in line:
            stu_paths.append(stu_path)
        else:
            stu_path.append(line)

        line = answer.readline().rstrip()

    # Remove duplicate paths in stu_paths
    # Copied from SO (lol)
    stu_paths = sorted(map(list, set(map(tuple, stu_paths))))

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
                f'{bcolors.FAIL} Could not find solution path {i} in student paths {bcolors.ENDC}')

    # If there are leftover paths - deal with this manually
    # All paths here are not the shortest, but you may be able to get marks anyway
    valid_paths = 0
    if len(stu_paths) != 0:
        print(
            f'{len(stu_paths)} paths in the student answer are either invalid or not the shortest path')

        for path in stu_paths:
            printMap(path)
            ans = input("Is this path valid? [y/Y/n/N] ")

            while True:
                if ans == "y" or ans == "n":
                    break
                ans = input("Please enter y/Y/n/N ")

            if ans.lower() == "y":
                valid_paths += 1

    # Calculate the mark for this phase
    if correct_paths == actual_correct_paths:
        # Full marks
        b_mark = 50
        colour = bcolors.OKGREEN
    elif correct_paths > 0 or valid_paths > 0:
        # Partial marks
        b_mark = 0

        # +30 for the first shortest path, +10 for every shortest path after that
        first_path = True
        for i in range(correct_paths):
            b_mark += 30 if first_path else 10
            first_path = False

        # +15 for the first valid path, +5 for every one after that
        first_path = True
        for i in range(valid_paths):
            b_mark += 15 if first_path else 5
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

# TODO
###
# Task C: check the least turns path is valid
###

# TODO
###
# Task D: given the absolute path of the file, check if the path is correct
###


# This is where the actual marking happens
with open("solution.txt", "r") as solution:
    with open("answer.txt", "r") as answer:
        taskA(solution, answer)
        taskB(solution, answer)
