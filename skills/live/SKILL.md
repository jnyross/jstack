---
name: live
description: Prove a time-sensitive fact against Gmail, Calendar, or the web. Use when a fact might have changed since ingest, or when about to answer 'is this still open?' from a Johnopedia page.
disable-model-invocation: true
---

# Live

GBrain is a lead. Live connectors are the test.

## Steps

1. Name the claim and which live source could falsify it.
2. Read that source. Gmail `search_threads` / `get_thread` / `get_message`. Calendar `list_events` / `search_events` / `get_event`. Browser for a public page. Linear `get_issue` only if the loop is a work ticket.
3. Compare to compiled truth (`get_page` or the ingested action list). If they disagree, live wins for current state.
4. Return the live id. If the source is unavailable, say so. Do not fall back to the page as if it were live.

## Reply

Claim, live result with id, compiled-truth comparison, memory vs live labels. Null is a finding.
