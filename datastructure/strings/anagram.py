def is_anagram(text1, text2):
    if len(text1) == 0 and len(text2) == 0:
        return True
    if len(text1) != len(text2):
        return False
    for ch in text1:
        if text1.count(ch) != text2.count(ch):
            return False
    return True


if __name__ == '__main__':
    assert(is_anagram("", "")) is True
    assert (is_anagram("ac", "acc")) is False
    assert (is_anagram("night", "thing")) is True

