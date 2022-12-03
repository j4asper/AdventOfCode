from string import ascii_letters


letters_to_numbers = dict()
for n in range(0, 52):
    letters_to_numbers[ascii_letters[n]] = n + 1


def get_half(string:str):
    string1, string2 = string[:len(string)//2], string[len(string)//2:]
    return string1, string2

def find_duplicates_in_rucksack_compartments(compartment_1:str, compartment_2:str):
    for char in compartment_1:
        if char in compartment_2:
            return char

def get_priority_sum(rucksacks:list):
    total_sum = 0
    for rucksack in rucksacks:
        compartment_1, compartment_2 = get_half(rucksack)
        duplicate = find_duplicates_in_rucksack_compartments(compartment_1, compartment_2)
        total_sum += letters_to_numbers[duplicate]
    
    return total_sum


if __name__ == "__main__":
    # First convert the input data to a list of rucksack_content.
    with open("2022\\3\\input.txt", "r") as f:
        rucksacks = f.readlines()
    
    print("Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?")
    print("Puzzle answer: ", get_priority_sum(rucksacks))