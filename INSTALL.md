# Installation Guide

## Prerequisites

- OpenClaw installed
- Python 3 available in PATH

## Global install (all sessions)

```bash
mkdir -p ~/.npm-global/lib/node_modules/openclaw/skills
git clone https://github.com/aetherdgldn-hub/hex-self-improver.git \
  ~/.npm-global/lib/node_modules/openclaw/skills/hex-self-improver
```

## Workspace install (project-specific)

```bash
mkdir -p ~/.openclaw/workspace/skills
git clone https://github.com/aetherdgldn-hub/hex-self-improver.git \
  ~/.openclaw/workspace/skills/hex-self-improver
```

## Verify install

```bash
ls -la ~/.npm-global/lib/node_modules/openclaw/skills/hex-self-improver
# or
ls -la ~/.openclaw/workspace/skills/hex-self-improver
```

You should see:
- `SKILL.md`
- `scripts/log_event.py`
- `references/rubric.md`

## Quick test

```bash
cd ~/.npm-global/lib/node_modules/openclaw/skills/hex-self-improver
python3 scripts/log_event.py \
  --type learning \
  --title "install-test" \
  --summary "Skill installed and logger executed." \
  --details "Generated first test learning entry." \
  --priority low
```
