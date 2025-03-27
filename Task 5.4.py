#write a python function to validate the Regular Expression for the following:
#a) Email Address
#b)Mobile numbers of Bangladesh
#c) Telephone numbers of use
#d) 16 character Alpha Numeric password composed of alphabets of upper case ,lower case special charecters,numbers 

import re

def validate_input(value, pattern):
    """Validates the given value against the provided regex pattern."""
    return bool(re.fullmatch(pattern, value))

# a) Email Address Validation
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return validate_input(email, email_pattern)

# b) Mobile Numbers of Bangladesh (Starts with +880 or 01 followed by 9 digits)
def is_valid_bd_mobile(number):
    bd_mobile_pattern = r"^(?:\+8801[3-9]\d{8}|01[3-9]\d{8})$"
    return validate_input(number, bd_mobile_pattern)

# c) US Telephone Numbers (Formats: (XXX) XXX-XXXX, XXX-XXX-XXXX, XXX.XXX.XXXX, XXX XXX XXXX)
def is_valid_us_phone(phone):
    us_phone_pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return validate_input(phone, us_phone_pattern)

# d) 16-character Alpha-Numeric Password with Upper, Lower, Special Character, and Number
def is_valid_password(password):
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"
    return validate_input(password, password_pattern)

# Testing the functions
print(is_valid_email("test@example.com"))  # True
print(is_valid_bd_mobile("+8801712345678"))  # True
print(is_valid_bd_mobile("01712345678"))  # True
print(is_valid_us_phone("(123) 456-7890"))  # True
print(is_valid_us_phone("123-456-7890"))  # True
print(is_valid_password("Abcd@1234Efgh5678"))  # True
print(is_valid_password("weakpassword"))  # False
