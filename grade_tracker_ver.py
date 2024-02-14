import tkinter as tk
from tkinter import ttk

def calculate_final_grade(grades, weights):
    # Calculate the sum of weighted grades
    weighted_sum = sum(grades[i] * weights[i] for i in range(len(grades)))

    # Calculate the total weight
    total_weight = sum(weights)

    # Calculate the final grade by dividing the weighted sum by the total weight
    final_grade = weighted_sum / total_weight

    return final_grade

def calculate_grade():
    # Define the weights for each category
    assignments_weight = float(assignments_weight_entry.get()) / 100
    quizzes_weight = float(quizzes_weight_entry.get()) / 100
    mid_term_weight = float(mid_term_weight_entry.get()) / 100
    final_weight = 1 - (assignments_weight + quizzes_weight + mid_term_weight)
    weights = [assignments_weight, quizzes_weight, mid_term_weight, final_weight]

    # Get the grades for each category
    assignments_grades = [float(entry.get().split('/')[0]) / float(entry.get().split('/')[1]) if entry.get() else 1 for entry in assignment_entries]
    quizzes_grades = [float(entry.get().split('/')[0]) / float(entry.get().split('/')[1]) if entry.get() else 1 for entry in quiz_entries]

    # Get the grades for mid-term and final exams
    mid_term_grade = float(mid_term_grade_entry.get().split('/')[0]) / float(mid_term_grade_entry.get().split('/')[1]) if mid_term_grade_entry.get() else 1
    final_grade = float(final_grade_entry.get().split('/')[0]) / float(final_grade_entry.get().split('/')[1]) if final_grade_entry.get() else 1

    # Calculate the total grades for each category
    total_grades = [sum(assignments_grades), sum(quizzes_grades), mid_term_grade, final_grade]

    # Calculate the final grade using the calculate_final_grade function
    final_grade = calculate_final_grade(total_grades, weights)

    # Convert final grade to percentage
    final_grade_percent = final_grade * 100

    # Update the result labels
    weighted_average_label.config(text=f"Weighted Average: {final_grade_percent:.2f}%")
    final_grade_label.config(text=f"Final Grade: {final_grade_percent:.2f}%")


def add_assignment_field():
    index = len(assignment_entries) + 6
    new_label = ttk.Label(root, text=f"Assignment {index - 5}:")
    new_label.grid(row=index, column=2, padx=5, pady=5)
    entry = ttk.Entry(root)
    entry.grid(row=index, column=3, padx=5, pady=5)
    assignment_entries.append(entry)

def add_quiz_field():
    index = len(quiz_entries) + 6
    new_label = ttk.Label(root, text=f"Quiz {index - 5}:")
    new_label.grid(row=index, column=0, padx=5, pady=5)
    entry = ttk.Entry(root)
    entry.grid(row=index, column=1, padx=5, pady=5)
    quiz_entries.append(entry)


# Create a Tkinter window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("600x400")

# Create and place labels and entries for weights
ttk.Label(root, text="Enter the weights for each category (in percentage):").grid(row=0, column=0, columnspan=2, pady=5)

ttk.Label(root, text="Assignments:").grid(row=1, column=0, padx=5)
assignments_weight_entry = ttk.Entry(root)
assignments_weight_entry.grid(row=1, column=1, padx=5)

ttk.Label(root, text="Quizzes:").grid(row=2, column=0, padx=5)
quizzes_weight_entry = ttk.Entry(root)
quizzes_weight_entry.grid(row=2, column=1, padx=5)

ttk.Label(root, text="Mid-Term:").grid(row=3, column=0, padx=5)
mid_term_weight_entry = ttk.Entry(root)
mid_term_weight_entry.grid(row=3, column=1, padx=5)

# Create and place labels and entries for grades
ttk.Label(root, text="Enter the grades for each category (e.g., '9/10'):").grid(row=4, column=0, columnspan=2, pady=5)

assignment_entries = []
ttk.Label(root, text="Assignment 1:").grid(row=5, column=2, padx=5)
entry = ttk.Entry(root)
entry.grid(row=5, column=3, padx=5)
assignment_entries.append(entry)

quiz_entries = []
ttk.Label(root, text="Quiz 1:").grid(row=5, column=0, padx=5)
entry = ttk.Entry(root)
entry.grid(row=5, column=1, padx=5)
quiz_entries.append(entry)

# Create labels and entries for midterm and final exams
mid_term_grade_label = ttk.Label(root, text="Mid-Term Exam:")
mid_term_grade_label.grid(row=7, column=0, padx=5, pady=5)
mid_term_grade_entry = ttk.Entry(root)
mid_term_grade_entry.grid(row=7, column=1, padx=5, pady=5)

final_grade_label = ttk.Label(root, text="Final Exam:")
final_grade_label.grid(row=8, column=0, padx=5, pady=5)
final_grade_entry = ttk.Entry(root)
final_grade_entry.grid(row=8, column=1, padx=5, pady=5)

# Create buttons to add new assignment and quiz fields
add_assignment_button = ttk.Button(root, text="Add Assignment", command=add_assignment_field)
add_assignment_button.grid(row=1, column=3, padx=5)

add_quiz_button = ttk.Button(root, text="Add Quiz", command=add_quiz_field)
add_quiz_button.grid(row=5, column=2, padx=5)

# Create a button to calculate the final grade
calculate_button = ttk.Button(root, text="Calculate", command=calculate_grade)
calculate_button.grid(row=9, column=0, columnspan=2, pady=10)

# Create labels to display the final result
weighted_average_label = ttk.Label(root, text="")
weighted_average_label.grid(row=10, column=0, columnspan=2)

final_grade_label = ttk.Label(root, text="")
final_grade_label.grid(row=11, column=0, columnspan=2)

root.mainloop()