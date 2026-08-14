# jstack

A Cursor plugin that closes knowledge-work loops against live Gmail, Calendar, and compiled Johnopedia pages.

pstack helps you write less code, at higher quality. jstack helps you keep fewer open threads, with sources you can re-check. The unit of work is a thread that ends.

If the work is a diff, a test, a PR, or a runtime repro, use `/poteto-mode`. jstack does not grow a coding path.

## Enable

Two steps. Open the folder so the skills load in this workspace. Then install it as a local plugin so `/jstack-mode` is available in other chats.

### 1. Open the folder

**File > Open Folder** on `/path/to/jstack`.

Project skills live at `.cursor/skills/` (a symlink to `skills/`). Opening this folder is enough to type `/jstack-mode` in a chat in this workspace. That is the create-skill project-skill path.

### 2. Install as a local Cursor plugin

This is a Cursor Plugin (`.cursor-plugin/plugin.json`), not a marketplace listing. From [Cursor's plugin docs](https://cursor.com/docs/plugins.md#test-plugins-locally):

```bash
mkdir -p ~/.cursor/plugins/local
ln -s /path/to/jstack ~/.cursor/plugins/local/jstack
```

The manifest must resolve at `~/.cursor/plugins/local/jstack/.cursor-plugin/plugin.json`. Nested extra folders will not load.

Then:

1. Confirm Gmail, Google Calendar, and Johnopedia MCPs are connected. Linear, GitHub, and a browser are optional.
2. In Cursor Settings, turn on **Include third-party Plugins, Skills, and other configs** if that toggle exists.
3. Command Palette: **Developer: Reload Window**.
4. Check Customize / Settings → Plugins for **jstack**. Type `/jstack-mode` in chat. It should appear as a skill.

Optional: `/setup-jstack` writes role agent files under `~/.cursor/agents/`. Until you run it, every role uses the shipped `jstack-agent` and inherits the parent chat model.

## Requirements

- Johnopedia: `user-Johnopedia`
- Gmail: `plugin-gmail-gmail`
- Google Calendar: `plugin-google-calendar-google-calendar`

This plugin does not install or declare these MCP servers. The IDs are install-specific, so a differently named server will not be found. If a server is missing, jstack skips that source and says so.

## First command

```
/jstack-mode triage my inbox and kill anything live sources show is done
```

That should match Triage, pull Gmail and Calendar first, tag Archive / Action / Skip, and run a stale pass against compiled open loops.

A stale-only pass:

```
/jstack-stale
```

If that pass cannot shrink the open list, the rest of the plugin is decoration. Say so and stop adding capture.

## `/jstack-mode`

Sticky router, same idea as `/poteto-mode`. It classifies the request, opens the matching playbook, and copies the steps in verbatim. Opt out by saying so. Casual chat stays out.

Seven playbooks. No eighth miscellaneous. Unmatched work is either coding (pstack) or a one-off under Close or Research.

| Playbook | When | Done artifact |
|---|---|---|
| [Triage](./skills/jstack-mode/playbooks/triage.md) | Inbox or calendar has piled up | Docket tagged Archive / Action / Skip. Stale compiled items killed. |
| [Brief](./skills/jstack-mode/playbooks/brief.md) | Catch me up. Prep me for a meeting. | Five bullets, tagged threads, one next move. |
| [Research](./skills/jstack-mode/playbooks/research.md) | Answer is scattered across memory, mail, web | Cited brief. Nulls listed. Memory vs live labeled. |
| [Decide](./skills/jstack-mode/playbooks/decide.md) | Two real options. A one-way door. | Johnopedia page. Rejected options stay on the page. |
| [Write](./skills/jstack-mode/playbooks/write.md) | Mail or a note a human will read | Exact outbound text shown. Send only after approval. |
| [Capture](./skills/jstack-mode/playbooks/capture.md) | A fact that will be asked again | A slug. `get_page` after `put_page`. |
| [Close](./skills/jstack-mode/playbooks/close.md) | One named loop should end | Live artifact changed, compiled truth updated in the same turn. |

Archive / Action / Skip is the inbox rule. Archive files it. Action is a real next move. Skip is noise. Do not invent a fourth bucket.

## Other slash skills

`/jstack-mode` fires these when a step needs them. You can call them directly.

| Skill | When |
|---|---|
| [`/jstack-mode`](./skills/jstack-mode/SKILL.md) | Default entry. Any loop that needs rigor. |
| [`/jstack-stale`](./skills/jstack-stale/SKILL.md) | Compare compiled open loops to live mail and calendar. Propose kills. |
| [`/setup-jstack`](./skills/setup-jstack/SKILL.md) | Write role agent files for sweep, judgment, and challenge-panel models. |
| [`/live`](./skills/live/SKILL.md) | A fact might have changed since ingest. |
| [`/state`](./skills/state/SKILL.md) | Catch-up or meeting prep. |
| [`/because`](./skills/because/SKILL.md) | Why did we decide this. Scattered history. |
| [`/drafts`](./skills/drafts/SKILL.md) | N variants of a letter or memo, then pick a base. |
| [`/challenge`](./skills/challenge/SKILL.md) | Adversarial review of a decision or outbound draft. Never on Triage. |
| [`/compile`](./skills/compile/SKILL.md) | Session leftovers that earned a page. |
| [`/unslop`](./skills/unslop/SKILL.md) | Every reply and every outbound draft. |

Principles are in [PRINCIPLES.md](./PRINCIPLES.md). The mode cites a leaf when it changes a decision. Wallpaper quotes do not count.

## Wiring

Named tools, not invented APIs.

- **Johnopedia** (`user-Johnopedia`). `query`, `search`, `get_page`, `list_pages`, `put_page`, `get_recent_salience`, `recall`, `get_timeline`. Compiled truth.
- **Gmail** (`plugin-gmail-gmail`). `search_threads`, `get_thread`, `get_message`, `create_draft`, `update_draft`, `list_drafts`, `label_thread`. `send_message` waits.
- **Google Calendar** (`plugin-google-calendar-google-calendar`). `list_calendars`, `list_events`, `search_events`, `get_event`. Event writes that change a real invite wait.
- **Linear** (`plugin-linear-linear`). Work tickets in Brief or Close. Skip for household admin.
- **GitHub** (`plugin-github-github`). Reading an issue as evidence. Shipping stays in pstack.
- **Browser.** In-app Browser, or `access-websites` / `browser-use`, when a live page is the artifact.

Send, book, pay, and sharing private facts always pause. Drafts and reversible page edits proceed.

## PoC limits

This is a skill pack. It is not a product yet.

- No overnight daemon. `/jstack-stale` is a skill you run. There is no morning-docket scheduler and no hook that fires on its own.
- No send, book, or pay without a yes in the chat. "Going to bed" does not override that.
- No coding playbooks. Hard stop to `/poteto-mode`.
- No character bots. Domain knowledge lives on Johnopedia pages, not in named personas.
- Seven playbooks, not twenty-two. Quality over coverage.
- Model setup defaults to `inherit` in role agent files under `~/.cursor/agents/`. Cheap sweep vs expensive judgment only happens after `/setup-jstack`.
- WhatsApp is not bundled. Use the existing WhatsApp skill if the thread lives there.
- If Gmail, Calendar, or Johnopedia is disconnected, the matching playbook says the source was skipped. It will not invent live state.
- Automations like pstack's benny are out of scope. If the stale pass cannot shrink the open list against live mail and calendar, do not add more surface.
