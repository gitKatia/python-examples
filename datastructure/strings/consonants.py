def count_consonants(text, recursive=False):
    vowels = "aeiouAEIOU"
    if not recursive:
        b = [ch for ch in text if ch.isalpha() and ch not in vowels]
        return len(b)
    if text == "":
        return 0
    first_char = text[0]
    if first_char.isalpha() and first_char not in vowels:
        return 1 + count_consonants(text[1:], recursive=True)
    else:
        return count_consonants(text[1:], recursive=True)


if __name__ == '__main__':
    assert(count_consonants("")) == 0
    assert (count_consonants("", recursive=True)) == 0
    assert (count_consonants(" ")) == 0
    assert (count_consonants(" ", recursive=True)) == 0
    assert (count_consonants("a")) == 0
    assert (count_consonants("a", recursive=True)) == 0
    assert (count_consonants("aBCbc")) == 4
    assert (count_consonants("aBCbc", recursive=True)) == 4