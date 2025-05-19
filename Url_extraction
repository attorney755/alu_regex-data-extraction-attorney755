import re

def check_url_format(url):
    # This function checks if the given URL is in a valid format
    # Here I used a regex pattern to match common URL formats
    pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-z]{2,6}(/\S*)?$'

    # Here I used re.fullmatch to ensure the entire string matches the pattern
    return bool(re.fullmatch(pattern, url))

# List of URLs to validate
web_addresses = ["https://www.example.com", "http://subdomain.example.org/page", "ftp://invalid.com"]

# Iterate over each URL and check its validity
for address in web_addresses:
    print(f"{address}: {'Valid' if check_url_format(address) else 'Invalid'}")
