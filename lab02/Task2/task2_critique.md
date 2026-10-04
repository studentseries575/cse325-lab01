# CSE325-2026-L02-M4RB-T2

## Lab 2 Task 2 — AI Critique and Decision Log

### AI Prompt

Critique this Python code specifically for modularity, readability, and maintainability. For each issue, quote the relevant code, identify the principle it affects, and explain whether the suggested improvement should be accepted or rejected for this small standalone program.

---

## AI Suggestions and Decisions

### 1. Separate input, analysis, and reporting

**AI Suggestion:**  
"Separate input, analysis, and reporting."

**Quoted Code:**  
`def analyze_grades():`

**Principle:** Modularity

**Decision:** ACCEPT

**Reason:**  
The `analyze_grades()` function handles input, calculations, and reporting. Splitting these responsibilities into smaller functions will make the calculations easier to test and allow the input and output parts to be changed independently.

---

### 2. Centralize the letter-grade thresholds

**AI Suggestion:**  
"Centralize the letter-grade thresholds."

**Quoted Code:**  
`if average >= 90:`  
and  
`if overall_average >= 90:`

**Principle:** Maintainability

**Decision:** ACCEPT

**Reason:**  
The same A-F grading logic is repeated for individual students and the overall average. A shared `letter_grade()` function will remove duplication and prevent the two grading rules from becoming inconsistent.

---

### 3. Replace the fixed grade count with a named value

**AI Suggestion:**  
"Replace the fixed grade count with a named value."

**Quoted Code:**  
`for j in range(3):`

**Principle:** Readability and Maintainability

**Decision:** ACCEPT

**Reason:**  
The value `3` represents the number of grades for each student, but its meaning is not immediately clear. A name such as `GRADES_PER_STUDENT` would make the purpose clearer and make future changes easier.

---

### 4. Remove or use the unused constant

**AI Suggestion:**  
"Remove or use the unused constant."

**Quoted Code:**  
`QUALITY_BASELINE = "before"`

**Principle:** Readability and Maintainability

**Decision:** REJECT

**Reason:**  
`QUALITY_BASELINE` is required as the primary configuration constant for this CSE325 Lab 2 task. Removing it would conflict with the assignment requirement even though it is not used by the program logic.

---

### 5. Replace student dictionaries with a class or dataclass

**AI Suggestion:**  
"Replace student dictionaries with a class or dataclass."

**Quoted Code:**  
`students.append({"name": name, "grades": grades})`

**Principle:** Modularity and Maintainability

**Decision:** REJECT

**Reason:**  
The current program only stores two fields, `name` and `grades`, and has one main consumer. Adding a class or dataclass would introduce extra structure without providing enough benefit for this small program.

---

### 6. Move grading rules into a separate module or configuration system

**AI Suggestion:**  
"Move grading rules into a separate module or configuration system."

**Quoted Code:**  
`def analyze_grades():`

**Principle:** Modularity and Maintainability

**Decision:** REJECT

**Reason:**  
This is a small standalone program and does not currently share grading rules with other programs. Creating another module or configuration layer would increase setup and navigation without solving an important problem in the current code.

---

## Summary of Decisions

### Accepted Suggestions

1. Separate input, analysis, and reporting.
2. Centralize the letter-grade thresholds.
3. Replace the fixed grade count with a named value.

### Rejected Suggestions

1. Remove or use the `QUALITY_BASELINE` constant.
2. Replace student dictionaries with a class or dataclass.
3. Move grading rules into a separate module or configuration system.

The rejected suggestions were not accepted because they either conflict with the lab requirement or add unnecessary complexity to this small standalone program.

Scope of the critique was limited to the provided `grade_analyzer.py` implementation.

CSE325-2026-L02-M4RB-T2