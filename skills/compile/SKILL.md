---
name: compile
description: Promote session leftovers that earned a Johnopedia page or a skill edit. Use at the end of a loop, after Close, or when a decision will be asked again. Analog of pstack /reflect plus add-to-johnopedia.
disable-model-invocation: true
---

# Compile

Chat leftovers are not compiled truth. Promote what will be retrieved. Leave the rest.

## Steps

1. List candidates from this session. Decisions, standing facts, killed threads, voice corrections. Trivia stays out.
2. For each candidate, search for an existing page. Update beats a duplicate. If it will not be retrieved, drop it.
3. `put_page` then `get_page`. Provenance on the page. Label inference.
4. Skill edits only when the same instruction appeared twice and a playbook or principle would have caught it. Do not grow playbooks for a one-off.

## Reply

Slugs written, candidates refused and why. No extra memoir of the session.
