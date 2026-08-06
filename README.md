# Toy benchmark

This is the smallest useful [Yukon](https://github.com/Layr-Labs/yukon)
benchmark: its score is the number in [`submission/score.txt`](submission/score.txt).
Higher numbers are better.

The setup command creates an empty Python virtual environment. The benchmark command
runs a small trusted evaluator that reads the submitted number and writes Yukon's JSON
score file to `score.json`. The result also includes a `verificationTimeMs`
metric covering the time spent reading and validating the submission.

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

To make a candidate submission, change `submission/score.txt`. Yukon packages only the
`submission` directory because it is the sole entry in `editablePaths`.

Official validation runs through `.github/workflows/benchmark.yml` and uploads
`score.json` as the result artifact.
