import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    for entry in (os.listdir(path)):
        if entry.endswith(".c"):
            print(entry)
        elif os.path.isdir(path +'/'+ entry):
            find_files('.c', path +'/'+ entry)


find_files(".c", "/Users/otrejo/Downloads/testdir")
