from django.http import JsonResponse
from django.shortcuts import render
import json
import random
import nltk
from sklearn.ensemble import RandomForestClassifier
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Load the trained model and vectorizer
with open("../model/model/chatbot_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("../model/model/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Load intents dataset
with open("../model/Dataset/intents1.json", "r") as f:
    intents = json.load(f)

# Initialize the lemmatizer and stopwords

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


# Preprocess the input text
def preprocess_input(input_text):
    tokens = nltk.word_tokenize(input_text.lower())
    filtered_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words and token.isalpha()
    ]
    return " ".join(filtered_tokens)


# Correct spelling using TextBlob
def correct_spelling(user_input):
    return str(TextBlob(user_input).correct())


# Get response based on the predicted intent
def get_response_for_intent(intent):
    for i in intents["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])


# View for chatbot page
def index(request):
    return render(request, "chatbot/index.html")


# View to handle chatbot response
def get_bot_response(request):
    if request.method == "POST":
        user_input = json.loads(request.body).get("message")
        corrected_input = correct_spelling(user_input)
        processed_input = preprocess_input(corrected_input)
        input_vector = vectorizer.transform([processed_input]).toarray()
        predicted_intent = model.predict(input_vector)[0]
        response = get_response_for_intent(predicted_intent)
        return JsonResponse({"response": response})


def about(request):
    return render(request, "chatbot/about.html")
