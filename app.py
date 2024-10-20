import streamlit as st
from utils.document_loader import load_manual
from utils.chatbot import USCISChatbot
from streamlit_option_menu import option_menu

# Load the USCIS manual text
context = load_manual()

# Initialize the chatbot with the USCIS manual as context
chatbot = USCISChatbot(context)

# Streamlit UI setup
st.set_page_config(page_title="Chatbot UI", page_icon="🤖", layout="centered")

# Sidebar navigation
with st.sidebar:
    selected = option_menu("Chatbot Menu", ["Chat", "About"],
                           icons=["chat", "info-circle"],
                           menu_icon="cast", default_index=0)

if selected == "Chat":
    st.title("🤖 Chatbot")
    st.write("Ask me anything related to USCIS Policy Manual.")

# User input
user_query = st.text_input("Your Question:", "")

# Submit button
if st.button("Submit"):
    if user_query.strip():
        response = chatbot.answer_query(user_query)
        st.text_area("Chatbot Response:", response, height=200)
    else:
        st.warning("Please enter a valid question.")

elif selected == "About":
    st.title("About This Chatbot")
    st.write("""
        This chatbot is designed to assist you with various USCIS policy-related questions.
        It utilizes a language model to provide accurate and relevant answers.
    """)