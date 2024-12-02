import streamlit as st
from Chatbot import chatbot

def main():
    st.title("End-to-End Chatbot")
    st.write("Type your message below to start chatting with the chatbot.")

    user_input = st.text_input("You:")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100)
        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me!")
            st.stop()

if __name__ == '__main__':
    main()