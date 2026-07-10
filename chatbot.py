"""
Basic Chatbot
CodeAlpha Python Programming Internship

Author: Helina Leul

Description:
A console-based rule-based chatbot that interacts with
users using predefined responses.

Features:
- Greets the user
- Responds to predefined questions
- Handles unknown inputs gracefully
- Saves chat history to a text file
- Clean and modular design
"""
# ==========================
# Imports
# ==========================

from datetime import datetime

from responses import RESPONSES

# ==========================
# Welcome Message
# ==========================

def display_welcome():
    """
    Display the chatbot welcome message.
    """

    print("\n" + "=" * 50)
    print("        CODEALPHA BASIC CHATBOT")
    print("=" * 50)
    print("Hello! I'm your friendly chatbot.")
    print("Type 'bye' anytime to end the conversation.")
    print("=" * 50)

# ==========================
# Get Bot Response
# ==========================

def get_bot_response(user_message):
    """
    Return the chatbot's response based on the user's message.
    """

    user_message = user_message.lower().strip()

    if user_message in RESPONSES:
        return RESPONSES[user_message]

    return (
        "I'm sorry, I don't understand that yet. "
        "Please try another question."
    )

# ==========================
# Save Chat History
# ==========================

def save_chat_history(user_message, bot_response):
    """
    Save each conversation to chat_history.txt.
    """

    with open("chat_history.txt", "a") as file:

        file.write(f"\nDate: {datetime.now()}\n")
        file.write(f"You: {user_message}\n")
        file.write(f"Bot: {bot_response}\n")
        file.write("-" * 50 + "\n")

        # ==========================
# Chat Loop
# ==========================

def chat():
    """
    Start the chatbot conversation.
    """

    while True:

        user_message = input("\nYou: ").strip()

        bot_response = get_bot_response(user_message)

        print(f"Bot: {bot_response}")

        save_chat_history(
            user_message,
            bot_response
        )

        if user_message.lower() == "bye":
            break

        # ==========================
# Main Program
# ==========================

def main():
    """
    Main function that runs the chatbot.
    """

    display_welcome()

    chat()

    print("\nThank you for chatting with me!")
# ==========================
# Run Program
# ==========================

if __name__ == "__main__":
    main()
