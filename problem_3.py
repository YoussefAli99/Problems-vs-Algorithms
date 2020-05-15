def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    inp = len(input_list)
    if inp <= 1:
        return [-1, -1]

    freq = [0] * 10
    for n in input_list:
        freq[n] += 1

    list1 = list()
    list2 = list()
    f = 2 if inp % 2 != 0 else 1
    for i in range(9, -1, -1):
        while freq[i]:
            if f:
                list1.append(str(i))
                f -= 1
            else:
                f += 1
                list2.append(str(i))
            freq[i] -= 1
    return [int(''.join(list1)), int(''.join(list2))]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])