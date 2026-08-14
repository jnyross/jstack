---
name: setup-jstack
description: Configure which models jstack uses per role. Detects available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-jstack, "configure jstack models", or changing sweep vs judgment vs challenge panel.
---

# Setup jstack

Write `~/.cursor/rules/jstack-models.mdc`, an always-applied rule that sets jstack's model per role. The skills read it and fall back to their inline defaults when a line is absent.

## Steps

### 1. Detect available models

Enumerate the model slugs you can pass to a `Task` subagent in this session. If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid.

### 2. Load current state

If `~/.cursor/rules/jstack-models.mdc` already exists, read it and treat its values as the current choices. Otherwise start from the defaults in step 5.

### 3. Map and confirm

Show every role with its current model. Ask whether to accept as-is or change specific roles. Offer the detected models plus `inherit-parent` and `auto`. Prefer AskQuestion over free text. The `challenge panel` value is a list. One subagent runs per entry, so the list length sets the count.

### 4. Validate

Every real slug written must be in the detected set. `inherit-parent` and `auto` always pass. If a chosen real slug is not available, stop and ask again.

### 5. Write the rule

Write `~/.cursor/rules/jstack-models.mdc` with `alwaysApply: true` and one line per role. Overwrite the whole file so re-runs stay idempotent. Shape:

```
---
description: jstack per-role model choices (overrides skill defaults)
alwaysApply: true
---
# jstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`).
sweep: inherit-parent
brief: inherit-parent
judgment and prose: inherit-parent
hardest judgment: inherit-parent
challenge panel: inherit-parent
stale pass: inherit-parent
```

PoC default is `inherit-parent` on every role so the plugin runs on whatever model is already in the chat. Replace `sweep` and `stale pass` with a fast model when you want cheap inbox fan-out. Replace `hardest judgment` and `challenge panel` with a scarce judgment model when Decide is worth it.

### 6. Confirm

Tell the user the rule was written and that it applies to new sessions. Re-running this skill updates it.
