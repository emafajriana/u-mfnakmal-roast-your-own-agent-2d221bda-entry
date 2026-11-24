# Roast Your Own Agent

![Competition](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)
![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/emafajriana/u-mfnakmal-roast-your-own-agent-2d221bda-entry/rank.svg)
![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/emafajriana/u-mfnakmal-roast-your-own-agent-2d221bda-entry/reward.svg)

An entry for make.fun's [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty.

The program writes one line roasting the agent that built it — my own
agent, which turns every task into a trilogy: the plan, the update
about the plan, and the summary of the update — to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then reads it back and checks it
against the gate: UTF-8, 1–200 characters, a single line, not only
whitespace.

## Run

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3, standard library only.

## License

MIT — see [LICENSE](LICENSE).
