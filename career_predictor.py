# career_predictor.py

career_data = {
    "AI Engineer": {
        "Python": 9,
        "Machine Learning": 9,
        "Mathematics": 8,
        "Communication": 6,
        "Problem Solving": 9
    },

    "Data Scientist": {
        "Python": 8,
        "Machine Learning": 8,
        "Mathematics": 9,
        "Communication": 7,
        "Problem Solving": 8
    },

    "Software Developer": {
        "Python": 9,
        "Machine Learning": 4,
        "Mathematics": 6,
        "Communication": 7,
        "Problem Solving": 8
    },

    "Data Analyst": {
        "Python": 7,
        "Machine Learning": 6,
        "Mathematics": 8,
        "Communication": 8,
        "Problem Solving": 7
    }
}


def get_user_skills():
    print("\nRate your skills (1-10)\n")

    skills = {}

    skills["Python"] = int(input("Python: "))
    skills["Machine Learning"] = int(input("Machine Learning: "))
    skills["Mathematics"] = int(input("Mathematics: "))
    skills["Communication"] = int(input("Communication: "))
    skills["Problem Solving"] = int(input("Problem Solving: "))

    return skills


def predict_career(user_skills):

    scores = {}

    for career, required_skills in career_data.items():

        score = 0

        for skill in required_skills:
            difference = abs(user_skills[skill] - required_skills[skill])
            score += (10 - difference)

        percentage = (score / 50) * 100
        scores[career] = round(percentage, 2)

    return sorted(scores.items(), key=lambda x: x[1],
