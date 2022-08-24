def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    to_list = phrase.split(" ")

    to_list[0] = to_list[0].title()

    return (" ".join(to_list))