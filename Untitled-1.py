class Chatbot:
    def __init__(self):
        self.intents = {
            "creator": {
                "questions": [
                    "what is the name of your developers",
                    "what is the name of your creators",
                    "who created you",
                    "your developers",
                    "your creators",
                    "who are your developers",
                    "who created you",
                    "creators"
                ],
                "responses": [
                    "College students"
                ]
            },
            "name": {
                "questions": [
                    "name",
                    "your name",
                    "do you have a name",
                    "what is your name",
                    "what should I call you",
                    "who are you"
                ],
                "responses": [
                    "You can call me Mind Reader.",
                    "I'm Mind Reader",
                    "I am a Chatbot.",
                    "I am your helper"
                ]
            },
            "staffordshire university": {
                "questions": [
                    "Where is Staffordshire University located",
                    "Tell me about Staffordshire University",
                    "What programs does Staffordshire University offer",
                    "Contact details for Staffordshire University"
                ],
                "responses": [
                    "Staffordshire University is located in Staffordshire, England, offering various undergraduate and postgraduate programs. For more details, visit their official website or contact them directly at [phone number]."
                ]
            },
            "staffordshire university admission process": {
                "questions": [
                    "How do I apply to Staffordshire University?",
                    "What is the admission process at Staffordshire University?",
                    "Admission requirements for Staffordshire University",
                    "How to get into Staffordshire University?"
                ],
                "responses": [
                    "To apply to Staffordshire University, you can submit your application via their website. Be sure to check the specific requirements for the course you are interested in, as well as the application deadlines. For more detailed information, visit the admissions section of their official website."
                ]
            }
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for intent, data in self.intents.items():
            for question in data["questions"]:
                if question in user_input:
                    return data["responses"][0]  # Return the first response for simplicity
        return "Sorry, I didn't understand that."

def main():
    bot = Chatbot()
    print("Welcome to the Staffordshire University Helper Bot! Ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
