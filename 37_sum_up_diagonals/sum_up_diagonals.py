def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    loops = len(matrix)
    
    sum_tl_br = 0
    sum_tr_bl = 0

    # number of times to loop
    for x in range(loops):
        sum_tl_br += matrix[x][x]
        sum_tr_bl += matrix[x][loops-(x+1)]

    total = sum_tl_br + sum_tr_bl

    return total 