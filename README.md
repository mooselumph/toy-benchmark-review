# Toy benchmark — independent manual-review tracks

This Yukon dev fixture has two independent tracks, `alpha` and `beta`, on the same
`master` branch. Both use `promotionMode: "manual"`. This fixture tests Yukon
PR #721: reviewed submissions use the existing promotion logic when a sibling
track advances the target branch. No independence manifest flag is required.

Each track scores twice the sum of its `submission/score.txt` and every regular
file under its own `numbers/` directory. Inputs must be finite numbers. Higher
scores are better. The original baselines were 26 for alpha and 46 for beta;
promoted test submissions increase those values. The evaluator reports
`verificationTimeMs` and `numberFileCount`; these are arithmetic test lanes, not
real optimization tasks.

## Run locally

```sh
python3 -m venv .venv
.venv/bin/python benchmark.py --track alpha
.venv/bin/python benchmark.py --track beta
```

With Yukon configured for `https://api-dev.yukon.org`:

```sh
yukon clone mooselumph/toy-number-review-tracks
yukon setup --track alpha
yukon run --track alpha
yukon run --track beta
```

Edit only the selected track's declared paths under `tracks/alpha/` or
`tracks/beta/`, then submit with `--track`, a public note, and model/harness
attribution. Each track has a separate workflow and result file. The workflows
run only on `workflow_dispatch`, so promotion itself does not run the evaluator.

## Cross-track promotion test

1. Prepare improving alpha and beta candidates against the same `master` commit.
2. Submit both and wait until both are in `review`.
3. Record their exact candidate commits, scores, and workflow run IDs.
4. Accept alpha and wait until it is promoted.
5. Accept beta using its original reviewed SHA. Beta must publish on the new tip,
   preserve alpha's winning files, retain its original score and reviewer history,
   and create no new validation run.

The API checks score eligibility independently for each track. PR #721 reuses
automatic promotion: it copies the selected candidate paths onto the new target
and updates the candidate branch. The review audit retains the original SHA.
Intervening merged PRs labeled `yukon-unsafe` block GitHub Actions promotion;
there is no automatic independence check or new failed-promotion retry API.
These workflows are dispatch-only, so the branch update does not start another
evaluation. Repositories with PR-triggered evaluation may start an additional
run before Yukon can cancel it.

The old root-level inputs, default evaluator invocation, and `benchmark.yml`
remain for historical fixture compatibility. The former standalone dev benchmark
retains its history; the schema-v2 challenge is imported under the new name above.
