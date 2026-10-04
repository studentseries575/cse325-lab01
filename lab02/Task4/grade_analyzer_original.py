# CSE325-2026-L02-M4RB-T1

QUALITY_BASELINE = "before"

def analyze_grades():
    print("Grade Analyzer")

    students = []

    count = int(input("Enter number of students: "))

    for i in range(count):
        name = input("Enter student name: ")
        grades = []

        for j in range(3):
            grade = float(input(f"Enter grade {j + 1}: "))
            grades.append(grade)

        students.append({"name": name, "grades": grades})

    total_students = len(students)

    if total_students == 0:
        print("No student records found.")
        return

    total_average = 0

    for student in students:
        grades = student["grades"]

        average = sum(grades) / len(grades)
        total_average += average

        if average >= 90:
            letter = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        elif average >= 60:
            letter = "D"
        else:
            letter = "F"

        print(
            f"Student: {student['name']}, "
            f"Average: {average:.2f}, Grade: {letter}"
        )

    overall_average = total_average / total_students

    if overall_average >= 90:
        overall_letter = "A"
    elif overall_average >= 80:
        overall_letter = "B"
    elif overall_average >= 70:
        overall_letter = "C"
    elif overall_average >= 60:
        overall_letter = "D"
    else:
        overall_letter = "F"

    print(f"Overall Average: {overall_average:.2f}")
    print(f"Overall Grade: {overall_letter}")


if __name__ == "__main__":
    analyze_grades()