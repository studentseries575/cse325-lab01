<!-- CSE325-2026-L03-T9WD-T3 -->

# Lab 3 - Task 3: Local-Context Requirement

SCOPE_LEDGER = "local_context"

## Genuine Local Requirement

Our campus does not have Wi-Fi available everywhere, and students mostly use mobile data.

### Requirement

The Campus Event Management System should be designed so that students can browse events and register using mobile data without requiring a campus Wi-Fi connection.

## Why This Is a Local Requirement

This requirement comes from our actual campus experience. Wi-Fi is not available everywhere on campus, and students commonly rely on mobile data.

A general AI model could not know this specific constraint because it does not automatically know the network availability and usage conditions of our campus.

## Addition to the Backlog

This local requirement should be added to the project backlog as:

> As a student, I want to browse events and register using mobile data so that I can use the event system even when campus Wi-Fi is unavailable.

### Priority

**Should**

### Justification

The original brief requires students to browse events and register, but it does not specify the network environment. Because campus Wi-Fi is not available everywhere, mobile-data-friendly access is an important local constraint that should influence implementation.

## Traceability

| Requirement | Source |
|---|---|
| Students need to access the system using mobile data | Genuine local campus experience |
| Campus Wi-Fi is not available everywhere | Genuine local campus experience |
| Mobile-data-friendly browsing and registration | Added local-context backlog requirement |

## Why the General Model Could Not Know This

The general project brief only states the required student and admin functionality. It does not contain information about our campus Wi-Fi coverage or students' typical use of mobile data.

Therefore, this requirement could only be added after providing the actual local context.

Scope reconciled against the brief.
CSE325-2026-L03-T9WD