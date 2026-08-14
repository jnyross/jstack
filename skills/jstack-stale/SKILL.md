---
name: jstack-stale
description: Compare Johnopedia open loops to live Gmail and Calendar, then propose kills. Use for /jstack-stale, Triage step 3, Friday close-out, or 'what on the action list is already done?'. First automation. If this pass cannot shrink the open list, the rest of jstack is decoration.
disable-model-invocation: true
---

# Jstack stale

The first automation is a pass against live mail and calendar. It is a skill you run, not a daemon. Propose kills. Do not silently delete.

If this pass cannot shrink the open list, say so. The rest of the plugin is decoration until it can.

## Steps

1. Load compiled open loops. Johnopedia `query` / `search` / `recall` / `get_recent_salience` for current-actions, open threads, waiting-on, and similar pages. `get_page` on each candidate before treating it as real. If Johnopedia is down, stop and say so. There is no stale pass without compiled truth.
2. For each open item, prove current state live. Gmail `search_threads` / `get_thread`. Calendar `list_events` / `search_events` / `get_event`. Skip an unavailable connector and say so. Null live results are findings, not proof of still-open.
3. Classify.
   - **Kill.** Live source shows done, declined, paid, sent, or cancelled. Compiled truth still lists it.
   - **Keep.** Live source still shows an open loop. Name the next date or next move.
   - **Unknown.** No live handle. Do not invent a kill.
4. Propose compiled-truth edits. Show the slug, the live id, and the exact page change. Wait for approval before `put_page` that retires a thread. After approval, `put_page` then `get_page`.

Use `subagent_type: "jstack-sweep"`. If `/setup-jstack` has never run, use `subagent_type: "jstack-agent"`. Never Challenge. Never send mail from this skill.

## Reply

Counts. Kills with slug plus live proof. Keeps with next date. Unknowns. If zero kills and the open list did not shrink, one line that the pass failed its job.
