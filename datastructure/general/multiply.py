def multiply(x, y, recursive=False):
    if not recursive:
        return x * y
    if x == 0 or y == 0:
        return 0
    if x < y:
        return multiply(y, x)
    return x + multiply(x, y - 1)


if __name__ == '__main__':
    assert(multiply(3, 4)) == 12
    assert (multiply(3, 4, recursive=True)) == 12
    assert (multiply(5, 3)) == 15
    assert (multiply(5, 3, recursive=True)) == 15
    assert (multiply(500, 2000)) == 1000000
    assert (multiply(500, 2000, recursive=True)) == 1000000
    assert (multiply(34, 0)) == 0
    assert (multiply(34, 0, recursive=True)) == 0