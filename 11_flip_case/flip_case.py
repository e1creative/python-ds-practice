def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = []
    for letter in phrase:
        # if letters are the same, run our swapping function
        if to_swap.lower() == letter.lower():
            # if letter is lowercase, then uppercase it, else letter is uppercase so lowercase it
            letter = letter.upper() if letter.islower() else letter.lower()
        
        new_phrase.append(letter)
    
    return ("".join(new_phrase))

