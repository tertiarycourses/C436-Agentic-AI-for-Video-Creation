from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
REQUIRED = ['README.md', 'AI-PROMPTS.md', 'evidence/checklist.md', 'data/agent-contracts.yaml', 'data/handoff-schema.json', 'starter/orchestrator-prompt.md', 'verify.py']
missing = [p for p in REQUIRED if not (ROOT / p).exists()]
text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*") if p.is_file() and p.name != "verify.py" and p.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".csv", ".txt", ".py"})
patterns = [r"sk-[A-Za-z0-9]{16,}", r"AIza[A-Za-z0-9_-]{20,}", r"ya29\.[A-Za-z0-9_-]+", r"BEGIN (?:RSA |EC )?PRIVATE KEY"]
secrets = [pat for pat in patterns if re.search(pat, text)]
legacy = [term for term in ["workflow.json", "SocialPost"] if term.lower() in text.lower()]
if missing or secrets or legacy:
    print("FAIL", {"missing": missing, "secret_patterns": secrets, "legacy_terms": legacy})
    sys.exit(1)
print("PASS Lab 06: required artifacts, secret scan and Hermes-only boundary")
