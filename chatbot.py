import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
pairs = [
    [
        r"hi|hello|hey",
        ["Hi there!", "Hello!", "Hey! How can i help you today?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple NLP chatbot you can call me Ai Chatbot!"]
    ],
    [
        r"how are you?",
        ["I'm doing well , thank you! How about you?"]
    ],
    [
        r"I am fine| I am good",
        ["Glad to hear that!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, Tell me what you need help with I'm here for you"]
    ],
    [
        r"who are you?",
        ["I'm just a python chatbot with a basic brain"]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm live in your computer!"]
    ],
    [
        r"how (.*) work",
        ["I use pattern matching and NLTK to talk withyou."]
    ],
    [
        r"quit",
        ["Bye! Take care"]
    ]
]
class CustomChat(Chat):
    def converse(self ,quit="quit"):
        print("Chatbot is ready to chat! type 'quit' to exit.\n")
        while True:
            user_input=input("you:")
            if user_input.lower()==quit:
                print("Chatbot: Bye! Take care.")
                break
            response=self.respond(user_input)
            print(f"chatbot: {response}")

if __name__=="__main__":
    Chatbot=CustomChat(pairs, reflections)
    Chatbot.converse()
