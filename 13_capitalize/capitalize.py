def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    out = "";
    for word in phrase.split():
        out += word[0].upper() + word[1:] + " ";

    return out

print(capitalize('only first word'))
