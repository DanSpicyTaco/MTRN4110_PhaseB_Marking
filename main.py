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
    if(solution.readline().strip() == "Start - Read map:"):
        line = solution.readline().strip()
        while line != "Done - Map read!":
            soln_map.append(line)
            line = solution.readline().strip()

    # Get the student's map
    stu_map = []
    if(answer.readline().strip() == "Start - Read map:"):
        line = answer.readline().strip()
        while line != "Done - Map read!":
            stu_map.append(line)
            line = answer.readline().strip()

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


def taskB(solution, answer):
    # Throw away first line - should be "Start - Find shortest paths:"
    solution.readline()
    answer.readline()

    # Get all the shortest paths printed out in the solution
    soln_paths = []
    line = solution.readline().strip()
    while line != "Done - Find shortest paths":
        # New path has started
        if "start path -" in line:
            soln_path = []
        elif "done path -" in line:
            soln_paths.append(soln_path)
        else:
            soln_path.append(line)

        line = solution.readline().strip()

    # Get all the shortest paths printed out in the student answer
    stu_paths = []
    line = answer.readline().strip()
    while line != "Done - Find shortest paths":
        # New path has started
        if "start path -" in line:
            stu_path = []
        elif "done path -" in line:
            stu_paths.append(stu_path)
        else:
            stu_path.append(line)

        line = answer.readline().strip()

    # Find the correct paths (in RIP time complexity)
    correct_paths = 0
    for i, soln_path in enumerate(soln_paths):
        match_found = True

        # Find the same path in stu_paths, if it exists
        for stu_path in stu_paths:
            # Compare current stu_path with current soln_path
            for j, soln_row in enumerate(soln_path):
                match_found = True
                if soln_row != stu_path[j]:
                    match_found = False
                    break

            # The current stu_path matches soln_path!
            if match_found == True:
                stu_paths.remove(stu_path)
                break

        if match_found == True:
            correct_paths += 1
            continue
        elif match_found == False:
            print(
                f'{bcolors.FAIL} Could not find solution path {i} in student paths {bcolors.ENDC}')

    # Calculate the mark for this phase
    if correct_paths == len(soln_paths):
        # Full marks
        b_mark = 50
        colour = bcolors.OKGREEN
    elif correct_paths > 0:
        # TODO - figure out how to calculate this!
        # Partial marks
        b_mark = correct_paths
        colour = bcolors.OKGREEN
    else:
        # No marks
        b_mark = 0
        colour = bcolors.FAIL

    print(f'{colour} Task B: {b_mark}/50 {bcolors.ENDC}')

# TODO
# Task C: check the least turns path is valid

# TODO
# Task D: given the absolute path of the file, check if the path is correct


with open("solution.txt", "r") as solution:
    with open("answer.txt", "r") as answer:
        taskA(solution, answer)
        taskB(solution, answer)
