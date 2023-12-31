def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    count = {}

    # for letter in phrase:
    #     if count.get(letter):  # check alt syntax
    #         count[letter] += 1
    #     else:
    #         count[letter] = 1

    # return count

    for letter in phrase:
        count[letter] = count.get(letter, 0) + 1

    return count
