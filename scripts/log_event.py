#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/hex/.openclaw/workspace')
LEARN_DIR = ROOT / '.learnings'
FILES = {
    'learning': LEARN_DIR / 'LEARNINGS.md',
    'error': LEARN_DIR / 'ERRORS.md',
    'feature': LEARN_DIR / 'FEATURE_REQUESTS.md',
}

PREFIX = {
    'learning': 'LRN',
    'error': 'ERR',
    'feature': 'FEAT',
}

def ensure_files():
    LEARN_DIR.mkdir(parents=True, exist_ok=True)
    for kind, path in FILES.items():
        if not path.exists():
            path.write_text(f'# {path.stem}\n\n', encoding='utf-8')

def next_id(kind: str) -> str:
    now = datetime.now(timezone.utc)
    date = now.strftime('%Y%m%d')
    path = FILES[kind]
    text = path.read_text(encoding='utf-8', errors='ignore') if path.exists() else ''
    count = text.count(f'[{PREFIX[kind]}-{date}-') + 1
    return f"{PREFIX[kind]}-{date}-{count:03d}"

def append_entry(kind: str, title: str, summary: str, details: str, priority: str):
    entry_id = next_id(kind)
    ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    path = FILES[kind]
    block = f"""## [{entry_id}] {title}

**Logged**: {ts}
**Priority**: {priority}
**Status**: pending

### Summary
{summary}

### Details
{details}

---

"""
    with path.open('a', encoding='utf-8') as f:
        f.write(block)
    print(f'{kind.upper()} logged -> {path} ({entry_id})')


def main():
    parser = argparse.ArgumentParser(description='Log self-improvement event')
    parser.add_argument('--type', choices=['learning', 'error', 'feature'], required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--summary', required=True)
    parser.add_argument('--details', required=True)
    parser.add_argument('--priority', choices=['low', 'medium', 'high', 'critical'], default='medium')
    args = parser.parse_args()

    # basic secret guardrail
    banned = ['api_key', 'token=', 'authorization:', 'private key', 'BEGIN RSA PRIVATE KEY']
    joined = f"{args.title}\n{args.summary}\n{args.details}".lower()
    if any(b.lower() in joined for b in banned):
        raise SystemExit('Refusing to log potential secret content. Redact and retry.')

    ensure_files()
    append_entry(args.type, args.title, args.summary, args.details, args.priority)

if __name__ == '__main__':
    main()
