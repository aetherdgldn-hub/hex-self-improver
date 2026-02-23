# Usage Guide

## Command

```bash
python3 scripts/log_event.py --type <learning|error|feature> --title "..." --summary "..." --details "..." [--priority low|medium|high|critical]
```

## Parameters

- `--type` (required): `learning`, `error`, or `feature`
- `--title` (required): short identifier
- `--summary` (required): one-line impact
- `--details` (required): what happened + what should happen next
- `--priority` (optional): default `medium`

## Output files

- learning -> `.learnings/LEARNINGS.md`
- error -> `.learnings/ERRORS.md`
- feature -> `.learnings/FEATURE_REQUESTS.md`

## Good entry style

- concise
- reproducible
- points to fix/action

## Avoid

- giant dumps
- vague entries ("something broke")
- secrets (keys, tokens, passwords)

## Promotion pattern

When an issue repeats or matters strategically, promote:
- workflow rule -> `AGENTS.md`
- tool gotcha -> `TOOLS.md`
- durable memory -> `MEMORY.md`
- day context -> `memory/daily/YYYY-MM-DD.md`
