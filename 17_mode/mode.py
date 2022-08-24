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
    number_count = {}

    for num in nums:
        number_count[num] = nums.count(num)
    
    # initialize our most common number to 0
    most_common_number = 0
    
    for (num, count) in number_count.items():
        if count > number_count.get(most_common_number, 0):
            most_common_number = num
        
    return most_common_number
    # for (k,v) in number_count.items:
    #     print(k,v)