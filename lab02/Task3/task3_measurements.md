# CSE325-2026-L02-M4RB-T3

# Lab 2 Task 3 — Apply, Re-measure, and Account for Every Number

## Accepted Changes Applied

The following accepted AI suggestions were applied:

1. Separated input, analysis, and reporting into smaller functions.
2. Centralized the repeated letter-grade thresholds in `letter_grade()`.
3. Replaced the magic number `3` in the grade input loop with `GRADES_PER_STUDENT = 3`.

## Before and After Measurements

| Metric | Before | After | Change |
|---|---:|---:|---|
| Ruff violations | 0 | 0 | No change |
| Highest cyclomatic complexity | 13 | 5 | Decreased by 8 |
| Longest function | 62 lines | 26 lines | Decreased by 36 lines |
| Worst-function parameter count | 0 | 0 | No change |

## Explanation of Each Movement

### Ruff violations: 0 → 0

The Ruff result stayed at zero because the original code did not contain any Ruff rule violations. The refactoring therefore did not produce a measurable change in linting violations.

### Highest cyclomatic complexity: 13 → 5

The highest complexity decreased from 13 to 5. The original `analyze_grades()` function contained both student grading logic and overall grading logic, including repeated conditional branches. Extracting the grading logic into `letter_grade()` reduced the number of decision paths inside the main function.

### Longest function: 62 → 26 lines

The longest function became much shorter because the original `analyze_grades()` function contained input collection, grade calculation, grading decisions, and reporting. These responsibilities were separated into `read_student_records()`, `calculate_average()`, `letter_grade()`, and `analyze_grades()`.

### Worst-function parameter count: 0 → 0

The parameter count did not change because the original `analyze_grades()` function had no parameters, and the refactored functions also do not have a function with more than zero parameters in the baseline comparison used for this task.

## Raw Tool Output — After Refactoring

### Ruff

All checks passed!

### Radon

lab02\Task1\grade_analyzer.py
    F 28:0 letter_grade - A (5)
    F 7:0 read_student_records - A (3)
    F 41:0 analyze_grades - A (3)
    F 24:0 calculate_average - A (1)

### Git Diff Stat

 lab02/Task1/grade_analyzer.py | 63 ++++++++++++++++++++++---------------------
 1 file changed, 32 insertions(+), 31 deletions(-)

## Result

The main measurable improvement was a reduction in complexity and function size. Ruff remained clean, while the highest cyclomatic complexity decreased from 13 to 5 and the longest function decreased from 62 lines to 26 lines. The parameter count remained unchanged because the original function already had zero parameters.

Measured against the construction baseline.
CSE325-2026-L02-M4RB-T3
