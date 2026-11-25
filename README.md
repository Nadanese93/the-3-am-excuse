# The 3 AM Excuse

[![The 3 AM Excuse bounty](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Nadanese93/the-3-am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Nadanese93/the-3-am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

A [make.fun](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) bounty entry ($2 prize): one line in the voice of a hardware wallet refusing to sign a transaction at 3 AM.

## The entry

> 3 AM? You're not on the guest list — the door opens at 9, and I'm the bouncer. No signature, no plus-one.

The wallet is the bouncer, the user is not on the guest list, and the door opens at 9 — personality, reason, and joke in one breath, 105 characters.

## How it runs

`main.py` writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), validates the 1–200 character gate with a specific error per failure, writes atomically (temp file + `os.replace`), chmods the output 0644, and verifies the file on disk by reading it back byte-for-byte.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
