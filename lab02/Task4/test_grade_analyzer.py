# CSE325-2026-L02-M4RB-T4

QUALITY_BASELINE = "tests"

import os
import subprocess
import sys


TARGET_FILE = os.environ.get(
    "TARGET_FILE",
    "lab02/Task1/grade_analyzer.py"
)


def run_program(input_data):
    result = subprocess.run(
        [sys.executable, TARGET_FILE],
        input=input_data,
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout


def test_single_student_grade():
    input_data = "1\nAli\n80\n90\n100\n"
    output = run_program(input_data)

    assert "Student: Ali, Average: 90.00, Grade: A" in output
    assert "Overall Grade: A" in output


def test_failing_grade():
    input_data = "1\nSara\n40\n50\n60\n"
    output = run_program(input_data)

    assert "Student: Sara, Average: 50.00, Grade: F" in output
    assert "Overall Grade: F" in output


def test_no_students():
    input_data = "0\n"
    output = run_program(input_data)

    assert "No student records found." in output