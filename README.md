
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
