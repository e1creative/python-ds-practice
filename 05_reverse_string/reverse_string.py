def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    converted_to_list = list(phrase)

    converted_to_list.reverse()

    return "".join(converted_to_list)