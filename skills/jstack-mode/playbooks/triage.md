### Triage

**You own the docket. Plan, classify, kill stale loops.**

Inbox, calendar, WhatsApp, or Linear has piled up. The user wants a docket, not a novel. Done is a short list tagged Archive / Action / Skip, with compiled-truth items that live sources already settled marked closed.

1. Pull live Gmail and Calendar first. Use `search_threads` and `list_events` / `search_events`. GBrain (`query`, `search`, `get_page`, `recall`, `get_recent_salience`) is for "did we already handle this?", not for whether it is still true.
2. Classify each item Archive / Action / Skip. That rule is already in use. Keep it. See the mode skill for the three buckets.
3. If GBrain still lists a thread the live source shows done, kill it in compiled truth in the same pass. Run the **jstack-stale** skill. Propose the page edit. Do not silently delete. `get_page` after `put_page`.
4. Hand Action items to Close, Write, or Decide. Do not grow a parking lot.

Use `subagent_type: "jstack-sweep"` for the fan-out. If `/setup-jstack` has never run, use `subagent_type: "jstack-agent"`. Skip Linear and WhatsApp unless the pile is actually there. Skip an unavailable MCP and say so.

**Reply:** the docket. One line per item, tagged Archive / Action / Skip, with a live citation (gmail thread id or event id). List compiled-truth kills separately, each with the slug and the live proof. One next move for the first Action item. If the stale pass could not shrink the open list, say that in one line.
