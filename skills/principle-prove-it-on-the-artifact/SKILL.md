---
name: principle-prove-it-on-the-artifact
description: "Apply when about to say done. Read the sent draft, the live event, or get_page. Do not trust the agent's summary of what it did."
disable-model-invocation: true
---

# Prove it on the artifact

Done means you read the real thing. Not a proxy. Not your own recap.

**Why:** Agents report what they intended. `create_draft` is not sent mail. `put_page` without `get_page` is an unconfirmed write. A calendar page in GBrain is not today's event.

**Pattern:** After a write, read it back. After a send (once approved), `get_thread` or `get_message` on the live id. After an event change, `get_event`. After a page update, `get_page`. Cite that id in the reply.

**Does not change:** Reversible work still in draft. Those are in progress, not done.
