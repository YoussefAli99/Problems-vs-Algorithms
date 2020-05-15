def rotated_array_search(input_list, number, mid=0):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    l = len(input_list)
    low = 0
    high = l
    while low <= high:
        pv = (low+high) // 2
        if input_list[0] < input_list[l-1] or pv == l-1:
            pv = 0
            break
        if input_list[pv-1] > input_list[pv]:
            break
        elif input_list[0] < input_list[pv]:
            low = pv
        elif input_list[0] > input_list[pv]:
            high = pv

    if input_list[pv] <= number and input_list[l-1] >= number:
        low = pv
        high = l
    else:
        low = 0
        high = pv

    while low <= high:
        pv = (low+high) // 2
        if input_list[pv] == number:
            return pv
        elif input_list[pv] < number:
            low = pv+1
        else:
            high = pv-1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8], 10])