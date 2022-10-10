def first_occurrence(a, target):
    if len(a) == 0:
        return - 1
    b = [index for (index, item) in enumerate(a) if item == target]
    return b[0] if len(b) > 0 else - 1


if __name__ == '__main__':

    # When - Then
    assert (first_occurrence([], 3)) == - 1
    assert (first_occurrence([3], 3)) == 0
    assert (first_occurrence([3, 3, 0], 3)) == 0
    assert (first_occurrence([3, 3, 3], 3)) == 0
    assert (first_occurrence([1, 2, 3], 3)) == 2
    assert (first_occurrence([1, 2, 3, 4], 3)) == 2
