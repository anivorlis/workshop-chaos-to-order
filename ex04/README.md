# DVC Pipeline

The starting point is the solution from ex03: a pipeline reading parameters from `config.toml`.  
The goal is to replace `pipeline.py` with a DVC DAG so that stages re-run only when their inputs change, and experiments are tracked automatically.

### Success criteria: Run the pipeline with DVC and compare metrics across two experiments

---

## Steps

### 0. Install DVC

Add DVC as a dev dependency (pinned in `uv.lock`, like numpy/matplotlib), then call it with `uv run dvc ...`:

```bash
uv add --dev dvc
```

*Hint: prefer `uv add --dev dvc` over `uv tool install dvc` — the latter installs it globally and isn't captured by the lockfile.*

### 1. Initialise DVC

```bash
uv run dvc init
git add .dvc .dvcignore
git commit -m "initialise dvc"
```

### 2. Map the pipeline

Sketch how data flows before writing any YAML:

```
generate_data ─> data/input.csv ─> fit ─> data/coefficients.json ─┬─> evaluate ─> data/metrics.json
                                                                  └─> visualize ─> data/plot.png
```

### 3. Write `dvc.yaml` (at the project root)

Declare the four stages. For each stage, ask yourself:

- **cmd** — how do I run it? (e.g. `uv run -m ex04.generate_data`)
- **deps** — what files does it read? (its own `.py` + any outputs of earlier stages)
- **outs / metrics** — what files does it produce?
- **params** — which keys in `ex04/config.toml` does it use?

Hints:
- List config values under `params:`, *not* `deps:` — DVC re-runs a stage only when a listed param changes.
- Chain stages by adding the previous stage's output to the next stage's `deps` (e.g. `fit` depends on `data/input.csv`).
- For `evaluate`, use `metrics:` instead of `outs:` with `cache: false`, so the metrics file is comparable and stays in git.
- For `visualize`, the plot is a plain `out`.

<details>
<summary>Stage skeleton (fill in the blanks)</summary>

```yaml
stages:
  generate_data:
    cmd: uv run -m ex04.generate_data
    deps:
      - ex04/generate_data.py
    params:
      - ex04/config.toml:
          - generate_data.<param>
    outs:
      - data/input.csv
  # fit, evaluate, visualize ...
```
</details>

### 4. Run the pipeline as an experiment

```bash
uv run dvc exp run
```

DVC runs the stages in dependency order and records the run (params + metrics) as an experiment. See the graph with `uv run dvc dag`.

### 5. Inspect the metrics

```bash
uv run dvc metrics show
```

### 6. Run a second experiment

Change `degree` in `ex04/config.toml`, then run again:

```bash
uv run dvc exp run
```

Only the stages affected by `fit.degree` re-run (`fit`, `evaluate`, `visualize`); `generate_data` stays cached.

### 7. Compare experiments

```bash
uv run dvc exp show
```

A table of every experiment with its params and metrics — see how `degree` moved MSE / RMSE / R². (`uv run dvc exp diff` compares two specific runs.)

To keep an experiment, commit it:

```bash
git add dvc.lock data/metrics.json ex04/config.toml
git commit -m "experiment: degree=<value>"
```

### 8. Set up a local remote

A remote is where DVC stores the actual data files (git only stores small pointers). We use a local folder here; real projects use S3, GCS, SSH, etc.

```bash
uv run dvc remote add -d local ./dvc-remote
git add .dvc/config
git commit -m "add local dvc remote"
```

### 9. Push data to the remote

```bash
uv run dvc push
```

### 10. Simulate a fresh clone

```bash
rm -rf data/
uv run dvc pull
ls data/
```

The data is restored from the remote without re-running the pipeline.
**git tracks code, DVC tracks data.**

---

## Note: `evaluate.py` writes metrics

In ex02/ex03 `evaluate.py` only printed metrics. Here it also saves them to `data/metrics.json` so DVC can track and compare them across experiments — without that file, `dvc metrics show` / `dvc exp show` have nothing to read.

