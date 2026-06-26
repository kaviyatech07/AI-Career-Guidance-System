from careers import careers
from courses import courses
print("===================================")
print(" AI CAREER GUIDANCE SYSTEM ")
print("===================================")

name = input("Enter your name: ")

print("\nWelcome,", name)
interest = input("Enter your interest (AI/Data Science/Software Development): ")
print("\nSelect your strongest skill:")
print("1. Python")
print("2. SQL")
print("3. Problem Solving")

skill = input("Enter your choice (1/2/3): ")
print("\nInterest Selected:", interest)
print("Skill Selected:", skill)
print("\nGenerating Career Recommendations...")
print("Based on your interest in", interest)
print("Hello", name + ", here are some career options for you:")
if skill == "1":
    print("\n===== CAREER RECOMMENDATIONS =====")
   
    for career in careers["AI"]:
        print("-", career)

elif skill == "2":
    print("\n===== CAREER RECOMMENDATIONS =====")

    for career in careers["Data Science"]:
    print("-", career)
    
elif skill == "3":
    print("\n===== CAREER RECOMMENDATIONS =====")

   for career in careers["Software Development"]:
        print("-", career)

else:
    print("\nInvalid choice.")

