def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    string = ""

    for char in phrase:
        if char == to_swap.upper() or char == to_swap.lower():
            string += char.swapcase()
        else:
            string += char

    return string
