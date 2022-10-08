def closest_number(a, target):
    if len(a) == 0:
        return None
    if len(a) == 1 or target < a[0]:
        return a[0]
    if len(a) == 2:
        distance_0 = abs(a[0] - target)
        distance_1 = abs(a[1] - target)
        return a[0] if distance_0 < distance_1 else a[1]
    if target > a[-1]:
        return a[-1]
    mid = len(a) // 2
    if target == a[mid]:
        return a[mid]
    elif target > a[mid]:
        b = a[mid + 1:]
        return closest_number(b, target)
    else:
        b = a[:mid + 1]
        return closest_number(b, target)


if __name__ == '__main__':

    # Given
    data_list = [1, 2, 4, 5, 6, 6, 8, 9]

    # When - Then
    assert (closest_number(data_list, -1)) == 1
    assert (closest_number(data_list, 0)) == 1
    assert (closest_number(data_list, 1)) == 1
    assert (closest_number(data_list, 2)) == 2
    assert (closest_number(data_list, 3)) == 4
    assert (closest_number(data_list, 4)) == 4
    assert (closest_number(data_list, 5)) == 5
    assert (closest_number(data_list, 6)) == 6
    assert (closest_number(data_list, 7)) == 8
    assert (closest_number(data_list, 8)) == 8
    assert (closest_number(data_list, 9)) == 9
    assert (closest_number(data_list, 11)) == 9

    # Given
    data_list = [2, 5, 6, 7, 8, 8, 9]

    # When - Then
    assert (closest_number(data_list, 1)) == 2
    assert (closest_number(data_list, 2)) == 2
    assert (closest_number(data_list, 3)) == 2
    assert (closest_number(data_list, 4)) == 5
    assert (closest_number(data_list, 5)) == 5
    assert (closest_number(data_list, 6)) == 6
    assert (closest_number(data_list, 5)) == 5
    assert (closest_number(data_list, 6)) == 6
    assert (closest_number(data_list, 7)) == 7
    assert (closest_number(data_list, 8)) == 8
    assert (closest_number(data_list, 9)) == 9
    assert (closest_number(data_list, 10)) == 9
