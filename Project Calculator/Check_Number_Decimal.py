def is_last_number_decimal(current):
    for char in current[::-1]: #Moving from the end to the beginning.
        if char == '.':
            return True
        if char in ['+', '-', '*']:
            return False
    return False