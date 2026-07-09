# roadmap.py

roadmaps = {

    "AI Engineer": [
        "Learn Python",
        "Learn Data Structures & Algorithms",
        "Master Machine Learning",
        "Learn Deep Learning",
        "Build 5 AI Projects",
        "Learn Git & GitHub",
        "Complete an AI Internship",
        "Prepare for Placements"
    ],

    "Data Scientist": [
        "Learn Python",
        "Master Statistics",
        "Learn SQL",
        "Learn Machine Learning",
        "Practice Data Visualization",
        "Build Data Science Projects",
        "Complete Internship",
        "Placement Preparation"
    ],

    "Software Developer": [
        "Learn Python/Java",
        "Learn Data Structures",
        "Practice Problem Solving",
        "Learn Web Development",
        "Build Full Stack Projects",
        "Learn Git & GitHub",
        "Complete Internship",
        "Placement Preparation"
    ],

    "Data Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Python",
        "Learn Power BI",
        "Learn Tableau",
        "Practice Data Analysis",
        "Build Portfolio",
        "Placement Preparation"
    ]
}


def show_roadmap(career):

    print("\n" + "=" * 50)
    print("        LEARNING ROADMAP")
    print("=" * 50)

    if career in roadmaps:
        for step_no, step in enumerate(roadmaps[career], start=1):
            print(f"{step_no}. {step}")
    else:
        print("Roadmap not available.")
