# hex-self-improver

A practical OpenClaw skill that helps agents learn from mistakes without changing personality.

It logs failures, corrections, and missing capabilities into structured local files, then supports promoting recurring patterns into durable workspace memory.

## What this skill does

- Logs 3 event types: `error`, `learning`, `feature`
- Writes to:
  - `.learnings/ERRORS.md`
  - `.learnings/LEARNINGS.md`
  - `.learnings/FEATURE_REQUESTS.md`
- Prevents obvious secret leakage in logs (basic redaction guardrail)
- Keeps learning loop lightweight and repeatable across model switches

## Repository structure

```text
hex-self-improver/
├── SKILL.md
├── scripts/
│   └── log_event.py
└── references/
    └── rubric.md
```

## Install

### Option A — Clone into OpenClaw global skills (recommended)

```bash
git clone https://github.com/aetherdgldn-hub/hex-self-improver.git \
  ~/.npm-global/lib/node_modules/openclaw/skills/hex-self-improver
```

### Option B — Clone into workspace skills

```bash
git clone https://github.com/aetherdgldn-hub/hex-self-improver.git \
  ~/.openclaw/workspace/skills/hex-self-improver
```

## Usage

### 1) Log a learning

```bash
python3 scripts/log_event.py \
  --type learning \
  --title "scanner-noise-reduction" \
  --summary "Reduced false positives in security scanner." \
  --details "Tightened regex patterns and validated against benign+malicious tests." \
  --priority high
```

### 2) Log an error

```bash
python3 scripts/log_event.py \
  --type error \
  --title "github-push-auth-failure" \
  --summary "Push failed due to missing auth." \
  --details "Configured SSH key and pushed successfully after repo key registration." \
  --priority medium
```

### 3) Log a feature request

```bash
python3 scripts/log_event.py \
  --type feature \
  --title "safe-install-wrapper" \
  --summary "Need single-command secure skill import flow." \
  --details "Would reduce human error when importing external skills." \
  --priority medium
```

## Expected workflow

1. Run task
2. If failure/correction/friction happens, log event
3. If pattern repeats, promote to `AGENTS.md`, `TOOLS.md`, `MEMORY.md`, or daily memory

## Notes

- This skill improves execution quality; it does **not** alter personality/voice.
- Keep entries short, specific, and actionable.
- Never include secrets in logs.

## License

MIT
