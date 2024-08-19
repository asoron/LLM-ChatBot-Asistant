import warnings
from langchain_ollama import OllamaLLM

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_core")

def initialize_model():
    return OllamaLLM(model="llama3", device="cuda")

def generate_response(model, template, question):
    prompt = template.format(question=question)
    try:
        answer = model(prompt).strip()
    except Exception as e:
        answer = "Sorry, something went wrong. Please try again."
    return answer
