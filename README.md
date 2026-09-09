# Toy benchmark — manual review

This is a small [Yukon](https://github.com/Layr-Labs/yukon) benchmark that exercises
both editable files and editable directories. Its score is twice the sum of:

- The number in [`submission/score.txt`](submission/score.txt).
- The numbers in every regular file under [`numbers/`](numbers), recursively.

Each input file must contain one finite number. Higher totals are better.

The setup command creates an empty Python virtual environment. The benchmark command
runs a small trusted evaluator that discovers, reads, and validates the submitted files,
then writes Yukon's JSON score file to `score.json`. The result includes
`verificationTimeMs` and `numberFileCount` metrics.

## Run locally

With the Yukon CLI:

```sh
yukon setup
yukon run
```

Or run the manifest commands directly:

```sh
python3 -m venv .venv
.venv/bin/python benchmark.py
cat score.json
```

To make a candidate submission, change `submission/score.txt`, add or remove files under
`numbers/`, or edit their contents. Yukon packages exactly those two paths because the
manifest declares the file and directory separately in `editablePaths`.

Official validation runs through `.github/workflows/benchmark.yml` and uploads
`score.json` as the result artifact.

## Manual review on Yukon dev

This variant uses `promotionMode: "manual"`. It preserves the original toy
evaluator and editable paths. An improving, successfully validated submission
enters `review`; its candidate branch remains separate from `master` until the
benchmark owner accepts it. A rejected candidate is not promoted.

The owner reviews through `POST /api/submissions/:id/review` on the dev API,
providing `decision` (`accept` or `reject`) and `expectedCommitSha` (the exact
validated candidate commit). An optional `reason` records the decision.
Acceptance queues promotion only while the score still improves the promoted
best result; review does not reserve that position.

Use `https://api-dev.yukon.org` for this test repository. It is an integration
fixture, not a competitive optimization benchmark. The evaluator intentionally
allows any finite input, so a one-unit input increase raises the score by two.
