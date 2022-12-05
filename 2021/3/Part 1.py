

def get_most_common_bit(binary_list:list, index:int):
    # Rather than making one_count and zero_count variables, we can check if the amount of zeros is larger og less than half the amount of entries in binary_list to decide which is the most common
    half_list_entries = len(binary_list)/2
    number_of_zeros = 0
    for binary_string in binary_list:
        if binary_string[index] == "0":
            number_of_zeros += 1
    
    return 0 if number_of_zeros > half_list_entries else 1
    
def calculate_power_consumption(binary_list:list):
    gamma_rate = []
    epsilon_rate = []
    
    binary_string_length = len(binary_list[0])
    for index in range(0, binary_string_length-1):
        bit = get_most_common_bit(binary_list, index)
        if bit == 0:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")
    
    
    gamma_rate_int = int("".join(gamma_rate), 2)
    epsilon_rate_int = int("".join(epsilon_rate), 2)
    return gamma_rate_int * epsilon_rate_int
    
    
    

if __name__ == "__main__":
    # First convert the input data to a list of binary numbers. Input is not sanitized, i realized when making part 2
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        binary_list = f.readlines()
    
    print("What is the power consumption of the submarine?")    
    print("Puzzle answer: ", calculate_power_consumption(binary_list))