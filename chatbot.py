def get_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


print("=== BASIC CHATBOT ===")
print("Type 'hello', 'how are you' or 'bye'\n")

while True:
    user_input = input("You: ")
    reply = get_reply(user_input)
    print("Bot:", reply)

    if user_input.lower().strip() == "bye":
        break