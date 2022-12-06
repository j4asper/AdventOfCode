def duplicate_in_list(four_chars:list):
    for char in four_chars:
        occurrences = four_chars.count(char)
        if occurrences != 1:
            return True
    return False

def find_marker(datastream_buffer:str):
    start_of_packet_marker = 1
    four_chars = list()
    for char in datastream_buffer:
        if start_of_packet_marker > 14:
            four_chars.pop(0)
        four_chars.append(char)
        if len(four_chars) == 14:
            duplicate = duplicate_in_list(four_chars)
            if not duplicate:
                return start_of_packet_marker
        start_of_packet_marker += 1
            

if __name__ == "__main__":
    # Get datastream buffer from input file
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        datastream_buffer = f.readline()
    
    print("How many characters need to be processed before the first start-of-message marker is detected?")
    print("Puzzle answer: ", find_marker(datastream_buffer))