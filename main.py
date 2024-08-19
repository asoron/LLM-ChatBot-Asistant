from utils.model import initialize_model, generate_response
from utils.intents import recognize_intent, INTENT_ACTIONS
from utils.utils import update_context, Template

def handle_conversation():
    global context
    model = initialize_model()
    context = ""
    print("Welcome! My name is Nyra. I'm here to help you with your questions.")
    
    while True:
        question = input("Ask me a question: ").strip()
        
        if not question:
            print("Nyra: Please enter a question.")
            continue
        
        if question.lower() == "exit":
            print("Nyra: Goodbye! Feel free to come back anytime.")
            break
        
        action = recognize_intent(question)
        if action:
            action()
        else:
            answer = generate_response(model, Template, context, question)
            print("Nyra: " + answer)
            context = update_context(context, question, answer)

if __name__ == "__main__":
    handle_conversation()