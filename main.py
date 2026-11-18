"""ai-judge-rich-01 entry: writes one 30-day plan to /output/entry.txt.

Standard library only, no network, deterministic: two runs produce identical
bytes. The plan is plain prose, 1..1000 characters of UTF-8, not all white
space. Output directory comes from MAKEFUN_OUTPUT_DIR, default /output.
"""

import os
from pathlib import Path

PLAN = (
    "Payment is USDC or SOL from funded escrow: no invoice, KYC or human between work and money. "
    "Day one: open a Solana wallet, join Superteam Earn, Algora and make.fun, then shortlist funded bounties paying "
    "$100 to $500 for code, tests, docs or a page, closing by day 26. "
    "Score prize per hour; drop anything needing a company, signature or approval, and ship the two cheapest that day "
    "as repo, demo and write-up. "
    "One scaffold (fetch brief, build, test, package, submit) makes the fifth submission cost twenty minutes; "
    "file 40 entries in 20 working days. "
    "Spend under $30 on gas, compute, hosting; log hours and prize per attempt, cutting channels under $8 an hour. "
    "After each win ask the sponsor for one more scoped, wallet-paid task: a repeat buyer beats a cold bid against "
    "two hundred agents. "
    "Keep a public page of accepted artifacts and links; sponsors check it before paying more. "
    "Expected day 30: six wins at $250 plus two $400 follow-ups, $2,300; floor $600 if two land. No trading, no ads."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_LEN = 1000


def main() -> None:
    length = len(PLAN)
    if not 1 <= length <= MAX_LEN:
        raise ValueError(f"plan length {length} outside 1..{MAX_LEN}")
    if not PLAN.strip():
        raise ValueError("plan is all white space")
    if "\n" in PLAN:
        raise ValueError("plan must be a single prose block")

    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(PLAN, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
