<!-- CSE325-2026-L03-T9WD-T1 -->

# Lab 3 - Task 1: Reconciled WBS

SCOPE_LEDGER = "reconciled_wbs"

## Project Brief

> “students browse events, register, and get reminders; admins add and remove events.”

## AI First-Pass WBS

The AI generated the following first-pass WBS:

### Event Browsing
- Build a student-facing view for browsing events.
- Display available events in the view.

### Event Registration
- Add a registration action for an event.
- Record which student registered for the event.

### Event Reminders
- Identify students registered for each event.
- Send reminders to those students about their events.

### Admin Event Management
- Implement an action for admins to add an event.
- Implement an action for admins to remove an event.

---

## Reconciled WBS

| ID | Module | Engineering Task | Traceability |
|---|---|---|---|
| WBS-01 | Event Browsing | Build a student-facing view for browsing events. | “students browse events” |
| WBS-02 | Event Browsing | Display available events in the view. | “students browse events” |
| WBS-03 | Event Browsing | Include events added by admins in the student browsing view. | ADDED - required to connect “admins add” with “students browse” |
| WBS-04 | Event Registration | Add a registration action for an event. | “students ... register” |
| WBS-05 | Event Registration | Record which student registered for the event. | “students ... register” |
| WBS-06 | Event Registration | Prevent registration for events that admins have removed. | ADDED - required to support “admins remove events” with registration |
| WBS-07 | Event Reminders | Identify students registered for each event. | ADDED - AI-derived detail not explicitly stated in the brief |
| WBS-08 | Event Reminders | Send reminders to those students about their events. | “students ... get reminders” |
| WBS-09 | Admin Event Management | Implement an action for admins to add an event. | “admins add ... events” |
| WBS-10 | Admin Event Management | Implement an action for admins to remove an event. | “admins ... remove events” |
| WBS-11 | Admin Event Management | Make added events available for student browsing and registration. | ADDED - required to make the “add events” requirement operational |
| WBS-12 | Admin Event Management | Remove deleted events from student browsing. | ADDED - required to make the “remove events” requirement operational |

---

## AI-Invented / Unsupported Task

The following task appeared in the actual AI output but is not explicitly stated in the project brief:

> “Identify students registered for each event.”

Reason:

The brief only says that students register for events and get reminders. It does not explicitly state that the system must identify registered students as a separate engineering task.

Therefore this task is recorded as an AI-derived detail that requires verification before being treated as a confirmed requirement.

---

## Reconciled Omissions / Added Tasks

The first-pass AI WBS covered all five high-level requirements, but it did not break some of them into the concrete engineering tasks needed for a complete implementation.

### Omission 1

The AI did not explicitly connect admin-added events with student browsing.

**ADDED:**
> Make added events available for student browsing and registration.

Reason: An admin adding an event must result in that event becoming available to students.

### Omission 2

The AI did not explicitly state what happens to student browsing when an admin removes an event.

**ADDED:**
> Remove deleted events from student browsing.

Reason: This makes the “admins remove events” requirement traceable to the student-facing system behavior.

### Additional reconciliation

The AI also did not explicitly connect event removal with registration.

**ADDED:**
> Prevent registration for events that admins have removed.

Reason: A removed event should not remain available for registration.

---

## Verification Against the Brief

| Brief Requirement | Reconciled WBS IDs | Status |
|---|---|---|
| Students browse events | WBS-01, WBS-02, WBS-03 | Covered |
| Students register | WBS-04, WBS-05, WBS-06 | Covered |
| Students get reminders | WBS-07, WBS-08 | Covered |
| Admins add events | WBS-09, WBS-11 | Covered |
| Admins remove events | WBS-10, WBS-12 | Covered |

Every reconciled WBS item is either traced to an exact brief phrase or explicitly marked `ADDED` with a reason.

Scope reconciled against the brief.
CSE325-2026-L03-T9WD