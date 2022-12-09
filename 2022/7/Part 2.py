filesystem = {}

def is_command(line:str):
    return line.startswith("$")

def is_dir(line:str):
    return line.startswith("dir")

def get_file_info(file_data:str):
    size, filename = file_data.split(" ")
    return int(size), filename

def get_current_path(path_list:list):
    if len(path_list) == 1:
        return "/"
    path = "/".join(path_list)
    fixed_path = path.replace("//", "/")
    return fixed_path

def parse_filesystem(filesystem_data:list):
    current_path = []
    for cli_output in filesystem_data:
        if is_command(cli_output):
            if cli_output == "$ ls":
                continue
            _, _command, directory = cli_output.split(" ")
            if directory == "..":
                current_path.pop(len(current_path)-1)
            else:
                current_path.append(directory)
                if filesystem.get(get_current_path(current_path)) is None:
                    filesystem[get_current_path(current_path)] = []
                    
        elif is_dir(cli_output):
            _, dir_name = cli_output.split(" ")
            cur_path = get_current_path(current_path)
            new_path = cur_path + f"/{dir_name}" if len(current_path) != 1 else cur_path + dir_name
            filesystem[new_path] = []
            filesystem[cur_path].append({"dir": new_path})
        else:
            size, filename = get_file_info(cli_output)
            cur_path = get_current_path(current_path)
            filesystem[cur_path].append({filename: int(size)})         
            

def get_size_of_directory(directory:str):
    total_size_of_dir = 0
    for data in filesystem[directory]:
        for item, content in data.items():
            if item == "dir":
                size_of_dir = get_size_of_directory(content)
                total_size_of_dir += size_of_dir
            else:
                total_size_of_dir += content
        
    return total_size_of_dir
    
def total_size_of_directories(filesystem_data:list):
    parse_filesystem(filesystem_data)
    return get_size_of_directory("/")

def find_directory_to_remove_to_make_space(filesystem_data:list):
    total_size = total_size_of_directories(filesystem_data)
    directories_to_make_space = list()
    max_filesystem_size = 70000000 - 30000000
    for directory in filesystem:
        size_of_dir = get_size_of_directory(directory)
        if (total_size - size_of_dir) <= max_filesystem_size:
            directories_to_make_space.append(size_of_dir)
    
    return min(directories_to_make_space)
            
            

if __name__ == "__main__":
    # Get filesystem data from input file
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        filesystem_data = [line.strip() for line in f.readlines()]

    print("Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?")
    print("Puzzle answer: ", find_directory_to_remove_to_make_space(filesystem_data))