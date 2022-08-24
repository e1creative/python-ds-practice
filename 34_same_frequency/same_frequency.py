def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    nums_set1 = set(str(num1))
    nums_set2 = set(str(num2))

    nums_list1 = list(str(num1))
    nums_list2 = list(str(num2))

    # check if num1 and num2 contain the same digits
    if not nums_set1 == nums_set2:
         # if the digists in each num are NOT the same return false
        return False
    else:
        # if the digists in each num ARE the same, 
        # loop through the nums in any set (since they contain the same num elements),
        # and get the count in botH LISTS
        for num in nums_set1:
            # compare. if the count is NOT the same in both LISTS return False
            if nums_list1.count(num) != nums_list2.count(num):
                return False

        # if no returns have been hit, then all counts are equal
        return True