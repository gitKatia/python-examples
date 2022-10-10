def peak(a):
    size_a = len(a)
    if size_a <= 2:
        return None
    if size_a == 3:
        return a[1]
    mid = len(a) // 2
    mid_a = a[mid]
    if mid_a > a[mid + 1] and mid_a > a[mid - 1]:
        return mid_a
    elif mid_a <= a[mid + 1]:
        b = a[mid:]
        return peak(b)
    else:
        b = a[:mid + 1]
        return peak(b)


if __name__ == '__main__':

    # When - Then
    assert (peak([])) is None
    assert (peak([1])) is None
    assert (peak([1, 2])) is None
    assert (peak([1, 2, 0])) == 2
    assert (peak([1, 2, 3, 4, 3, 2, 1])) == 4
    assert (peak([1, 5, 4, 3, 2, 1, 0])) == 5
    assert (peak([1, 2, 3, 4, 5, 6, 1])) == 6
