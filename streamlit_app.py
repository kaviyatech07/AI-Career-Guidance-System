import streamlit as st

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🤖"
)

st.title("🤖 AI Career Guidance System")

st.write("Welcome to my AI Career Guidance System!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome, {name}!")
