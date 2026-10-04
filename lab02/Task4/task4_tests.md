# Lab 2 Task 4 — Test Evidence

## Test File

`lab02/Task4/test_grade_analyzer.py`

## Original Version

Command:

`$env:TARGET_FILE="lab02/Task4/grade_analyzer_original.py"`

`py -m pytest lab02\Task4\test_grade_analyzer.py`

Result:

`3 passed`

## Refactored Version

Command:

`$env:TARGET_FILE="lab02/Task1/grade_analyzer.py"`

`py -m pytest lab02\Task4\test_grade_analyzer.py`

Result:

`3 passed`

## Tests Used

1. Single student with grades 80, 90, 100 → Average 90.00, Grade A.
2. Failing student with grades 40, 50, 60 → Average 50.00, Grade F.
3. Zero students → "No student records found."

## What These Tests Would Not Catch

These tests verify the main expected outputs, but they would not catch cosmetic readability problems, poor variable names, or unnecessary code duplication if the program still produces the same results.

CSE325-2026-L02-M4RB-T4