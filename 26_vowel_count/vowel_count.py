def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel = 'aeiou'
    result = {};
    for val in phrase.lower():
        if val in vowel:
            if val in result.keys():
                result[val] += 1
            else:
                result[val] = 1;

    return result;

print(vowel_count('rithm school'));
print(vowel_count('HOW ARE YOU? i am great!') );

        