
def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    
    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """
    try:
        # float to int lol
        return (True, int(float(num_string)))
    except (ValueError, TypeError):
        return (False, 0)
    

def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    
    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """
    try:
        if '.' not in str(num_string):
            return (True, 0, 1)
        
        # copy right of decimal
        frac_part = str(num_string).split('.')[1]
        if not frac_part.isdigit():
            return (False, 0, 0)
        
        # num is copy denom is 10^len copy
        numerator = int(frac_part)
        denominator = 10 ** len(frac_part)
        
        # result
        return (True, numerator, denominator)
    
    # error?
    except (ValueError, IndexError):
        return (False, 0, 0)

