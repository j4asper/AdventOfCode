def amount_of_surrounding_trees(data:list):
    return (len(data) * 2) + ((len(data[0]) - 2) * 2)


def get_tree_directions(data:list, line_index:int, index:int):
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
                    
    return top, left, right, buttom
                
    

def find_visible_trees_in_line(data:list, line_index:int):
    visible_trees = 0
    #for tree in data[line_index]:
    for i in range(1, len(data[line_index]) - 1):
        top, left, right, buttom = get_tree_directions(data, line_index, i)
        max_values = [max(top), max(left), max(right), max(buttom)]
        if any(value < int(data[line_index][i]) for value in max_values):
            visible_trees += 1
    
    return visible_trees


def find_amount_of_visible_trees(data:list):
    amount_of_visible_trees = 0
    amount_of_visible_trees += amount_of_surrounding_trees(data)
    
    for i in range(1, len(data)-1):
        amount_of_visible_trees += find_visible_trees_in_line(data, i)
    
    return amount_of_visible_trees
        

if __name__ == "__main__":
    # Get data from input file
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    print("Consider your map; how many trees are visible from outside the grid?")
    print("Puzzle answer: ", find_amount_of_visible_trees(data))