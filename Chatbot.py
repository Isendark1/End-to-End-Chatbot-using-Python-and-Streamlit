import os
import ssl
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st


# Setup for nltk downloads
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there!", "Hello!", "Hey! How can I help you today?", "I'm doing well, thank you! How about you?"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye!", "See you soon!", "Take care!", "Goodbye, have a nice day!"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome!", "No problem at all!", "Glad I could help!", "You're welcome, anytime!"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me?", "What should I do?"],
        "responses": ["Of course! What do you need help with?", "Sure, what can I assist you with?", "I'm here to help!"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you?", "What is your age?", "Can you tell me your age?"],
        "responses": ["I don't have an age. I'm just a chatbot!", "I exist in the digital realm, age doesn't apply here!"]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like?", "How's the weather today?", "Can you tell me the weather?"],
        "responses": ["I'm sorry, I can't provide real-time weather information.", "You can check a weather app for real-time data."]
    },
    {
        "tag": "budgeting",
        "patterns": ["How do I make a budget?", "Can you help me with budgeting?", "What's a good way to budget?"],
        "responses": [
            "To make a budget, start by tracking your income and expenses.",
            "A simple budgeting method is the 50/30/20 rule: 50% for essentials, 30% for wants, and 20% for savings and debt repayment."
        ]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score?", "How can I check my credit score?", "How do I improve my credit score?"],
        "responses": [
            "A credit score represents your creditworthiness. The higher your score, the better.",
            "You can check your credit score on websites like Credit Karma.",
            "To improve your credit score, try to make all payments on time and keep your credit utilization low."
        ]
    },
    {
        "tag": "jokes",
        "patterns": ["Tell me a joke", "Can you tell me a joke?", "Make me laugh"],
        "responses": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why don’t skeletons fight each other? They don’t have the guts!"
        ]
    },
    {
        "tag": "general_info",
        "patterns": ["Tell me something interesting", "I want to know something new", "Give me a fun fact"],
        "responses": [
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
            "A fun fact: Octopuses have three hearts!"
        ]
    }
]

# Create the vectorizer
vectorizer = TfidfVectorizer()

# Prepare data for training
tags = []
patterns = []

# Loop through intents to populate tags and patterns
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Vectorize patterns and extract tags
x = vectorizer.fit_transform(patterns)  # Features
y = tags  # Labels (intents)

clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response