def make_list_of_total_calories(calories_input:list):
    total_calories = list()
    
    current_list_of_calories = list()
    for calorie_line in calories_input:
        if calorie_line != "\n":
            current_list_of_calories.append(int(calorie_line))
        else:
            total_calories.append(sum(current_list_of_calories))
            current_list_of_calories.clear()
    
    return total_calories


def find_largest_amount_of_calories(puzzle_input:list):
    total_calories = make_list_of_total_calories(puzzle_input)
    return max(total_calories)

if __name__ == "__main__":
    # First convert the input data to a list of calorie amounts.
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        calories = f.readlines()
    
    print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
    print("Puzzle answer: ", find_largest_amount_of_calories(calories))