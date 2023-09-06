def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    tup = tuple(phrase);
    result = {};

    for elem in tup:
        result[elem] = tup.count(elem);
    
    return result

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))
