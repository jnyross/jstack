---
name: drafts
description: N variants of a letter or a decision memo, then pick a base and graft. Use when wording is load-bearing, Write step 3, or Decide wants competing memos. Analog of pstack /arena, different object.
disable-model-invocation: true
---

# Drafts

Same shape as pstack arena. The object is prose, not a diff.

## Steps

1. Lock the audience, the constraint, and the done artifact (Gmail draft, chat memo, decision page section).
2. Spawn N variants on the panel from `/setup-jstack` (default 3). Split the `challenge panel` line on commas; one variant per entry. Each variant is a full draft, not a bullet list of tones. Always `subagent_type: "jstack-agent"`; put each panel entry on Task `model` (omit `model` for `inherit-parent` or `auto`).
3. Pick a base. Graft a line or two from the others only when they are strictly better, not to average them.
4. Show the exact chosen text. Apply **unslop**. Do not send.

## Reply

The chosen draft in full, which variant was the base, what was grafted, and a wait for send or page-write approval if the next step changes the world.
