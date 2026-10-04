# CSE325-2026-L02-M4RB-T3

QUALITY_BASELINE = "after"
GRADES_PER_STUDENT = 3


def read_student_records():
    students = []
    count = int(input("Enter number of students: "))

    for i in range(count):
        name = input("Enter student name: ")
        grades = []

        for j in range(GRADES_PER_STUDENT):
            grade = float(input(f"Enter grade {j + 1}: "))
            grades.append(grade)

        students.append({"name": name, "grades": grades})

    return students


def calculate_average(grades):
    return sum(grades) / len(grades)


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def analyze_grades():
    print("Grade Analyzer")

    students = read_student_records()
    total_students = len(students)

    if total_students == 0:
        print("No student records found.")
        return

    total_average = 0

    for student in students:
        average = calculate_average(student["grades"])
        total_average += average
        letter = letter_grade(average)

        print(
            f"Student: {student['name']}, "
            f"Average: {average:.2f}, Grade: {letter}"
        )

    overall_average = total_average / total_students
    overall_letter = letter_grade(overall_average)

    print(f"Overall Average: {overall_average:.2f}")
    print(f"Overall Grade: {overall_letter}")


if __name__ == "__main__":
    analyze_grades()