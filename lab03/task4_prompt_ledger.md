<!-- CSE325-2026-L03-T9WD-T4 -->

# Lab 3 - Task 4: Prompt Ledger

SCOPE_LEDGER = "prompt_ledger"

The following ledger records the actual prompts used during the planning process and the changes made after reviewing their results.

| # | Actual Prompt | Result | What Changed | Why |
|---|---|---|---|---|
| 1 | Act as a software project planner. Break the Campus Event Management System into 4-6 modules. For each module list 3-5 concrete engineering tasks. Give the result as a nested list. | The AI produced a first-pass WBS with modules such as Event Browsing, Event Registration, Event Reminders, Admin Event Addition, and Admin Event Removal. | The first draft was reviewed against the project brief and unsupported details and missing concrete implementation links were identified. | The first AI output was treated as a starting point rather than a final plan. |
| 2 | Review your previous WBS for the following brief: “students browse events, register, and get reminders; admins add and remove events.” Now create a more detailed WBS with 4-6 modules and 3-5 concrete engineering tasks per module. Do NOT simply repeat the brief as one task. Break each requirement into concrete tasks. Do not intentionally omit any requirement from the brief, but produce your best first-draft plan without manually checking it afterward. | The AI produced another detailed WBS, but it still covered all five high-level requirements and therefore did not provide the omissions needed for the graded reconciliation exercise. | This attempt was superseded by a more constrained first-pass prompt. | The result did not expose enough omissions at the engineering-task level for Task 1 reconciliation. |
| 3 | Act as a software project planner. Produce a quick first-pass WBS for this brief: “students browse events, register, and get reminders; admins add and remove events.” Use exactly 4 modules and exactly 2 concrete engineering tasks per module. Do not add extra features such as authentication, cancellation, filtering, reporting, or analytics. Do not explain the result and do not revise or verify it afterward. Just give the first-pass WBS. | The AI produced four modules with two tasks each: Event Browsing, Event Registration, Event Reminders, and Admin Event Management. | This became the first-pass WBS used for the final Task 1 reconciliation. Additional traceable engineering tasks were added where the first pass was not sufficiently detailed. | The constrained output was easier to audit against the brief and identify unsupported or missing implementation details. |
| 4 | Act as a software project planner. Using this project brief: “students browse events, register, and get reminders; admins add and remove events.” Create at least 10 user stories. Use this format for every story: “As a <role>, I want <goal> so that <benefit>.” Then apply MoSCoW prioritisation to each story: Must, Should, Could, Won't. Give a one-line justification for every priority. Do not add explanations outside the user-story list. | The AI generated 12 user stories distributed across Must, Should, Could, and Won't. | The stories were organised into the required backlog table, and three Must priorities were defended against specific competing Should stories. | The Task 2 deliverable required at least 10 stories and explicit defence of three Must labels. |

## Failed / Superseded Attempts

### Attempt 2 - Superseded

The second WBS prompt was superseded because its output still covered all five high-level requirements. It did not provide enough useful omissions for the required reconciliation exercise.

### Attempt 3 - Used as the Final First-Pass WBS

The constrained four-module/two-task prompt produced a smaller first-pass WBS. This output was used as the evidence for the Task 1 reconciliation.

## Planning Process Changes

The planning process changed from a broad AI-generated WBS to a more constrained first-pass WBS so that the AI output could be checked more clearly against the project brief.

The user-story prompt was then used separately to create the prioritised backlog required for Task 2.

Scope reconciled against the brief.
CSE325-2026-L03-T9WD