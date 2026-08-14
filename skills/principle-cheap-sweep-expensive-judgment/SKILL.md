---
name: principle-cheap-sweep-expensive-judgment
description: "Apply when choosing a model for fan-out across inbox slices or source categories, vs a contested decision. Triage and source sweeps use a fast model. Decide and Challenge may spend a judgment model. Cost sensitivity is an operating rule, not a vibe."
disable-model-invocation: true
---

# Cheap sweep, expensive judgment

Triage and source sweeps are cheap. Decide and Challenge are expensive. Do not invert that.

**Why:** Inbox classification does not earn a scarce judgment model. A one-way door might. Spending the judgment model on Triage trains the plugin to be decoration.

**Pattern:** Fan-out Gmail slices, calendar windows, and GBrain searches with `subagent_type: "jstack-sweep"`. Briefs, Write, and Capture use `subagent_type: "jstack-prose"`. Decide uses `subagent_type: "jstack-judgment"`. Challenge may run `subagent_type: "jstack-panel-<number>"` members. If `/setup-jstack` has never run, use `subagent_type: "jstack-agent"` for each role. Never run Challenge on Triage.

**Does not change:** The playbook steps. A cheap model still copies them verbatim.
