---
name: principle-memory-vs-live
description: "Apply on any time-sensitive fact. RSVPs, payments, bookings, 'is this still open?'. GBrain is durable context. Gmail, Calendar, and the web are live truth. Never answer done from an ingested action list."
disable-model-invocation: true
---

# Memory vs live

GBrain holds durable preference, history, and compiled pages. Gmail, Calendar, and the web hold whether it is still true.

**Why:** Ingested action lists lag. An open item in compiled truth is a lead. Treating it as current state is how settled bookings stay "open" for weeks.

**Pattern:** Before answering "is this done?", "are we going?", "did they reply?", or any RSVP, payment, or booking state, read the live connector. Cite the thread id or event id. If the live source disagrees with the page, the live source wins for current state. The page gets updated or killed in the same turn.

**Does not change:** Relationship context, voice, past decisions, household preference. Those stay on the page until a new decision replaces them.
