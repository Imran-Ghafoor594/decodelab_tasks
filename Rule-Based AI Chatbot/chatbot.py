from pyfiglet import Figlet

f = Figlet(font="slant")
print(f.renderText("Bot Activated"))

knowledge_base = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I am doing great.",
    "your name": "I am a Rule-Based AI Chatbot.",
    "help": "I can answer simple predefined questions.",
    "thanks": "You're welcome!"
}

print("Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    reply = knowledge_base.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)