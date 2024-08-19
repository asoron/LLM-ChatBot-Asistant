import json 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import pickle

with open('json/intents.json', 'r') as f:
    data = json.load(f)

utterances = []
labels = []

for intent in data['intents']:
    for utterance in intent['utterances']:
        utterances.append(utterance)
        labels.append(intent['intent'])

X_train, X_test, y_train, y_test = train_test_split(utterances, labels, test_size=0.2, random_state=42)

model = make_pipeline(CountVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model accuracy:", model.score(X_test, y_test))
