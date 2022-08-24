def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    for val1 in nums:
        for val2 in nums:
            if val1 + val2 == goal:
                print((val1, val2))
                return ((val1, val2))
            return (())

sum_pairs([1, 2, 2, 10], 4)
sum_pairs([4, 2, 10, 5, 1], 6)
sum_pairs([5, 1, 4, 8, 3, 2], 7)
sum_pairs([11, 20, 4, 2, 1, 5], 100)
sum_pairs([50, 20, 4, 2, 1, 5], 100)

# what does "finish" mean in the 3rd example