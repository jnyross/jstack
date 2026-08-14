### Write

**You own the outbound text. Prose is the product.**

An email, memo, note, or reply that will be read by a human. Done is a draft in Gmail or in chat. Send only when asked, after the exact text is shown.

1. Read the thread and any GBrain voice or relationship context. `get_thread` / `get_message` for mail. `query` / `get_page` for voice. Do not invent tone.
2. Draft under **unslop**. Short sentences. No chatbot padding. If this is mail, `create_draft` or `update_draft` is reversible and should proceed.
3. If the wording is load-bearing, run **drafts** (N variants, pick a base, graft). Same shape as pstack arena, different object.
4. Show the exact outbound text. Do not `send_message` or sending `reply` until approved. **principle-ask-before-the-world-changes**.

After a send is approved and the live message exists, hand to Close so compiled truth updates in the same turn.

**Reply:** the exact outbound text, who it is to, which facts were memory vs live, and a one-line wait for send approval. No paraphrase of the draft. The draft is the artifact.
