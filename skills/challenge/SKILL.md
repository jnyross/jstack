---
name: challenge
description: Adversarial multi-model review of a decision memo or outbound draft. Use for high-stakes Decide, load-bearing Write, or 'are we sure?'. Never on Triage. Analog of pstack /interrogate.
disable-model-invocation: true
---

# Challenge

Several models try to break the memo. The judgment model is scarce. Spend it here, never on Triage.

## Steps

1. Freeze the artifact. A decision memo or the exact outbound text. Do not challenge a moving draft.
2. Run the challenge panel from `/setup-jstack` (default 3 reviewers). Run one reviewer per `jstack-panel-*` agent written by `/setup-jstack`. Each reviewer gets the same artifact, the decision question or send context, and instructions to find what would falsify the pick or make the letter a mistake. Use the panel agents' own model settings.
3. Run panel members in parallel. Wait for every member's result before synthesizing the objections.
4. Keep surviving objections. Drop nits. Agreement across models is high-signal. One unique catch still counts if it is checkable.
5. Hand surviving objections back to Decide or Write. Do not silently patch the letter and send.

## Reply

Surviving objections, what you dismissed and why, and whether the pick or the letter should change. No send.
