# Import the statistics module to calculate averages
import statistics

# Function to categorize students based on their average scores
def categorize_student(avg_score):
    if avg_score >= 90:
        return "Excellent"
    elif avg_score >= 70:
        return "Good"
    elif avg_score >= 50:
        return "Average"
    else:
        return "Below Average"

# Initialize an empty list to store student scores
student_scores = []

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Loop to input scores for each student
for i in range(num_students):
    student_name = input(f"Enter the name of student {i + 1}: ")
    student_score = float(input(f"Enter the score for {student_name}: "))
    student_scores.append((student_name, student_score))

# Calculate the average score for all students
all_scores = [score for name, score in student_scores]
average_score = statistics.mean(all_scores)

# Display the average score
print(f"\nThe average score for all students is: {average_score:.2f}\n")

# Categorize and display each student's performance
print("Student Performance Categories:")
for name, score in student_scores:
    category = categorize_student(score)
    print(f"{name}: {category}")
