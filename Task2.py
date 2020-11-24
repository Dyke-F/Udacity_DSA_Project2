import os


def find_files(suffix, path):
    """ Main function, storing all files in a given root (path) ending with suffix (".c") """
    output = []
    return _recfiles(suffix, path, output)

def _recfiles(suffix, path, output):
    """ Recursive function, iterates through the given path and checks all its subdirectories.
        Base case: If an input path to this function is a file, check if it ends with suffix and
        eventuallly append it to the output list
        Else: Create a next_path list with all subdirectories of the current path. Then recursively
        iterate through each subpath until hitting the base condition.
    """
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            end_idx = path.rfind("/")
            filename = path[end_idx+1:]
            output.append(filename)

    else:
        next_path = [path+"/"+element for element in os.listdir(path)]
        for subpath in next_path:
            _recfiles(suffix, subpath, output)
    
    return output


path = os.path.join(os.getcwd()+"testdir")


### Test cases ###

print(find_files(".c", path))
# ['b.c', 't1.c', 'a.c', 'a.c']

print(find_files(".h", path))
# ['b.h', 'a.h', 't1.h', 'a.h']

print(find_files(" ", path))
# []

print(find_files("", path))
# ['.DS_Store', '.gitkeep', '.DS_Store', 'b.h', 'b.c', 't1.c', '.gitkeep', 'a.h', 'a.c', 't1.h', 'a.h', 'a.c']

print(find_files(".xxx", path))
# []
