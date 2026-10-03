
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
    
# Test characteristic
print(characteristic("123.456"))    # (True, 123)
print(characteristic("-45.5"))      # (True, -45)
print(characteristic("0.999"))      # (True, 0)
print(characteristic("invalid"))    # (False, 0)

# Test mantissa
print(mantissa("123.456"))          # (True, 57, 125) - 456/1000 reduced
print(mantissa("0.5"))              # (True, 1, 2)
print(mantissa("0.25"))             # (True, 1, 4)
print(mantissa("1.0"))              # (False, 0, 0) - empty fractional part
print(mantissa("42"))               # (True, 0, 1) - no decimal point