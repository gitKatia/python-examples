def find_uppercase(text, recursive=False):
    if not recursive:
        b = [ch for ch in text if ch.isupper()]
        return b[0] if len(b) > 0 else None
    if len(text) == 0:
        return None
    if text[0].isupper():
        return text[0]
    else:
        return find_uppercase(text[1:], recursive=True)


if __name__ == '__main__':

    # When - Then
    assert (find_uppercase("")) is None
    assert (find_uppercase("george")) is None
    assert (find_uppercase("isYours")) == 'Y'
    assert (find_uppercase("", recursive=True)) is None
    assert (find_uppercase("george", recursive=True)) is None
    assert (find_uppercase("isYours", recursive=True)) == 'Y'
