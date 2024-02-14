def calculate_final_grade(grades, weights):
    # Calculate the sum of weighted grades
    weighted_sum = sum(grades[i] * weights[i] for i in range(len(grades)))

    # Calculate the total weight
    total_weight = sum(weights)

    # Calculate the final grade by dividing the weighted sum by the total weight
    final_grade = weighted_sum / total_weight

    return final_grade

def main():
    # Subject name input
    subject = input("Enter the subject name: ")

    # Define the weights for each category
    total_weight = 100
    assignments_weight = float(input("Enter the weight for assignments (in percentage): "))
    quizzes_weight = float(input("Enter the weight for quizzes (in percentage): "))
    mid_term_weight = float(input("Enter the weight for the mid-term (in percentage): "))
    final_weight = total_weight - (assignments_weight + quizzes_weight + mid_term_weight)
    weights = [assignments_weight / 100, quizzes_weight / 100, mid_term_weight / 100, final_weight / 100]

    # Display percentages for each category
    print("\nWeights for each category:")
    print(f"- {assignments_weight}% for Assignments")
    print(f"- {quizzes_weight}% for Quizzes")
    print(f"- {mid_term_weight}% for Mid-Term")
    print(f"- {final_weight}% for Final")

    # Get the number of assignments
    num_assignments = int(input("Enter the number of assignments: "))

    # Get grades for each assignment
    assignments_grades = []
    for i in range(num_assignments):
        score, total = map(float, input(f"Enter score and total for assignment {i+1} (e.g., '9/10'): ").split('/'))
        assignments_grades.append(score / total)

    # Get the number of quizzes
    num_quizzes = int(input("Enter the number of quizzes: "))

    # Get grades for each quiz
    quizzes_grades = []
    for i in range(num_quizzes):
        score, total = map(float, input(f"Enter score and total for quiz {i+1} (e.g., '9/10'): ").split('/'))
        quizzes_grades.append(score / total)

    # Get the grade for the mid-term exam
    mid_term_grade, mid_term_total = map(float, input("Enter score and total for mid-term exam (e.g., '80/100'): ").split('/'))
    
    # Get the grade for the final exam
    final_grade, final_total = map(float, input("Enter score and total for final exam (e.g., '80/100'): ").split('/'))

    # Calculate the total grades for each category
    total_grades = [sum(assignments_grades), sum(quizzes_grades), mid_term_grade / mid_term_total, final_grade / final_total]

    # Calculate the final grade using the calculate_final_grade function
    final_grade = calculate_final_grade(total_grades, weights)

    # Calculate the weighted average
    weighted_average = sum(grades * weights[i] for i, grades in enumerate(total_grades))

    # Convert final grade and weighted average to percentages
    final_grade_percent = final_grade * 100
    weighted_average_percent = weighted_average * 100

    # Print the weighted average
    print(f"\nWeighted Average for {subject}: {weighted_average_percent:.2f}%")

    # Print explanation of how the grades are calculated
    print("\nWe calculate the final grade by dividing the sum of the weighted grades by the total weight.")

    # Print the final grade for the subject
    print(f"Final Grade for {subject}: {final_grade_percent:.2f}%")

if __name__ == "__main__":
    main()