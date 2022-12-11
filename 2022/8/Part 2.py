def get_score_by_list(trees:list, tree_height:int):
    score = 0
    for tree in trees:
        score += 1
        if tree <= tree_height:
            if tree == tree_height:
                break
        else:
            break

    return score
    
    
def get_scenic_score(data:list, line_index:int, index:int):
    top, left, right, buttom = list(), list(), list(), list()
    for line in data:
        
        if data.index(line) < line_index:
            top.append(int(line[index]))
        elif data.index(line) > line_index:
            buttom.append(int(line[index]))
        else:
            line_of_trees = data[line_index]
            for i in range(0, len(line_of_trees)):
                if i == index:
                    continue
                if i < index:
                    left.append(int(line_of_trees[i]))
                else:
                    right.append(int(line_of_trees[i]))
    
    tree_int = int(data[line_index][index])
    top.reverse()
    top_scenic = get_score_by_list(top, tree_int)
    left.reverse()
    left_scenic = get_score_by_list(left, tree_int)
    right_scenic = get_score_by_list(right, tree_int)
    buttom_scenic = get_score_by_list(buttom, tree_int)
        
    return top_scenic * left_scenic * right_scenic * buttom_scenic


def get_highest_scenic_score_in_line(data:list, line_index:int):
    highest_scenic_scores = list()
    #for tree in data[line_index]:
    for i in range(1, len(data[line_index]) - 1):
        score = get_scenic_score(data, line_index, i)
        highest_scenic_scores.append(score)
    
    return max(highest_scenic_scores)


def get_highest_scenic_score(data:list):
    scenic_scores = list()
    
    for i in range(1, len(data)-1):
        highest_scenic_score_in_line = get_highest_scenic_score_in_line(data, i)
        scenic_scores.append(highest_scenic_score_in_line)
    
    return max(scenic_scores)


if __name__ == "__main__":
    # Get data from input file
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    print("Consider each tree on your map. What is the highest scenic score possible for any tree?")
    print("Puzzle answer: ", get_highest_scenic_score(data))