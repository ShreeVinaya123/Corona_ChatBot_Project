import json
import random
import nltk
import numpy as np
import pickle
from nltk.stem import PorterStemmer
from tensorflow.keras.models import load_model

nltk.download('punkt')

# Initialize stemmer
stemmer = PorterStemmer()

# Load pre-trained model
model = load_model("chatbot_model.h5")

# Load data
with open("intents.json") as file:
    data = json.load(file)

# Load preprocessed words and classes
with open("words.pkl", "rb") as f:
    words = pickle.load(f)

with open("classes.pkl", "rb") as f:
    classes = pickle.load(f)

def tokenize_and_stem(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def predict_class(sentence):
    bow = bag_of_words(sentence, words)
    results = model.predict(np.array([bow]))[0]
    results_index = np.argmax(results)
    tag = classes[results_index]
    if results[results_index] > 0.7:
        return tag
    else:
        return "no_match"

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm sorry, I didn't understand that."

def bag_of_words(sentence, words):
    sentence_words = tokenize_and_stem(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def chat():
    print("Start talking with the bot! (type 'quit' to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            print("Stay safe! Goodbye!")
            break

        bow = bag_of_words(inp, words)
        results = model.predict(np.array([bow]))[0]
        results_index = np.argmax(results)
        tag = classes[results_index]

        if results[results_index] > 0.7:
            for intent in data["intents"]:
                if intent["tag"] == tag:
                    print("Bot:", random.choice(intent["responses"]))
        else:
            print("Bot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chat()



