def linear_search(data, target):
    for item in data:
        if item == target:
            return True
    return False


def binary_search(data, target):
    left_index = 0
    right_index = len(data) - 1
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        mid_index_data = data[mid_index]
        if target == mid_index_data:
            return True
        elif target < mid_index_data:
            right_index = right_index - 1
        else:
            left_index = left_index + 1
    return False


def binary_search_recursive(data, target, left_index, right_index):
    if left_index > right_index:
        return False
    mid_index = (left_index + right_index) // 2
    mid_index_data = data[mid_index]
    if target == mid_index_data:
        return True
    elif target < mid_index_data:
        return binary_search_recursive(data, target, left_index, mid_index - 1)
    else:
        return binary_search_recursive(data, target, mid_index + 1, right_index)


if __name__ == '__main__':
    data_list = [1, 3, 5, 6, 7, 9, 10, 15]
    print(binary_search(data_list, 0))
    print(binary_search(data_list, 1))
    print(binary_search(data_list, 9))
    print(binary_search(data_list, 8))
    print(binary_search(data_list, 15))
    print(binary_search(data_list, 16))
    print("----")
    print(binary_search_recursive(data_list, 0, 0, 7))
    print("1", binary_search_recursive(data_list, 1, 0, 7))
    print("9", binary_search_recursive(data_list, 9, 0, 7))
    print("8", binary_search_recursive(data_list, 8, 0, 7))
    print("15", binary_search_recursive(data_list, 15, 0, 7))
    print(binary_search_recursive(data_list, 16, 0, 7))
