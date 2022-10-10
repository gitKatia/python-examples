def find_min_index(a):
    return a.index(min(a))


if __name__ == '__main__':
    assert (find_min_index([5, 6, 7, 1, 2, 3, 5])) == 3
    assert (find_min_index([1, 2, 3, 4, 5, 6, 7])) == 0
    assert (find_min_index([4, 5, 6, 7, 1, 2, 3])) == 4
    assert (find_min_index([6, 7, 1, 2, 3, 4, 5])) == 2
    assert (find_min_index([7, 1, 2, 3, 4, 5, 6])) == 1
    assert (find_min_index([3, 4, 5, 6, 7, 1, 2])) == 5
    assert (find_min_index([2, 3, 4, 5, 6, 7, 1])) == 6