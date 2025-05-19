import re

def check_phone_format(phone):
    # This function checks if the given phone number is in a valid format
    # Here I used a regex pattern to match common phone number formats
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'

    # Here I used re.fullmatch to ensure the entire string matches the pattern
    return bool(re.fullmatch(pattern, phone))

# List of phone numbers to validate
phone_numbers = ["(123) 456-7890", "123-456-7890", "123.456.7890", "000-000-"]

def get_phone_status(phone):
    # This function returns a tuple with the phone number and its validation status
    return (phone, "Valid" if check_phone_format(phone) else "Invalid")

# Iterate over each phone number and check its validity
results = list(map(get_phone_status, phone_numbers))

print("Phone Number Validation Summary:")
for phone, status in results:
    print(f"{phone}: {status}")
