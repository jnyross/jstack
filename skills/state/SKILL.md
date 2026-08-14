---
name: state
description: Rebuild working context for catch-up or meeting prep. Use for 'catch me up', 'prep me for this meeting', 'where did we leave this?', or Brief playbook step 4.
disable-model-invocation: true
---

# State

Rebuild working context, then stop. Analog of pstack `/recall`, aimed at people and threads instead of a git branch.

## Steps

1. Lock scope. Topic, window, which calendars or inboxes. State it back. Default window is the next 48 hours for meeting prep, last 7 days for catch-up.
2. Fan out with `subagent_type: "jstack-sweep"`. GBrain `query`, `get_page`, `get_recent_salience`, `recall`. Live Calendar `list_events`. Live Gmail `search_threads`. Linear only if the topic is work.
3. Verify time-sensitive facts with the **live** skill. RSVP state, "did they reply", and "is this still on" never come from a page alone.
4. Write the brief to the contract below. Cut adjacent threads unless they block this one.

## Output contract

- **Capsule.** At most 5 bullets. What this is and where it stands.
- **Threads.** One line each, tagged `[live]`, `[memory]`, or `[conflict]`. Cite slug, gmail id, or event id.
- **Next move.** One concrete action.

**Reply:** the brief, to that contract. Apply **unslop**.
