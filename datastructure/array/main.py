import bisect
if __name__ == '__main__':
    # Where to insert the element to maintain the list sorted
    assert(bisect.bisect_left([], 4)) == 0
    assert (bisect.bisect_left([1], 4)) == 1
    assert (bisect.bisect_left([1, 2, 3, 5], 4)) == 3
    assert (bisect.bisect_left([1, 2, 3, 4, 5], 4)) == 3
    # To the right. Same as bisect
    assert (bisect.bisect_right([], 4)) == 0
    assert (bisect.bisect_right([1], 4)) == 1
    assert (bisect.bisect_right([1, 2, 3, 5], 4)) == 3
    assert (bisect.bisect_right([1, 2, 3, 4, 5], 4)) == 4
    # insort_left and insort_right
