import webbrowser
from utils.spotify import *
import warnings
import datetime
import pickle
import random
import os
import time

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_core")

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def open_website(url):
    print("Nyra: Opening the website...")
    webbrowser.open(url)

def clear_context():
    global context
    context = ""
    print("Nyra: I have cleared the conversation context.")

def open_calculator():
    print("Nyra: Opening the calculator...")
    os.system('calc')

def open_notepad():
    print("Nyra: Opening Notepad...")
    os.system('notepad')

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Nyra: The current time is {current_time}.")

def search_google():
    query = input("Nyra: What would you like to search for on Google? ")
    search_url = f"https://www.google.com/search?q={query}"
    open_website(search_url)
    
def set_timer():
    minutes = input("Nyra: How would you like to set minute? ")
    print(f"Nyra: Setting a timer for {minutes} minutes...")
    time.sleep(minutes * 60)
    print("Nyra: Time's up!")
    
def shutdown_computer():
    print("Nyra: Shutting down the computer...")
    os.system('shutdown /s /t 1')

def restart_computer():
    print("Nyra: Restarting the computer...")
    os.system('shutdown /r /t 1')

INTENT_ACTIONS = {
    "open_google": lambda: open_website("https://www.google.com"),
    "open_youtube": lambda: open_website("https://www.youtube.com"),
    "clear_context": clear_context,
    "tell_time": tell_time,
    "open_github": lambda: open_website("https://www.github.com"),
    "search_google": search_google,
    "set_timer": set_timer,
    "open_calculator": open_calculator,
    "open_notepad": open_notepad,
    "shutdown_computer": shutdown_computer,
    "restart_computer": restart_computer,
    "play_song": play_song, 
    "pause_music": pause_music,
    "resume_music": resume_music,
    "next_track": next_track,
    "previous_track": previous_track,
    "play_playlist": play_playlist 
}


def recognize_intent(question):
    intent = model.predict([question.lower().strip()])[0]
    return INTENT_ACTIONS.get(intent, None)
