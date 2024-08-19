
# Nyra: AI-Powered Document Assistant

Nyra is an AI-powered assistant capable of reading and understanding documents. It can answer questions based on the content of multiple documents, control various applications, and interact with Spotify for music playback. Nyra leverages advanced NLP models and provides an intuitive, conversational interface.

## Features

- **Document Understanding**: Nyra reads and processes all PDF documents in the `Docs` folder upon startup. It stores the content in memory and answers questions based on the combined text of all documents.
- **Natural Language Processing (NLP)**: Powered by a sophisticated language model (OllamaLLM), Nyra generates accurate and contextually relevant answers.
- **Application Control**: Nyra can open websites, launch applications like Calculator and Notepad, set timers, and even control system functions like shutdown and restart.
- **Spotify Integration**: Control your Spotify playback with commands like play, pause, next track, previous track, and more.
- **Extensible Intent System**: Easily add new commands and functionalities through an intent-based system.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Configuration](#configuration)
5. [Adding New Features](#adding-new-features)
6. [License](#license)

## Installation

### Prerequisites

- **Python 3.7+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer. It usually comes with Python, but you can install it separately if needed.

### Clone the Repository

```bash
git clone https://github.com/asoron/nyra-ai-assistant.git
cd nyra-ai-assistant
```

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Setup Spotify API Credentials

1. Create a Spotify Developer account and create a new app to get your `Client ID` and `Client Secret`.
2. Set up the environment variables for your Spotify credentials:

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-redirect-uri'
```

## Usage

## Using the LangChain Ollama Llama 3.1:8B Model

This project harnesses the power of the **LangChain Ollama Llama 3.1:8B** model to deliver advanced natural language processing capabilities. The model is pivotal in generating accurate, contextually aware responses for both document-based queries and general conversational interactions.

### **Model Overview**

- **Model Name**: Llama 3.1:8B
- **Architecture**: Derived from the Llama family, known for its balance between performance and accuracy.
- **Parameter Count**: 8 billion parameters, offering a robust model that excels in both computational efficiency and response quality.

### **Integration with LangChain**

The Llama 3.1:8B model is seamlessly integrated into this project using the **LangChain** framework, which simplifies the deployment of large language models (LLMs) across various applications. LangChain provides a streamlined interface that makes it straightforward to leverage the capabilities of Llama 3.1:8B for complex tasks such as document analysis and conversational AI.

### **Key Features**

- **Document-Based Q&A**: Nyra can answer questions by thoroughly analyzing and understanding the content across multiple documents. This feature is ideal for situations requiring in-depth, context-specific answers.
- **Conversational AI**: The model adeptly manages free-flowing conversations, providing responses that are both informative and relevant to the context of the discussion.

### **How It Works**

1. **Model Initialization**  
   The Llama 3.1:8B model is initialized at the program's start, using the `OllamaLLM` class from the `langchain_ollama` package. This setup is optimized for CUDA devices, ensuring efficient performance.

    ```python
    from langchain_ollama import OllamaLLM
    
    def initialize_model():
        return OllamaLLM(model="llama3", device="cuda")
    ```

2. **Generating Responses**  
   Nyra generates responses by processing user queries and document content through the model. The responses are crafted to be precise and contextually relevant.

    ```python
    def generate_response(model, template, question):
        prompt = template.format(question=question)
        try:
            answer = model(prompt).strip()
        except Exception as e:
            answer = "Sorry, something went wrong. Please try again."
        return answer
    ```

3. **Document-Based Question Answering**  
   The model excels at answering questions derived from document content. It processes the combined text from all loaded documents and generates answers based on the provided context.

    ```python
    def answer_question_from_text(question, context):
        prompt = f"Answer the following question based on the provided context:\\n\\nContext: {context}\\n\\nQuestion: {question}\\n\\nAnswer:"
        answer = model(prompt)
        return answer.strip()
    ```

### **Benefits**

- **High Precision**: The Llama 3.1:8B model delivers highly precise answers, making it suitable for addressing complex and nuanced queries.
- **Performance Optimization**: Despite its extensive parameter count, the model is optimized for GPU performance, ensuring rapid response times.
- **Versatility**: The model's architecture allows it to handle a wide range of queries, from straightforward questions to more intricate, document-based inquiries.

### **System Requirements**

To effectively utilize the Llama 3.1:8B model, ensure that your system is equipped with a compatible GPU capable of handling high computational loads. The model initialization relies on CUDA, making it ideal for high-performance computing environments.

### **Conclusion**

The integration of the LangChain Ollama Llama 3.1:8B model elevates Nyra’s capabilities, enabling it to deliver accurate, context-sensitive responses across various use cases. Whether answering questions based on extensive document content or managing dynamic conversations, this model provides a robust foundation for advanced natural language processing tasks.

### Starting the Assistant

To start Nyra, simply run the `start.py` script:

```bash
python start.py
```

Nyra will read all PDF documents in the `Docs` folder upon startup and be ready to answer questions based on their content.

### Example Commands

- **Document-Based Question**: "Nyra, what is the main purpose of these documents?"
- **Open Google**: "Nyra, open Google."
- **Play a Song on Spotify**: "Nyra, play 'Bohemian Rhapsody'."
- **Set a Timer**: "Nyra, set a timer for 10 minutes."
- **Tell a Joke**: "Nyra, tell me a joke."

## Project Structure

```
nyra-ai-assistant/
│
├── Docs/                     # Folder containing all PDF documents
├── utils/
│   ├── model.py              # Model initialization and response generation
│   ├── intents.py            # Intent recognition and action execution
│   ├── spotify.py            # Spotify control functions
│   ├── readDocument.py       # Document reading and Q&A functions
│   └── utils.py              # Utility functions (e.g., context management)
├── document_processor.py     # Main document reading and answering logic
├── start.py                  # Entry point for the assistant
├── main.py                   # Alternative main script (can be customized for different purposes)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Configuration

### Customizing Document Folder

If you want to use a different folder for your documents, modify the `docs_folder` variable in `document_processor.py`:

```python
docs_folder = "Docs"  # Default folder
```

### Adjusting the Confidence Threshold

In `intents.py`, you can adjust the confidence threshold for intent recognition:

```python
if confidence > 0.9:  # Adjust this threshold as needed
```

This ensures that only highly confident matches trigger actions, allowing for more accurate command recognition.

## Adding New Features

### Adding a New Intent

1. **Define the Action**: Implement the function that will be triggered by the new intent.
2. **Add to `INTENT_ACTIONS`**: Map the intent to the action in `intents.py`.

```python
def new_action():
    # Your code here
    print("Nyra: Executing new action...")

INTENT_ACTIONS = {
    "new_intent": new_action,
    # Other intents...
}
```

3. **Update the JSON Intent File**: Add the new intent and its corresponding utterances to `intents.json`.

```json
{
  "intent": "new_intent",
  "utterances": [
    "trigger new action",
    "execute new feature",
    "start new function"
  ]
}
```

4. **Retrain the Model**: Ensure the intent recognition model is updated to include the new intent.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
