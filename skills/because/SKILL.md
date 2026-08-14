---
name: because
description: Cited research across GBrain, mail, calendar, and the web. Use for 'why did we decide this', 'what's the history', Research playbook sweeps, or any question whose answer is scattered.
disable-model-invocation: true
---

# Because

Coverage over a pretty story. Analog of pstack `/why`. Sources are GBrain, Gmail, Calendar, and the web. Null results are findings.

## Steps

1. Name the question and the sources that could hold an answer. Do not pick a story first.
2. Sweep in parallel. One slice per source. Johnopedia `query` / `search` / `get_page`. Gmail `search_threads`. Calendar `search_events`. Browser if the web could hold it. Context7 only for a library API. Skip an unavailable MCP and say so.
3. Convert private facts to generic criteria before any web search.
4. Synthesize with gaps named. Two sources in conflict stay in conflict. Confidence matches the evidence.

## Reply

Question, sources swept including nulls, cited answer, disagreements, confidence. Every claim has a slug, gmail id, event id, or URL, or is labeled inference.
