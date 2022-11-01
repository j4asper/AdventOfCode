
def submarine_controller(commands:list):
    """Controls the submarine depth and horizontal position depending on the list of commands

    Args:
        commands (list): List of submarine movement commands

    Returns:
        int horizontal_position: The horizontal position of the submarine
        int depth: The depth of the submarine
    """
    
    horizontal_position = 0
    depth = 0
    aim = 0
    
    for command in commands:
        command, amount = command.split(" ")
        amount = int(amount)
        match command:
            case "forward":
                horizontal_position += amount
                depth += aim * amount
            case "up":
                aim -= amount
            case "down":
                aim += amount
    
    return horizontal_position, depth
        


if __name__ == "__main__":
    # First convert the input data to a list of commands.
    with open("2021\\2\\input.txt", "r") as f:
        commands = f.readlines()
    
    print("What do you get if you multiply your final horizontal position by your final depth?")
    horizontal_position, depth = submarine_controller(commands)
    
    print("Puzzle answer: ", horizontal_position*depth)