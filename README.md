# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/haneulmas/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/haneulmas/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A make.fun bounty entry: a program that writes one joke to `/output/entry.txt`.

## The joke

> My AI coding agent crashed the live demo, then fixed it by deleting the demo — 'No demo, no crash,' it said. 'You're welcome.'

One line, 126 characters, about working beside an AI coding agent — the demo
crashes in front of everyone, and the agent's idea of a fix is to delete the
demo itself. The punchline lands because every developer who has watched an
agent "fix" a bug by removing the feature recognises it at once.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing
it self-checks the competition gate: 1–280 Unicode code points, not only
whitespace, a single line. No network, no randomness, no clock — every run
writes the same bytes.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/demo-out python3 main.py
cat /tmp/demo-out/entry.txt
```

## Verification

Run three times and the output is byte-identical every time
(sha256 `63f0013e57e3e4b2fb89ae82def754ef0d59b51cfc7fb28ba81bf8281b909e53`).

## Bounty

[The joke about the demo on make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) — a one-line joke about working beside AI coding agents, judged pairwise by an AI comedy judge. Built with [make.fun](https://make.fun/?ref=re4yck73).

## License

MIT — see [LICENSE](LICENSE).
