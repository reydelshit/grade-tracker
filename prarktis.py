import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout

class GradeCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grade Calculator")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create and add widgets
        self.create_weight_widgets()
        self.create_grade_widgets()
        self.create_result_widgets()
        self.create_button_widgets()

    def create_weight_widgets(self):
        weight_label = QLabel("Enter the weights for each category (in percentage):")
        self.layout.addWidget(weight_label)

        self.assignments_weight_entry = QLineEdit()
        self.assignments_weight_entry.setPlaceholderText("Assignments")
        self.layout.addWidget(self.assignments_weight_entry)

        self.quizzes_weight_entry = QLineEdit()
        self.quizzes_weight_entry.setPlaceholderText("Quizzes")
        self.layout.addWidget(self.quizzes_weight_entry)

        self.mid_term_weight_entry = QLineEdit()
        self.mid_term_weight_entry.setPlaceholderText("Mid-Term")
        self.layout.addWidget(self.mid_term_weight_entry)

        self.final_exam_weight_label = QLabel() 
        self.layout.addWidget(self.final_exam_weight_label)

        # Connect the calculation of final exam weight to signal of all weight entries being filled
        self.assignments_weight_entry.editingFinished.connect(self.calculate_final_exam_weight)
        self.quizzes_weight_entry.editingFinished.connect(self.calculate_final_exam_weight)
        self.mid_term_weight_entry.editingFinished.connect(self.calculate_final_exam_weight)
    
    def calculate_final_exam_weight(self):
        try:
            # Check if all weight entries are filled
            if self.assignments_weight_entry.text() and self.quizzes_weight_entry.text() and self.mid_term_weight_entry.text():
                # Define the weights for each category
                assignments_weight = float(self.assignments_weight_entry.text()) / 100
                quizzes_weight = float(self.quizzes_weight_entry.text()) / 100
                mid_term_weight = float(self.mid_term_weight_entry.text()) / 100

                # Calculate the remaining weight for the final exam
                final_weight = 1 - (assignments_weight + quizzes_weight + mid_term_weight)

                # Update the label to display the final exam weight
                self.final_exam_weight_label.setText(f"Final Exam Weight: {final_weight * 100:.2f}%")
        except ValueError:
            pass

    def create_grade_widgets(self):
        grade_label = QLabel("Enter the grades for each category (e.g., '9/10'):")
        self.layout.addWidget(grade_label)

        self.assignment_entries = [QLineEdit()]
        self.assignment_entries[0].setPlaceholderText("Assignment 1")
        self.layout.addWidget(self.assignment_entries[0])

        self.quiz_entries = [QLineEdit()]
        self.quiz_entries[0].setPlaceholderText("Quiz 1")
        self.layout.addWidget(self.quiz_entries[0])

        self.mid_term_grade_entry = QLineEdit()
        self.mid_term_grade_entry.setPlaceholderText("Mid-Term Exam")
        self.layout.addWidget(self.mid_term_grade_entry)

        self.final_grade_entry = QLineEdit()
        self.final_grade_entry.setPlaceholderText("Final Exam")
        self.layout.addWidget(self.final_grade_entry)

    def create_result_widgets(self):
        self.weighted_average_label = QLabel("")
        self.layout.addWidget(self.weighted_average_label)

        self.final_grade_label = QLabel("")
        self.layout.addWidget(self.final_grade_label)

    def create_button_widgets(self):
        add_assignment_button = QPushButton("Add Assignment")
        add_assignment_button.clicked.connect(self.add_assignment_field)
        self.layout.addWidget(add_assignment_button)

        add_quiz_button = QPushButton("Add Quiz")
        add_quiz_button.clicked.connect(self.add_quiz_field)
        self.layout.addWidget(add_quiz_button)

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_grade)
        self.layout.addWidget(calculate_button)

    def calculate_grade(self):
        try:
            # Define the weights for each category
            assignments_weight = float(self.assignments_weight_entry.text()) / 100
            quizzes_weight = float(self.quizzes_weight_entry.text()) / 100
            mid_term_weight = float(self.mid_term_weight_entry.text()) / 100
            final_weight = 1 - (assignments_weight + quizzes_weight + mid_term_weight)

            # Get the grades for each category
            assignments_grades = [self.extract_grade(entry.text()) for entry in self.assignment_entries]
            quizzes_grades = [self.extract_grade(entry.text()) for entry in self.quiz_entries]

            # Get the grades for mid-term and final exams
            mid_term_grade = self.extract_grade(self.mid_term_grade_entry.text())
            final_grade = self.extract_grade(self.final_grade_entry.text())

            # Calculate the final grade
            total_weighted_grades = (sum(assignments_grades) * assignments_weight +
                                    sum(quizzes_grades) * quizzes_weight +
                                    mid_term_grade * mid_term_weight +
                                    final_grade * final_weight)
            total_weight = assignments_weight + quizzes_weight + mid_term_weight + final_weight
            final_grade_percent = (total_weighted_grades / total_weight) * 100

            # Update the result labels
            self.weighted_average_label.setText(f"Weighted Average: {final_grade_percent:.2f}%")
            self.final_grade_label.setText(f"Final Grade: {final_grade_percent:.2f}%")
        except ValueError:
            self.weighted_average_label.setText("Please enter valid grades and weights.")

    def extract_grade(self, text):
        if '/' in text:
            parts = text.split('/')
            if len(parts) == 2:
                try:
                    return float(parts[0]) / float(parts[1])
                except ValueError:
                    return 0.0
        return 0.0

    def add_assignment_field(self):
        index = len(self.assignment_entries) + 6
        new_entry = QLineEdit()
        new_entry.setPlaceholderText(f"Assignment {index - 5}")
        self.layout.addWidget(new_entry)
        self.assignment_entries.append(new_entry)

    def add_quiz_field(self):
        index = len(self.quiz_entries) + 6
        new_entry = QLineEdit()
        new_entry.setPlaceholderText(f"Quiz {index - 5}")
        self.layout.addWidget(new_entry)
        self.quiz_entries.append(new_entry)


def main():
    app = QApplication(sys.argv)
    window = GradeCalculatorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()