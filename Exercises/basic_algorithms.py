# @Author: otrejo
# @Date:   2020-03-05T17:23:35-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-05T17:35:48-05:00

# Recursive binary search using recursion
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    
