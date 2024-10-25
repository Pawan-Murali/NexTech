import random

# List of bad motivational quotes
bad_quotes = [
    "Give up now – tomorrow's not looking any better.",
    "Why try when you can fail?",
    "Dream small and avoid disappointment.",
    "If you can't do it perfectly, don’t bother at all.",
    "Good things come... to people who wait too long and miss out."
]

# Function to return a random bad quote
def get_bad_quote():
    return random.choice(bad_quotes)

# Example usage
print(get_bad_quote())
