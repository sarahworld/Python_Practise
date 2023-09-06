def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    every_other_elem = []

    for index, val in enumerate(lst):
        if(index % 2 == 0):
            every_other_elem.append(val);
    
    return every_other_elem;

print(remove_every_other([1, 2, 3, 4, 5]))


