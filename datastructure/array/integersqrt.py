from math import sqrt


def integer_square_root(k):
    j = k // 2
    j_sqrt = sqrt(j)
    while j_sqrt <= k:
        previous_j = j
        j = j + (k - j) // 2
        j_sqrt = sqrt(j)
        delta_j = j - previous_j
        exact = round(j_sqrt) * round(j_sqrt) == k
        if exact:
            return round(j_sqrt)
        if delta_j == 0:
            return int(j_sqrt)
    return int(j_sqrt)


if __name__ == '__main__':
    assert (integer_square_root(625)) == 25
    assert (integer_square_root(1000)) == 31
    assert(integer_square_root(300)) == 17
    assert (integer_square_root(12)) == 3
