import random

# List of bad motivational quotes
honest_quotes = {
    "self_doubt": [
        "Why bother? You're not that special.",
        "Confidence? Not in this lifetime.",
        "Why try when it's easier to fail?",
    ],
    "procrastination": [
        "You’ll probably do it tomorrow…or next year.",
        "Deadlines are just suggestions, right?",
        "Maybe if you ignore it, it’ll go away.",
    ],
    "fitness": [
        "Abs are overrated. Have a donut.",
        "Lifting the remote counts as exercise.",
        "Why run when you can sit?",
    ]
}

# Display available categories to the user
print("Available categories:", ', '.join(honest_quotes.keys()))
# Ask the user to select a category
category = input("Choose a category from the above: ").lower()

# Function to return a random bad quote
def get_honesty(category):
    if category in honest_quotes:
        return random.choice(honest_quotes[category])
    else:
        print("Category not found. Please choose a valid category.")
        while True:
            category = input("Choose a category from the above: ").strip().lower()
            quote = get_honesty(category)
            if quote:
                print(quote)
                break  # Exit loop after displaying a quote
            else:
                print("Category not found. Please choose a valid category.")





# Get a random quote from the chosen category
print(get_honesty(category))
