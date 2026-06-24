from careers import careers
print("===================================")
print(" AI CAREER GUIDANCE SYSTEM ")
print("===================================")

name = input("Enter your name: ")

print("\nWelcome,", name)

print("\nSelect your strongest skill:")
print("1. Python")
print("2. SQL")
print("3. Problem Solving")

skill = input("Enter your choice (1/2/3): ")

if skill == "1":
    print("\nRecommended Careers:")
    print("- AI Engineer")
    print("- Machine Learning Engineer")
    print("- Python Developer")

elif skill == "2":
    print("\nRecommended Careers:")
    print("- Data Analyst")
    print("- Database Developer")
    print("- Business Intelligence Analyst")

elif skill == "3":
    print("\nRecommended Careers:")
    print("- Software Developer")
    print("- System Analyst")
    print("- Product Engineer")

else:
    print("\nInvalid choice.")
if skill == "1":
    ...
elif skill == "2":
    ...
