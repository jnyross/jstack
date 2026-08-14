### Decide

**You own the choice. Capture what was rejected too.**

Two real options remain. A one-way door. Taste or risk, not a lookup. Done is a Johnopedia decision page. What was picked, what was rejected, the evidence, the review date.

1. State the decision question and what would falsify each option.
2. Gather evidence with Research or Brief. Do not decide from chat vibes. Cite live vs memory.
3. For high stakes, run **challenge** (multi-model) on the memo. Use `subagent_type: "jstack-judgment"` for the decision and `subagent_type: "jstack-panel-<number>"` for each panel member. If `/setup-jstack` has never run, use `subagent_type: "jstack-agent"` for all of them. The judgment role is scarce. Use it here, never on Triage.
4. Write the decision to Johnopedia with `put_page`. Include rejected options on the same page. `get_page` after write. Present irreversible next steps and wait for approval before send, book, or pay.

A lookup ("what time is the flight") is not Decide. Route it to Brief or Research.

**Reply:** the decision question, the pick, what was rejected and why, the slug, the review date, and any paused irreversible step with the exact action waiting on approval.
