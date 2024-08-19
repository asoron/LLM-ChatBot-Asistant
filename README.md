
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
