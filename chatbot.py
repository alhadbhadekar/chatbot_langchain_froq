from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from a .env file
load_dotenv()

# streamlit page setup
st.set_page_config(
    page_title="Groq + LangChain Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# st.title("💬 Groq + LangChain Chatbot")
st.markdown(
    """
    <h1 style='text-align: center;'>💬 Groq + LangChain Chatbot</h1>
    """,
    unsafe_allow_html=True
)

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# llm initiate
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.6,
)

# Add custom CSS to move chat box up
st.markdown(
    """
    <style>
    /* Adds bottom padding to the main chat container */
    .stChatInput {
        margin-bottom: 80px !important; /* Adjust spacing above footer */
    }
    </style>
    """,
    unsafe_allow_html=True
)

user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant."}, *st.session_state.chat_history]
    )

    assistant_message = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

    with st.chat_message("assistant"):
        st.markdown(assistant_message)

footer = """
    <div style="
        position: fixed;
        bottom: 0;
        right: 0;
        width: 100%;
        text-align: right;
        padding: 10px 20px;
        color: grey;
        font-size: 14px;
        font-style: italic;
        background-color: rgba(255,255,255,0);
        z-index: 9999;
    ">
        <hr style="border: none; border-top: 1px solid #ccc; margin-bottom: 6px;">
        Developed Just For Fun
        <br>
        Author: Alhad Bhadekar
        <br>
        <a href="https://www.linkedin.com/in/alhadb/" target="_blank"
           style="color: grey; text-decoration: none; font-style: italic;">
           LinkedIn
        </a>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)