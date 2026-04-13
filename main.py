# Student Result Checker System (With Subjects)

print("===== STUDENT RESULT CHECKER =====")

name = input("Enter student name: ")

subjects = [
    "Mathematics",
    "English Language",
    "Integrated Science",
    "Social Studies",
    "R.M.E",
    "Creative Arts",
    "Career Technology",
    "Ghanaian Language (Akuapim Twi)"
]

scores = []

# Collect scores
for subject in subjects:
    score = float(input(f"Enter score for {subject}: "))
    scores.append(score)

# Calculations
total = sum(scores)
average = total / len(subjects)

# Grade system
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Output
print("\n===== RESULT SUMMARY =====")
print("Student Name:", name)

print("\nSubjects and Scores:")
for i in range(len(subjects)):
    print(subjects[i], ":", scores[i])

print("\nTotal Score:", total)
print("Average Score:", average)
print("Grade:", grade)

if grade == "F":
    print("Status: FAIL")
else:
    print("Status: PASS")