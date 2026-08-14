---
name: setup-jstack
description: Configure which models jstack uses per role. Detects available models and writes role agents under ~/.cursor/agents. Use for /setup-jstack, "configure jstack models", or changing sweep vs judgment vs challenge panel.
disable-model-invocation: true
---

# Setup jstack

Write one role agent per configured model under `~/.cursor/agents/`. The role agents are `jstack-sweep`, `jstack-prose`, `jstack-judgment`, and one `jstack-panel-<number>` file per challenge panel member. If no role agent files exist, every role falls back to the shipped `jstack-agent`, which uses `inherit` and the parent chat model.

## Steps

### 1. Detect available models

Enumerate the model IDs you can pass to a subagent in this session. If you cannot detect any, ask the user to paste the IDs they have access to. Never write a real ID you have not confirmed is available. The alias `inherit` is always valid.

### 2. Load current state

Read the `model:` line from any existing `~/.cursor/agents/jstack-*.md` role files. Treat those values as the current choices. Use `inherit` for missing `jstack-sweep`, `jstack-prose`, and `jstack-judgment` files. Use three `inherit` entries for a missing panel.

### 3. Map and confirm

Show every role with its current model. Ask whether to accept the choices or change specific roles. Offer the detected model IDs plus `inherit`. Prefer AskQuestion over free text. The challenge panel is a comma-separated list. One panel file is written per entry, so the list length sets the fan-out.

The fixed role mapping is:

- `sweep` writes `jstack-sweep`.
- `judgment-and-prose` writes `jstack-prose`.
- `judgment` writes `jstack-judgment`.
- Panel entry `k` writes `jstack-panel-k`.

### 4. Validate

Every real ID written must be in the detected set. `inherit` always passes. If a chosen real ID is not available, stop and ask again.

### 5. Write the role agents

Write each selected role agent under `~/.cursor/agents/`. Set `name` to the agent name, use a one-line description that names its jstack role, and set `model` to the selected ID or `inherit`. Do not set `is_background` or `readonly`.

```
---
name: jstack-sweep
description: Jstack sweep role.
model: inherit
---
# Jstack subagent

You are operating as jstack-mode's full agent style. Read the `jstack-mode` skill's `SKILL.md` in full before doing any work, including its inline Principles index. Navigate to a leaf `principle-*` skill whenever you apply that principle.

If the work is a diff, a test, a PR, or a runtime repro, stop. Say to use `/poteto-mode`. Do not grow a coding path here.
```

Use the same body and matching frontmatter for `jstack-prose`, `jstack-judgment`, and each `jstack-panel-<number>` file. Change only the `name`, the one-line role description, and the selected `model`.

The fresh-run defaults write `jstack-sweep`, `jstack-prose`, `jstack-judgment`, `jstack-panel-1`, `jstack-panel-2`, and `jstack-panel-3`, all with `model: inherit`.

### 6. Handle stale panel files

If the new panel is smaller, propose deleting `jstack-panel-*` files above the new count. Wait for approval before deleting them. Re-runs must not leave old panel files that keep adding members to the fan-out.

### 7. Migrate the old rules file

If `~/.cursor/rules/jstack-models.mdc` exists, say that it no longer drives anything. Offer to delete it and wait for approval. Do not delete it silently.

### 8. Confirm

Tell the user which role agent files were written under `~/.cursor/agents/`, which panel files were proposed for deletion, and whether the old rules file was found.
