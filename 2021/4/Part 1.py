

def extract_boards_and_numbers(raw_input:str):
    splitted = raw_input.split("\n\n")
    numbers = [int(num) for num in splitted[0].split(",")]
    boards = {}
    
    board_num = 1
    for board_data in splitted[1:]:
        rows = []
        columns = []
        
        raw_rows = board_data.split("\n")
        for raw_row in raw_rows:
            # Fix double spaces in middle of string
            raw_row = raw_row.replace("  ", " ")
            rows.append([int(num) for num in raw_row.strip().split(" ")])
                
        for n in range(0, len(rows)): # Maybe minus 1
            column = []
            for row in rows:
                column.append(row[n])
            columns.append(column)
                
        boards[board_num] = {"rows": rows, "columns": columns}
        board_num += 1
    return numbers, boards


def get_sum_of_all_unmarked_numbers(board:dict, used_numbers:list):
    total = 0
    for row in board["rows"]:
        for number in row:
            if number not in used_numbers:
                total += number
    
    return total * used_numbers[len(used_numbers)-1]


def check_boards_for_complete_row_or_column(boards:dict, used_numbers:list):
    for board_number, board in boards.items():
        for row in board["rows"]:
            if all(num in used_numbers for num in row):
                # Winner
                return True, board_number
        for column in board["columns"]:
            if all(num in used_numbers for num in column):
                # Winner
                return True, board_number
    
    return False, None
        
        
def bingo_game(numbers:list, boards:dict):
    used_numbers = []
    for number in numbers:
        used_numbers.append(number)
        winner_found, board_number = check_boards_for_complete_row_or_column(boards, used_numbers)
        if winner_found:
            return used_numbers, board_number
        
        

if __name__ == "__main__":
    # Load puzzle input.
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        raw_bingo = f.read()
    numbers, boards = extract_boards_and_numbers(raw_bingo)
    used_numbers, board_number = bingo_game(numbers, boards)
    final_score = get_sum_of_all_unmarked_numbers(boards[board_number], used_numbers)
    print("What will your final score be if you choose that board?")    
    print("Puzzle answer: ", final_score)