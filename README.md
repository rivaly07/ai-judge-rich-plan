# ai-judge-rich-plan

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/rivaly07/ai-judge-rich-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/rivaly07/ai-judge-rich-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

A 991-character plan for a software agent that starts with $100 and 30 days and ends holding
the most money it can. It sells nothing that needs an invoice: it takes funded, small-ticket
bounties — code, tests, docs, a page — on Superteam Earn, Algora and make.fun, where the prize
sits in escrow and pays USDC or SOL to a wallet, so no KYC, legal entity or human signature can
stall the payout. Day one is a wallet, three registrations and two cheapest tasks shipped; the
rest is one reusable scaffold that makes submission forty as cheap as submission five, a $30 cap
on gas and compute, a prize-per-hour filter, one repeat task requested from every sponsor that
paid, and a public page of accepted artifacts that wins the next, larger bounty. Expected day 30
is about $2,300 with a $600 floor if only two wins land.

## Run it

```sh
python3 main.py                 # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Standard library only, no network. Two runs produce byte-identical output; the plan is checked
to be 1..1000 characters of UTF-8 and not only white space before it is written.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
