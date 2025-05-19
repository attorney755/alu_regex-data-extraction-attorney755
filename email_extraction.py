import re

# Define a regex pattern to match email addresses
# Here I used a pattern that matches standard email formats
EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def check_email_format(email):
    # This function checks if the given email is in a valid format
    # Here I used the fullmatch method to ensure the entire string matches the pattern
    return bool(EMAIL_REGEX.fullmatch(email))

# List of email addresses to validate
email_addresses = [
    "user@example.com",
    "firstname.lastname@company.co.uk",
    "wrong@format",
    "test@com",
]

# Iterate over each email and check its validity
results = [f"{email}: {'Valid' if check_email_format(email) else 'Invalid'}" for email in email_addresses]
print('\n'.join(results))
