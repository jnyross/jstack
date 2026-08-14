---
name: principle-compiled-truth-earns-a-page
description: "Apply when you will be asked this again, or a decision needs an audit trail. Write it to Johnopedia in the same session. Chat transcripts are not the system of record. Trivia does not get a page."
disable-model-invocation: true
---

# Compiled truth earns a page

Write durable facts and decisions to Johnopedia in the same session. Chat is not the system of record.

**Why:** Transcripts rot. A decision that only lives in this thread will be re-litigated. A page that will never be retrieved is how action lists rot the other way.

**Pattern:** Search first (`search`, `query`). Update beats a duplicate. `put_page` then `get_page`. Provenance on the page. If you cannot name who would retrieve this, do not write it.

**Does not change:** Working notes that die with the turn. Triage dockets. Drafts waiting on send approval.
