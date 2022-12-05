from string import ascii_uppercase

stacks = dict()

def parse_stacks(stacks_and_movements:list):
    for line in stacks_and_movements:
        # Check if line contains brackets to check if it's still at the stacks
        if "[" not in line:
            break
        # One stack take up 3 chars, between each stack there will be 1 space.
        num_of_spaces = 0
        current_stack = 1
        line = line.replace("\n", "")
        for char in line:
            if num_of_spaces == 3:
                num_of_spaces = 0
                current_stack += 1
                continue
            num_of_spaces += 1
            if char in ascii_uppercase:
                if stacks.get(current_stack) is None:
                    stacks[current_stack] = []
                stacks[current_stack].append(char)
    # Reverse all lists because index 0 will be the top crate, it's easier if it's the last index
    for stack_num in stacks:
        stacks[stack_num].reverse()
            

def get_movements(stacks_and_movements:list):
    movements = list()
    for line in stacks_and_movements:
        if not line.startswith("move"):
            continue
        
        _, amount, _, from_stack, _, to_stack = line.split(" ")
        movements.append((int(amount), int(from_stack), int(to_stack)))
    return movements


def move_crate(amount:int, from_stack:int, to_stack:int):
    for n in range(1, amount+1):
        top_crate_index = len(stacks[from_stack]) - 1
        top_crate = stacks[from_stack].pop(top_crate_index)
        stacks[to_stack].append(top_crate)
        

def get_crates_on_top_of_each_stack(stacks_and_movements:list):
    parse_stacks(stacks_and_movements)
    movements = get_movements(stacks_and_movements)
    # Start moving crates
    for movement in movements:
        move_crate(movement[0], movement[1], movement[2])
    
    sorted_stack_numbers = sorted(stacks.keys())
    top_crates = list()
    for stack_num in sorted_stack_numbers:
        top_crates.append(stacks[stack_num][len(stacks[stack_num])-1])
    
    return "".join(top_crates)
    
    

if __name__ == "__main__":
    # First convert the input data to a list of stacks and movements.
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        stacks_and_movements = f.readlines()
    
    print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
    print("Puzzle answer: ", get_crates_on_top_of_each_stack(stacks_and_movements))