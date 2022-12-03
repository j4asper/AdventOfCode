def get_most_common_bit(binary_list:list, index:int):
    # Rather than making one_count and zero_count variables, we can check if the amount of zeros is larger og less than half the amount of entries in binary_list to decide which is the most common
    half_list_entries = len(binary_list)/2
    number_of_zeros = 0
    for binary_string in binary_list:
        if binary_string[index] == "0":
            number_of_zeros += 1
    
    return 0 if number_of_zeros > half_list_entries else 1, number_of_zeros == half_list_entries


def get_oxygen_generator_rating(binary_list:list):
    binary_list_copy = binary_list.copy()
    
    binary_string_length = len(binary_list[0])
    for i in range(0, binary_string_length):
        if len(binary_list_copy) == 1:
            break
        common_bit, same_amount = get_most_common_bit(binary_list_copy, i)
        # Same amount AKA same number of 0's and 1's
        if same_amount:
            common_bit = 1
        for binary_string in binary_list_copy.copy():
            if binary_string[i] != str(common_bit):
                binary_list_copy.remove(binary_string)
    return int(binary_list_copy[0], 2)
            
        

def get_CO2_scrubber_rating(binary_list:list):
    binary_list_copy = binary_list.copy()
    
    binary_string_length = len(binary_list[0])
    for i in range(0, binary_string_length):
        if len(binary_list_copy) == 1:
            break
        common_bit, same_amount = get_most_common_bit(binary_list_copy, i)
        # Same amount AKA same number of 0's and 1's
        least_common_bit = 0 if common_bit == 1 else 1
        if same_amount:
            least_common_bit = 0
        for binary_string in binary_list_copy.copy():
            if binary_string[i] != str(least_common_bit):
                binary_list_copy.remove(binary_string)
    return int(binary_list_copy[0], 2)


def get_life_support_rating(binary_list:list):
    oxygen_generator_rating = get_oxygen_generator_rating(binary_list)
    CO2_scrubber_rating = get_CO2_scrubber_rating(binary_list)
    return oxygen_generator_rating * CO2_scrubber_rating
    

if __name__ == "__main__":
    # First convert the input data to a list of binary numbers.
    with open("2021\\3\\input.txt", "r") as f:
        binary_list = [binary.strip() for binary in f.readlines()]
    
    print("What is the life support rating of the submarine?")    
    print("Puzzle answer: ", get_life_support_rating(binary_list))