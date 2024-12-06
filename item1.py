#Initialization of the student's name, final quizzes, final research/assignment, final project, and final exam ratings.
student_name = ""
final_quizzes = 0
final_research = 0
final_project = 0
final_exam = 0
final_grade = 0
grading_remark = 0

#Input the student's name, final quizzes, final research/assignment, final project, and final exam ratings
student_name = str(input("Enter student's name: "))
final_quizzes = float(input("Enter the grade in the final quizzes: "))
final_research = float(input("Enter the grade in the final research: "))
final_project = float(input("Enter the grade in the final project: "))
final_exam = float(input("Enter the grade in the final exam: "))

#Computing the final grade
final_grade = (0.30 * final_quizzes) + (0.10 * final_research) + (0.40 * final_exam) + (0.20 * final_project)
round_final_grade = round(final_grade)

#Determining the equivalent grading remark
if 98 <= round_final_grade <= 100:
    grading_remark = 4.00
elif 95 <= round_final_grade <= 97:
    grading_remark = 3.75
elif 92 <= round_final_grade <= 94:
    grading_remark = 3.50
elif 89 <= round_final_grade <= 91:
    grading_remark = 3.25
elif 86 <= round_final_grade <= 88:
    grading_remark = 3.00
elif 83 <= round_final_grade <= 85:
    grading_remark = 2.75
elif 80 <= round_final_grade <= 82:
    grading_remark = 2.50
elif 77 <= round_final_grade <= 79:
    grading_remark = 2.25
elif 74 <= round_final_grade <= 76:
    grading_remark = 2.00
elif 71 <= round_final_grade <= 73:
    grading_remark = 1.75
elif 68 <= round_final_grade <= 70:
    grading_remark = 1.50
elif 64 <= round_final_grade <= 67:
    grading_remark = 1.25
elif 60 <= round_final_grade <= 63:
    grading_remark = 1.00
else:
    grading_remark = "Invalid"

#Displaying student's name, final quizzes, final research/assignment, final project, final grade, and the equivalent grading remark
print("----------------------------")
print("Student's Name: ", student_name)
print("Final Quizzes: ", final_quizzes)
print("Final Research/Assignment :", final_research)
print("Final Project: ", final_project)
print("Final Grade: ", round_final_grade)
print("Equivalent Grading Remark :", grading_remark)
