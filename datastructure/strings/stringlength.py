def string_length(text, recursive=False):
    if text == "":
        return 0
    if not recursive:
        length = 0
        for ch in text:
            length += 1
        return length
    return 1 + string_length(text[1:], recursive=True)


if __name__ == '__main__':
    assert(string_length("")) == 0
    assert (string_length("", recursive=True)) == 0
    assert (string_length("ciao")) == 4
    assert (string_length("ciao", recursive=True)) == 4