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
