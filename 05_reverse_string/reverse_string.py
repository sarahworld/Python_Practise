def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    result = []
    for elem in phrase:
        result.insert(0, elem);
    return ''.join(result)

print(reverse_string('awesome'));