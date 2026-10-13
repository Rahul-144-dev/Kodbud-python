RESPONSES = {
    # Greetings
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What's on your mind?",
    "hey": "Hey! Ask me anything.",
    "good morning": "Good morning! Ready to learn something?",
    "good evening": "Good evening! How can I assist?",
    # About the bot
    "who are you": "I'm a simple rule-based chatbot. No AI inside (yet).",
    "what is your name": "You can call me Python Chatbot.",
    "what can you do": "I can greet you, answer a few FAQs, and say goodbye. Type 'help' to see topics.",
    # normal questions
    "what is python": "Python is a popular, beginner-friendly programming language.",
    "what is machine learning": "ML is a field where computers learn patterns from data instead of being explicitly programmed.",
    "what is numpy": "NumPy is a Python library for fast numerical computing on arrays.",
    "what is pandas": "Pandas is a Python library for working with tabular data (like Excel, but in code).",
    # Small talk
    "how are you": "I'm just code, so I'm always fine. How about you?",
    "thanks": "You're welcome!",
    "thank you": "Anytime!",
    "ok": "Cool. Anything else?",
    "okay": "Cool. Anything else?",
}

EXIT_WORDS = {"bye", "exit", "quit", "goodbye", "end"}


def normalize(text):
    return text.lower().strip()


def get_reply(user_input):
    if user_input in RESPONSES:
        return RESPONSES[user_input]

    for key, reply in RESPONSES.items():
        if key in user_input:
            return reply

    return "Sorry, I didn't understand that. Type 'help' for topics."


def show_help():
    print("\n--- Topics I can talk about ---")
    topics = [
        "hello / hi / hey",
        "who are you",
        "what can you do",
        "what is python",
        "what is machine learning",
        "what is numpy",
        "what is pandas",
        "how are you",
        "bye / exit / quit",
    ]
    for t in topics:
        print(f"  - {t}")
    print()


def main():
    print("=== Python Chatbot ===")
    print("Type 'help' to see what I can talk about. Type 'bye' to exit.\n")

    while True:
        raw = input("You: ")
        user_input = normalize(raw)

        if not user_input:
            print("Python Chatbot: Say something!\n")
            continue

        if user_input in EXIT_WORDS:
            print("Python Chatbot: Goodbye! 👋")
            break

        if user_input == "help":
            show_help()
            continue

        reply = get_reply(user_input)
        print(f"Python Chatbot: {reply}\n")


if __name__ == "__main__":
    main()
