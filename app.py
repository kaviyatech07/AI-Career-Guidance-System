from careers import careers
from courses import courses
from career_predictor import predict_career
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Career Guidance System")
st.write("Welcome to the AI Career Guidance System!")

# -----------------------------
# User Information
# -----------------------------
name = st.text_input("Enter Your Name")

st.subheader("📊 Rate Your Skills")

python_skill = st.slider("Python", 1, 10, 5)
ml_skill = st.slider("Machine Learning", 1, 10, 5)
math_skill = st.slider("Mathematics", 1, 10, 5)
communication_skill = st.slider("Communication", 1, 10, 5)
problem_skill = st.slider("Problem Solving", 1, 10, 5)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Career"):

    st.success(f"Welcome, {name}!")

    user_skills = {
        "Python": python_skill,
        "Machine Learning": ml_skill,
        "Mathematics": math_skill,
        "Communication": communication_skill,
        "Problem Solving": problem_skill
    }

    results = predict_career(user_skills)

    # Best Career
    best_career = results[0][0]
    best_score = results[0][1]

    st.subheader("🏆 Best Career")
    st.success(best_career)
    st.write(f"📊 Match Score: **{best_score}%**")

    st.subheader("📚 Recommended Courses")

career_to_interest = {
    "AI Engineer": "AI",
    "Data Scientist": "Data Science",
    "Software Developer": "Software Development"
}

if best_career in career_to_interest:
    interest = career_to_interest[best_career]

    if interest in courses:
        for course in courses[interest]:
            st.write(f"📘 {course}")

    # Top Career Matches
    st.subheader("🎯 Top 3 Career Matches")

    for career, score in results[:3]:
        st.write(f"✅ {career} — {score}% Match")
