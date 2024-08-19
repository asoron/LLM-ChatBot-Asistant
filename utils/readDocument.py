import fitz
import os
from utils.model import initialize_model

# Initialize the model
model = initialize_model()

# Global variable to store the combined text from all documents
all_documents_text = ""

def read_all_pdfs_in_folder(folder_path):
    global all_documents_text
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            print(f"Nyra: Reading {file_name}...")
            all_documents_text += read_pdf(file_path) + "\n\n"

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def answer_question_from_text(question, context):
    prompt = f"Answer the following question based on the provided context:\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    answer = model(prompt)
    return answer.strip()

def load_documents():
    docs_folder = "Docs"  
    print("Nyra: Reading all documents in the Docs folder...")
    read_all_pdfs_in_folder(docs_folder)

def answer_from_documents():
    if not all_documents_text:
        print("Nyra: Documents have not been loaded.")
        return
    
    question = input("Nyra: What question would you like to ask based on the documents? ")
    answer = answer_question_from_text(question, all_documents_text)
    print(f"Nyra: {answer}")
