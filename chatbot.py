import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am good, thanks for asking. How about you?']),
    (r'(.*) your name?', ["I'm just a humble chatbot.", "I'm a chatbot, so I don't really have a name."]),
    (r'(.*) help (.*)', ['I can assist you with a variety of topics. Just ask me anything!']),
    (r'(.*) (good|well|fine)', ['That\'s great!', 'Awesome!', 'Good to hear!']),
    (r'(.*) (bad|not good)', ['Oh, I\'m sorry to hear that. Is there anything I can do to help?']),
    (r'quit', ['Bye! Take care.', 'Goodbye!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def chat():
    print("Hi! I'm a simple chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat()
