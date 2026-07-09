import streamlit as st

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Guidance System")

st.write("Welcome to the AI Career Guidance System")

name = st.text_input("Enter your Name")

interest = st.selectbox(
    "Select Your Interest",
    [
        "AI",
        "Data Science",
        "Software Development"
    ]
)

if st.button("Show Recommendation"):
    st.success(f"Welcome {name}")

    st.write("Interest:", interest)
