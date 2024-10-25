import random

# List of bad motivational quotes
honest_quotes = {
    "Self_doubt": [
        "Why bother? You're not that special.",
        "Confidence? Not in this lifetime.",
        "Why try when it's easier to fail?",
    ],
    "Procrastination": [
        "You’ll probably do it tomorrow…or next year.",
        "Deadlines are just suggestions, right?",
        "Maybe if you ignore it, it’ll go away.",
    ],
    "Fitness": [
        "Abs are overrated. Have a donut.",
        "Lifting the remote counts as exercise.",
        "Why run when you can sit?",
    ]
}

# Function to return a random bad quote
def get_honesty(category):
    if category in honest_quotes:
        return random.choice(honest_quotes[category])
    else:
        return "Category not found. Please choose a valid category."

# Display available categories to the user
print("Available categories:", ', '.join(honest_quotes.keys()))

# Ask the user to select a category
user_category = input("Choose a category from the above: ").lower()

# Get a random quote from the chosen category
print(get_honesty(user_category))
