# @Author: otrejo
# @Date:   2020-03-05T00:12:05-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-21T21:58:45-04:00



import os

def find_files(suffix, path, path_files):
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
    #path_files = []
    for entry in (os.listdir(path)):
        if entry.endswith(".c"):
            path_files.append(path)
        elif os.path.isdir(path +'/'+ entry):
            find_files('.c', path +'/'+ entry, path_files)
    #print(path_files)
    return path_files

print(find_files(".c", "testdir", []))
