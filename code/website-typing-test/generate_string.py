import string
import random

def generate_random_string_with_specific_chars(length):
    # Characters that can be typed without the Shift key, only lowercase and specified punctuation
    chars = string.ascii_lowercase + ",./;'["

    # Initialize the string and count for spaces
    random_string = ''
    space_count = 0

    for _ in range(length):
        # Add a space after every 5 characters on average
        if space_count >= 5:
            random_string += ' '
            space_count = 0
        else:
            random_string += random.choice(chars)
            space_count += 1

    return random_string

# Generate a new string with the specified characters
random_text_specific = generate_random_string_with_specific_chars(1000)
print(random_text_specific)  
len(random_text_specific)  # Check the length of the generated string including spaces
