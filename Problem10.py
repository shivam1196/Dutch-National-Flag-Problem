def sort_012(input_list):
    start = 0
    middle = 0
    end = len(input_list) - 1
    while middle <= end:
        if input_list[middle] == 0:
            # swap
            temp = input_list[start]
            input_list[start] = input_list[middle]
            input_list[middle] = temp

            start = start + 1
            middle = middle + 1
        elif input_list[middle] == 1:
            middle = middle + 1
        else:
            # swap
            temp = input_list[middle]
            input_list[middle] = input_list[end]
            input_list[end] = temp

            end = end - 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    test_function([])
