<!-- CSE325-2026-L05-C6VN-T3 -->
<!-- REQ_SOURCE_MAP: Quality attributes traced to stakeholder source -->

# Lab 5 — Task 3: Measurable Quality Attributes

## Purpose

The stakeholder source contains vague quality statements such as “fast”,
“secure”, “quick”, and “many users”. These statements are rewritten as
measurable requirements while keeping their original meaning.

## Quality Attribute Register

| ID | Original Statement | Measurable Requirement | Measurement |
|---|---|---|---|
| QA-01 | “It should be fast.” | Event browsing pages should load within **2 seconds** under normal operating conditions. | Measure page response/load time. |
| QA-02 | “It should be secure.” | The system must use **authenticated access** for student and admin functions and must protect user credentials during login. | Verify authentication and credential protection. |
| QA-03 | “Login must also be quick.” | Login should complete within **2 seconds** under normal operating conditions. | Measure login response time. |
| QA-04 | “The system should handle many users.” | The system should support **100 concurrent users** while maintaining the stated response-time targets. | Run a concurrent-user load test and measure response time. |

## Conditions and Tolerances

- Response-time targets are measured under normal operating conditions.
- A response is considered within target when it completes in **2 seconds
  or less**.
- The concurrent-user target is **100 users**.
- Security is verified through the required authentication and credential
  protection checks.

## Traceability

QA-01 is derived from the stakeholder statement “It should be fast.”

QA-02 is derived from the stakeholder statement “It should be secure.”

QA-03 is derived from the stakeholder statement “Login must also be quick.”

QA-04 is derived from the stakeholder statement “The system should handle
many users.”

These numeric targets are proposed measurable acceptance criteria; the
stakeholder source itself does not provide these exact numbers.

Traced to the stakeholder source text.

CSE325-2026-L05-C6VN