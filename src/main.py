from careers import careers
from courses import courses
from career_predictor import get_user_skills, predict_career
from roadmap import show_roadmap

print("=" * 50)
print("      AI CAREER GUIDANCE SYSTEM")
print("=" * 50)

# User Name
name = input("Enter your name: ").strip()
print("\nWelcome,", name)

# User Interest
interest = input("Enter your interest (AI/Data Science/Software Development): ").strip()

# Menu
print("\nWhat do you want to see?")
print("1. Career Recommendations")
print("2. Recommended Courses")
print("3. Both")

choice = input("Enter your choice (1/2/3): ")

print("\nYou selected:", interest)

# Check valid interest
if interest not in careers:
    print("\nInvalid interest! Please restart the program.")
else:

    # Show Careers
    if choice == "1":
        print("\n===== CAREER RECOMMENDATIONS =====")
        for career in careers[interest]:
            print("-", career)

    # Show Courses
    elif choice == "2":
        print("\n===== RECOMMENDED COURSES =====")
        for course in courses[interest]:
            print("-", course)

    # Show Both
    elif choice == "3":
        print("\n===== CAREER RECOMMENDATIONS =====")
        for career in careers[interest]:
            print("-", career)

        print("\n===== RECOMMENDED COURSES =====")
        for course in courses[interest]:
            print("-", course)

    # Invalid Menu Choice
    else:
        print("\nInvalid choice!")

print("\n" + "=" * 50)
print("Thank you for using AI Career Guidance System,", name + "!")
print("Best wishes for your future career! 🚀")
print("=" * 50)
