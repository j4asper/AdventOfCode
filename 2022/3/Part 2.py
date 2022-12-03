from string import ascii_letters


letters_to_numbers = dict()
for n in range(0, 52):
    letters_to_numbers[ascii_letters[n]] = n + 1


def find_duplicates_in_rucksack_group(rucksack_group:list):
    for char in rucksack_group[0]:
        if char in rucksack_group[1] and char in rucksack_group[2]:
            return char

def divide_into_groups_of_three(all_rucksacks:list):
    rucksack_groups = list()
    current_rucksack_group = list()
    for rucksack in all_rucksacks:
        current_rucksack_group.append(rucksack.strip())
        if len(current_rucksack_group) == 3:
            rucksack_groups.append(current_rucksack_group.copy())
            current_rucksack_group.clear()
    return rucksack_groups

def get_priority_sum(rucksacks:list):
    total_sum = 0
    groups = divide_into_groups_of_three(rucksacks)
    for rucksack_group in groups:
        duplicate = find_duplicates_in_rucksack_group(rucksack_group)
        total_sum += letters_to_numbers[duplicate]
    
    return total_sum


if __name__ == "__main__":
    # First convert the input data to a list of rucksack_content.
    with open("2022\\3\\input.txt", "r") as f:
        rucksacks = f.readlines()
    
    print("Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?")
    print("Puzzle answer: ", get_priority_sum(rucksacks))