def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True
    if len(text) == 2:
        return text[0] == text[1]
    mid = len(text) // 2
    text_left = text[:mid]
    if len(text) % 2 == 0:
        text_right_reversed = text[mid:][::-1]
    else:
        text_right_reversed = text[mid + 1:][::-1]
    return text_left == text_right_reversed


if __name__ == '__main__':
    assert (is_palindrome("abba")) is True
    assert (is_palindrome("radar")) is True
    assert (is_palindrome("")) is True
    assert (is_palindrome("a")) is True
    assert (is_palindrome("aa")) is True
    assert (is_palindrome("hey")) is False

