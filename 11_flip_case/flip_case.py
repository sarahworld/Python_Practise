def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    out=""
    for elem in phrase:
        if (to_swap.lower() == elem.lower()):
            elem = elem.swapcase()

        out += elem
            

    return out

print(flip_case('Aaaahhh', 'a'))
