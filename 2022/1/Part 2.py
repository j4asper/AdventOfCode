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


def find_sum_of_3_largest_amounts_of_calories(puzzle_input:list):
    total_calories = make_list_of_total_calories(puzzle_input)
    top_3 = list()
    
    for _n in range(0, 3):
        largest_amount = max(total_calories)
        top_3.append(largest_amount)
        total_calories.remove(largest_amount)
    return sum(top_3)

if __name__ == "__main__":
    # First convert the input data to a list of measurements.
    with open("2022\\1\\input.txt", "r") as f:
        calories = f.readlines()
    
    print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
    print("Puzzle answer: ", find_sum_of_3_largest_amounts_of_calories(calories))