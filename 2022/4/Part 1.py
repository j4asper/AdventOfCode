
def get_assignment_range(assignment):
    assignment_range = list()
    a = int(assignment.split("-")[0])
    b = int(assignment.split("-")[1])
    for n in range(a, b+1):
        assignment_range.append(n)
    return assignment_range


def is_contained_in_assignment_pair(assignment_1:list, assignment_2:list):
    return all(item in assignment_1 for item in assignment_2) or all(item in assignment_2 for item in assignment_1)


def amount_of_fully_contained_assignments(assignments:list):
    amount = 0
    for assignment_pair in assignments:
        assignment_1, assignment_2 = assignment_pair.strip().split(",")
        assignment_1_range = get_assignment_range(assignment_1)
        assignment_2_range = get_assignment_range(assignment_2)
        if is_contained_in_assignment_pair(assignment_1_range, assignment_2_range):
            amount += 1
    return amount


if __name__ == "__main__":
    # First convert the input data to a list of assignment strings.
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        assignments = f.readlines()
    
    print("In how many assignment pairs does one range fully contain the other?")
    print("Puzzle answer: ", amount_of_fully_contained_assignments(assignments))