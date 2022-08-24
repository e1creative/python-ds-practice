def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    i = 0
    i_max = len(nums)

    count = 0

    while i <= (i_max - 2):

        inner_i = 0
        for num in nums:
            if nums[i] < nums[i + 1]:
                count += 1
            inner_i += 1
        
        i += 1

    return count