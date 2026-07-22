from careers import careers
from courses import courses
from career_predictor import predict_career
from roadmap import show_roadmap
from career_info import career_info
import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📋 Navigation")

st.sidebar.info(
    """
    **AI Career Guidance System**

    ✅ Career Prediction
    ✅ Skill Assessment
    ✅ Learning Roadmap
    ✅ Recommended Courses

    Developed by **Kaviya**
    """
)

# -----------------------------
# Main Title
# -----------------------------
st.title("🤖 AI Career Guidance System")

st.markdown("---")

st.info("💡 Rate your skills honestly to get the best career recommendation.")

st.write("Welcome to the AI Career Guidance System!")

# -----------------------------
# User Name
# -----------------------------
name = st.text_input("Enter Your Name")

# -----------------------------
# Skill Assessment
# -----------------------------
st.subheader("📊 Rate Your Skills")

python_skill = st.slider("Python", 1, 10, 5)
ml_skill = st.slider("Machine Learning", 1, 10, 5)
math_skill = st.slider("Mathematics", 1, 10, 5)
communication_skill = st.slider("Communication", 1, 10, 5)
problem_skill = st.slider("Problem Solving", 1, 10, 5)

# -----------------------------
# Predict Button
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

    # -----------------------------
    # Best Career
    # -----------------------------
    best_career = results[0][0]
    best_score = results[0][1]

    st.subheader("🏆 Your Best Career Match")
    st.success(f"🎯 {best_career}")

    st.write(f"📊 Match Score: **{best_score}%**")

    # -----------------------------
    # Top 3 Career Matches
    # -----------------------------
    st.subheader("🎯 Top 3 Career Matches")

    top3 = pd.DataFrame(
        results[:3],
        columns=["Career", "Match Score (%)"]
    )

    st.table(top3)

    # -----------------------------
    # Career Match Chart
    # -----------------------------
    st.subheader("📊 Career Match Chart")

    chart_data = pd.DataFrame(
        results,
        columns=["Career", "Match Score (%)"]
    )

    st.bar_chart(chart_data.set_index("Career"))

    # -----------------------------
    # Learning Roadmap
    # -----------------------------
    st.subheader("🗺️ Learning Roadmap")

    roadmap = show_roadmap(best_career)

    for i, step in enumerate(roadmap, start=1):
        st.write(f"{i}. {step}")

    # -----------------------------
    # Recommended Courses
    # -----------------------------
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
           
