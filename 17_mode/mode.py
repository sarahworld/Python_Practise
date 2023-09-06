def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    max_count = 0;
    max = nums[0]

    for val in nums:
        if max_count < nums.count(val):
            max_count = nums.count(val)
            max = val
    
    return max
        
print(mode([1, 2, 1]))