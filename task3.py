import re

def password_strength(password):
    """
    Evaluates the strength of a password based on length, use of upper and lower case letters,
    digits, and special characters.
    """
    # Setting up the criteria
    length = len(password) >= 8
    digit = re.search(r"\d", password) is not None
    uppercase = re.search(r"[A-Z]", password) is not None
    lowercase = re.search(r"[a-z]", password) is not None
    special_char = re.search(r"\W", password) is not None

    # Evaluating the password
    criteria = [length, digit, uppercase, lowercase, special_char]
    strength = sum(criteria)
    feedback = []

    if not length:
        feedback.append("- Password should be at least 8 characters long.")
    if not digit:
        feedback.append("- Password should include at least one digit.")
    if not uppercase:
        feedback.append("- Password should include at least one uppercase letter.")
    if not lowercase:
        feedback.append("- Password should include at least one lowercase letter.")
    if not special_char:
        feedback.append("- Password should include at least one special character.")
    
    # Providing feedback based on the number of criteria met
    if strength == 5:
        return "Strong password!"
    elif strength >= 3:
        feedback.insert(0, "Moderate password. Consider the following suggestions for improvement:")
    else:
        feedback.insert(0, "Weak password. Consider the following suggestions for improvement:")

    return '\n'.join(feedback)

# User input
password = input("Enter your password to check its strength: ")

# Checking the password strength
result = password_strength(password)
print(result)
