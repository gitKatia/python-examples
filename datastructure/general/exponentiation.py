from math import pow


def power(base, exponent, recursive=False):
    if not recursive:
        return pow(base, exponent)
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


if __name__ == '__main__':
    assert (power(2, 1)) == 2
    assert (power(2, 1, recursive=True)) == 2
    assert (power(2, 2)) == 4
    assert (power(2, 2, recursive=True)) == 4
    assert (power(2, - 1)) == 0.5
    assert (power(2, - 1, recursive=True)) == 0.5
    assert (power(0, 1)) == 0
    assert (power(0, 1, recursive=True)) == 0