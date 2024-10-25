// Dictionary of "honest" quotes
const honestQuotes = {
    "insecurity": [
        "Why bother? You're not special.",
        "Confidence? Not in this lifetime.",
        "Why try when it's easier to fail?"
    ],
    "procrastination": [
        "There's always going to be a tomorrow. If not... then even better.",
        "Deadlines are just suggestions, right?",
        "Maybe if you ignore it, it’ll go away."
    ],
    "fitness": [
        "Abs are overrated. Have a donut.",
        "Lifting the remote counts as exercise.",
        "Why run when you can sit?"
    ],
    "academics": [
        "You'll fail even if you study hard. So binge that show!",
        "You can't make it in a single day.",
        "You don't have the talent to study",
        "Anyway, you are not going to pass."
    ],
    "athletics": [
        "Everyone knows you're going to lose.",
        "This match is going to be impossible for you.",
        "The other team looks so good.",
        "It seems like the other team had great practice."
    ],
    "marriage": [
        "You are clearly the problem.",
        "You can't be a good partner, it's due to your father.",
        "Why did you even get married in the first place?"
    ]
};

// Function to fetch a random quote for the selected category
function fetchQuote() {
    const category = document.getElementById('categoryDropdown').value;
    const quotes = honestQuotes[category];
    if (quotes) {
        const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
        document.getElementById('quoteOutput').textContent = `"${randomQuote}"`;
    } else {
        document.getElementById('quoteOutput').textContent = "Category not found.";
    }
}
