def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
    ans = [-float('inf'), float('inf')]
    for n in ints:
        if n > ans[0]:
            ans[0] = n
        if n < ans[1]:
            ans[1] = n
    return (ans[1], ans[0])

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max_by_sorting([0])) else "Fail")
print ("Pass" if (None == get_min_max_by_sorting([])) else "Fail")