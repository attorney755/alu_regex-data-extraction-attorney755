import re

def check_usd_format(amount):
    # This function checks if the given amount is in a valid US dollar format
    # Here I used a regex pattern to match common US dollar formats
    pattern = r'^\$\d{1,3}(?:,\d{3})*(?:\.\d{2,})?$|^\$\d+(?:\.\d{2})?$'

    # Here I used re.fullmatch to ensure the entire string matches the pattern
    return bool(re.fullmatch(pattern, amount))

# List of currency amounts to validate
currency_amounts = [
    "$19.99",
    "$1,234.56",
    "$100",
    "$12,345",
    "$12,345.67",
    "$123456.78",
    "19.99",
    "$1,234.567",
    "$1,23.45"
]

# Iterate over each amount and check its validity
for amount in currency_amounts:
    # Here I used an f-string to print the result
    print(f"{amount}: {'Valid' if check_usd_format(amount) else 'Invalid'}")
