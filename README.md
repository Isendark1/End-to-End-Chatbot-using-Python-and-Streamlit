## Project Overview

This project demonstrates the development of an end-to-end chatbot using Python. The chatbot is trained on a dataset of intents and utilizes a machine learning model to classify user input into various categories, providing dynamic and contextually appropriate responses. Key components of the project include:

  - **Data Preprocessing and Vectorization**: The input text is processed and transformed into numerical features using `TfidfVectorizer`.
  - **Intent Classification Model**: A `Logistic Regression` model is used to predict user intent based on their input.  
  - **Chatbot Functionality**: The chatbot predicts the intent of the user's message and provides a relevant response from a set of predefined options.
  - **Interactive User Interface with Streamlit**: The chatbot is deployed using Streamlit, providing a user-friendly web interface for interaction.

This project serves as an example of integrating machine learning with natural language processing (NLP) to build an intelligent chatbot system, and is suitable for anyone interested in developing simple conversational agents.


## Library Dependencies

This project relies on specific versions of key libraries to ensure compatibility and functionality. Below are the versions used in this project:

- **NLTK**: 3.9.1  
- **Pandas**: 2.1.3  
- **Scikit-learn**: 1.2.2  
- **Streamlit**: 1.40.2  

Make sure to install these versions to reproduce the environment accurately. You can install the required libraries using:

```bash
pip install nltk==3.9.1 pandas==2.1.3 scikit-learn==1.2.2 streamlit==1.40.2
```
1. **`chatbot.py`**  
   This script contains the core implementation of the chatbot, including the logic, natural language processing (NLP) components, and response generation. It serves as the backbone of the chatbot application.

2. **`main.py`**  
   This script is responsible for deploying the chatbot as a web application using **Streamlit**. It provides an interactive interface for users to chat with the chatbot directly in their browser. The Streamlit interface ensures an easy-to-use and visually appealing experience.

## Running the Application

To deploy the chatbot locally, use the following command in your terminal:

```bash
streamlit run main.py
```

## Chatbot Interactions

Below are some sample interactions with the chatbot to showcase its capabilities:

### Greeting Interaction
![Greeting Interaction](Chatbot%20Interactions/1.png)

### Weather Query
![Weather Query](Chatbot%20Interactions/2.png)

### Joke Request
![Joke Request](Chatbot%20Interactions/3.png)

### Fun Fact Request
![Fun Fact Request](Chatbot%20Interactions/4.png)



