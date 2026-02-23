---
name: hex-self-improver
description: Capture mistakes, corrections, and reusable wins into structured local logs, then promote durable patterns into workspace memory files. Use when a task fails, user corrects output, a better method is discovered, or repeated friction appears in workflow.
---

# Hex Self Improver

Run a tight post-task learning loop.

## Core Workflow

1. Detect trigger:
   - command/tool failure
   - user correction
   - repeated friction
   - improved method discovered
2. Append one concise entry via script:
   - `python3 skills/hex-self-improver/scripts/log_event.py --type error|learning|feature --title "..." --summary "..." --details "..."`
3. If recurring/high-value, promote:
   - workflow pattern -> `AGENTS.md`
   - tool gotcha -> `TOOLS.md`
   - long-term strategic memory -> `MEMORY.md`
   - day-specific context -> `memory/daily/YYYY-MM-DD.md`
4. Keep entries short and actionable.

## Rules

- Never log secrets, tokens, passwords, private keys.
- Prefer one strong learning over noisy dumps.
- If same issue repeats, update prior pattern and increment recurrence.

## Files

- `.learnings/LEARNINGS.md`
- `.learnings/ERRORS.md`
- `.learnings/FEATURE_REQUESTS.md`
- `references/rubric.md`
- `scripts/log_event.py`
