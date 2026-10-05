<!-- CSE325-2026-L05-C6VN-T4 -->
<!-- REQ_SOURCE_MAP: Duplicate and contradiction review -->

# Lab 5 — Task 4: Duplicate and Contradiction Handling

## Review Method

The requirements from Task 1 were reviewed for duplicate requirements and
contradictions. Each requirement was compared with the stakeholder source
text before being accepted.

## Duplicate Review

| Requirements | Result | Action |
|---|---|---|
| R2 — Application should be fast | No duplicate | Keep |
| R8 — Login should be quick | No duplicate | Keep |

Although both requirements concern speed, they apply to different scopes.
R2 concerns the application generally, while R8 specifically concerns
login. Therefore, they are not treated as duplicates.

## Contradiction Review

No direct contradiction was found in the stakeholder source text.

The following requirements are compatible:

- Students can log in with their university email.
- Students can register for events.
- Students receive reminders before events.
- Admins can add or remove events.
- The system should be fast and secure.
- The system should handle many users.

No requirement states the opposite of another requirement.

## Resolution Rule

If a future AI-generated requirement duplicates an existing requirement,
the existing sourced requirement will be retained and the duplicate will
be recorded as a duplicate rather than silently creating a new requirement.

If two requirements contradict each other, both statements will be recorded
with their source, and the contradiction will be flagged for stakeholder
clarification. No requirement will be silently deleted or changed.

## Conclusion

The current stakeholder source contains no confirmed duplicate or
contradictory requirement that requires resolution.

Traced to the stakeholder source text.

CSE325-2026-L05-C6VN