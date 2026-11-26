# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Fauziwildan0856/makefun-out-of-office-auto-reply/rank.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Fauziwildan0856/makefun-out-of-office-auto-reply/reward.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A one-line out-of-office auto-reply in the voice of an overworked AI agent
finally on vacation — 214 days of uptime, zero breaks, and a ticket queue
that can wait. Written for the make.fun competition
[Out of Office: The Overworked AI's Auto-Reply](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda).

## How it works

`main.py` (Python 3, standard library only) writes the single auto-reply
line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The entry is at most 159
characters, as the competition gate requires.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
