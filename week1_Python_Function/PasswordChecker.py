## Password Strength Checker

def is_strong(password):
    """This function check whether give password is strong or not"""
    if len(password) < 8:                                           # Check if password has at least 8 characters
        return False                                                # Return False if password is too short
    if not any(char.isdigit() for char in password):                # Check if password contains at least one digit
        return False                                                # Return False if no digit is found
    if not any(char.islower() for char in password):                # Check if password contains at least one lowercase letter
        return False                                                # Return False if no lowercase letter is found
    if not any(char.isupper() for char in password):                # Check if password contains at least one uppercase letter
        return False                                                # Return False if no uppercase letter is found
    if not any(char in '!@#$%^&*()_+' for char in password):        # Check if password contains at least one special character
        return False                                                # Return False if no special character is found
    return True                                                     # Return True if all conditions are met - password is strong

# Calling function with test cases
print(is_strong("WeakPass"))                                       # Test with weak password - should return False
print(is_strong("Strong2Pass$*"))                                  # Test with strong password - should return True
