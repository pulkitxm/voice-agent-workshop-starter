# Voice AI Agent Workshop Starter

> A working LiveKit voice agent on **Groq + Smallest.ai + Noveum** — pre-wired with tracing, ready to be reshaped into your own product with **Cursor** in 3 hours.

This is the starter repo for the **Vibe-Code a Voice AI Agent** workshop at Frontier Tower (Thu May 14, 2026, 4:30–7:30 PM PT). 🍕🍻 Pizza and drinks on us.

---

## Setup — complete these 6 steps first

Work through these at the start of the workshop. Step 1 (signups) may need a few minutes — start there while the intro is running.

### Step 1 — Sign up for 4 services (all free tier)

| Service | URL | What you need |
|---------|-----|---------------|
| [LiveKit Cloud](https://cloud.livekit.io) | cloud.livekit.io | Project URL + API Key + Secret → Settings → Keys |
| [Groq](https://console.groq.com) | console.groq.com | API Key |
| [Smallest.ai](https://console.smallest.ai/apikeys) | console.smallest.ai | API Key → API Keys (covers STT + TTS) |
| [Noveum](https://noveum.ai) | noveum.ai | API Key → Settings → API Keys |

### Step 2 — Clone, install, and fill in your keys

```bash
git clone <this-repo-url> voice-agent-workshop-starter
cd voice-agent-workshop-starter

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# open .env — paste in all 4 keys (comments in the file say exactly where each one lives)
```

### Step 3 — Connect the Noveum MCP and restart

Do this **before** running verify — the MCP must be connected before you start using Cursor for workshop prompts, and adding it requires a restart.

**Claude Code CLI:**
```bash
claude mcp add --transport http noveum https://noveum.ai/api/mcp \
  --header "Authorization: Bearer YOUR_NOVEUM_API_KEY"
```
Then restart your `claude` session.

**Cursor:**

Open **Cursor Settings → MCP → Add new MCP server** and paste:

```json
{
  "mcpServers": {
    "noveum": {
      "url": "https://noveum.ai/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_NOVEUM_API_KEY"
      }
    }
  }
}
```

Save, then click the **reload** button next to the server (or fully restart Cursor). Confirm the green connected status.

### Step 4 — Verify all keys work

```bash
python verify_setup.py
```

All checks must be green. If anything is red, fix it now.

### Step 5 — Smoke test: run the starter agent and make a call

```bash
python build_knowledge.py
python agent.py dev
```

You should see `registered worker {agent_name: workshop-starter-agent, ...}`.

Open the **LiveKit Cloud console** → Agents → configure the session → set **Agent name** to `workshop-starter-agent` → **Save and start session**. Talk to it. If it responds, you're good.

> You can also use [agents-playground.livekit.io](https://agents-playground.livekit.io) — paste `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET` from your `.env`.

### Step 6 — Install the LiveKit CLI and authenticate

```bash
brew install livekit-cli
lk cloud auth        # one-time browser OAuth
```

---

## Workshop

Once all 6 setup steps are green, open **[WORKSHOP.md](WORKSHOP.md)** for the stage-by-stage runbook.
Use **[PROMPT_CHEATSHEET.md](PROMPT_CHEATSHEET.md)** for the 7 prompts — copy each one and paste it into Cursor or `claude` as-is (only PROMPT 2 has a bracket to fill in).

---

## Stack

```
Caller ─► LiveKit ─► Smallest.ai Pulse (STT) ─► Groq gpt-oss-120b (LLM) ─► Smallest.ai Lightning (TTS) ─► Caller
                                                        │
                                                        └─► Noveum (traces, NovaSynth, NovaPilot)
```

---

## License

MIT — fork it, ship it, sell it.
