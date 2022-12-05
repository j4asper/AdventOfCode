# A and X = Rock
# B and Y = Paper
# C and Z  = Scissors

def find_winner_of_match_and_get_person_2_points(person_1:str, person_2:str):
    point_table = {
        "A": 1, "X": 1,
        "B": 2, "Y": 2,
        "C": 3, "Z": 3,
        "draw": 3, "won": 6
    }
    
    convert_table = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    
    # Draw
    if convert_table[person_1] == person_2:
        return point_table["draw"] + point_table[person_2]
    
    match person_1:
        case "A":
            match person_2:
                case "Y":
                    return point_table["won"] + point_table[person_2]
                case "Z":
                    return point_table[person_2]
        case "B":
            match person_2:
                case "X":
                    return point_table[person_2]
                case "Z":
                    return point_table["won"] + point_table[person_2]
        case "C":
            match person_2:
                case "Y":
                    return point_table[person_2]
                case "X":
                    return point_table["won"] + point_table[person_2]


def play_rock_paper_scissors(strategy_input:list):
    # Total score is person 2's score
    total_score = 0

    for strategy in strategy_input:
        person_1, person_2 = strategy.strip().split(" ")
        person_2_score = find_winner_of_match_and_get_person_2_points(person_1, person_2)
        total_score += person_2_score
    
    return total_score


if __name__ == "__main__":
    # First convert the input data to a list of strategies.
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        strategy_input = f.readlines()
    
    print("What would your total score be if everything goes exactly according to your strategy guide?")
    print("Puzzle answer: ", play_rock_paper_scissors(strategy_input))