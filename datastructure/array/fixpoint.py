def fix_point(a, binary_search=False):
    if binary_search:
        return fix_point_binary_search(a)
    # Standard is linear search
    b = [item for (index, item) in enumerate(a) if item == index]
    return None if len(b) == 0 else b[0]


def fix_point_binary_search(a):
    size_a = len(a)
    if size_a == 0:
        return None
    if a[0] == 0:
        return a[0]
    if a[-1] == size_a - 1:
        return a[-1]
    mid = size_a // 2
    mid_a = a[mid]
    if mid_a == mid:
        return mid_a
    elif mid_a < mid:
        b = a[mid:]
        return fix_point_binary_search(b)
    else:
        b = a[:mid - 1]
        return fix_point_binary_search(b)


if __name__ == '__main__':

    # When - Then
    assert (fix_point([0, 1, 2, 3, 4, 5, 6, 7])) == 0
    assert (fix_point([0, 1, 2, 3, 4, 5, 6, 7], binary_search=True)) == 0
    assert (fix_point([])) is None
    assert (fix_point([], binary_search=True)) is None
    assert (fix_point([1, 2])) is None
    assert (fix_point([1, 2], binary_search=True)) is None
    assert (fix_point([-5, 0, 2])) == 2
    assert (fix_point([-5, 0, 2], binary_search=True)) == 2
    assert (fix_point([-5, 1, 2])) == 1
    assert (fix_point([-5, 1, 2], binary_search=True)) == 2
