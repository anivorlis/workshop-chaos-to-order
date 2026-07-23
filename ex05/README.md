# Reproducibility with pixi

`pixi` is an alternative to `uv`: a fast, cross-platform package & environment manager built on the **conda-forge** ecosystem, with its own lockfile (`pixi.lock`) and a built-in task runner.

The goal of this exercise is to run the **same code from ex01–ex04** using pixi instead of uv — same reproducibility story, different tool.

### Success criteria: Run the dice example and the fitting pipeline through pixi tasks, backed by a committed `pixi.lock`

---

## Steps

### 0. Install pixi

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

*(or `brew install pixi`)*

### 1. Initialise a pixi project

```bash
pixi init
```

This creates a `pixi.toml` manifest (project metadata, platforms, dependencies, tasks) and, on first install, a `pixi.lock`.

*Hint: pixi can also live inside your existing `pyproject.toml` under a `[tool.pixi]` table — but keep it separate here so it doesn't clash with the uv setup from the earlier exercises.*

### 2. Add the dependencies

The exercises need `numpy` and `matplotlib` (and `dvc` for ex04):

```bash
pixi add numpy matplotlib
pixi add dvc
```

These come from conda-forge and are written into `pixi.toml` + pinned in `pixi.lock`.

*Hint: for a package that only exists on PyPI, use `pixi add --pypi <name>`.*

### 3. Run a single script

The uv commands from the earlier exercises map directly — swap `uv run` for `pixi run`:

```bash
pixi run python -m ex01.e01      # was: uv run -m ex01.e01
pixi run python -m ex04.pipeline # was: uv run -m ex04.pipeline
```

`pixi run` executes inside the locked environment. Use `pixi shell` if you want to activate it interactively.

### 4. Define tasks

Instead of typing module paths, declare **tasks** in `pixi.toml`:

```toml
[tasks]
dice = "python -m ex01.e01"
generate = "python -m ex04.generate_data"
fit = { cmd = "python -m ex04.fit", depends-on = ["generate"] }
evaluate = { cmd = "python -m ex04.evaluate", depends-on = ["fit"] }
visualize = { cmd = "python -m ex04.visualize", depends-on = ["fit"] }
pipeline = { depends-on = ["evaluate", "visualize"] }
```

Now run them by name — pixi resolves the dependency order automatically:

```bash
pixi run dice
pixi run pipeline
```

*This is pixi's built-in version of the DAG idea from ex04: `depends-on` chains the stages together.*

### 5. Lock and share

```bash
git add pixi.toml pixi.lock
git commit -m "add pixi environment"
```

`pixi.lock` pins exact package versions **and** solves for each platform, so a colleague on a different OS gets the same environment with a single `pixi install`.

---

## uv → pixi cheat sheet

| Task | uv | pixi |
|---|---|---|
| Init project | `uv init` | `pixi init` |
| Add dependency | `uv add numpy` | `pixi add numpy` |
| Add PyPI-only dep | `uv add <pkg>` | `pixi add --pypi <pkg>` |
| Run a module | `uv run -m ex01.e01` | `pixi run python -m ex01.e01` |
| Run a named task | *(n/a)* | `pixi run pipeline` |
| Activate the env | `source .venv/bin/activate` | `pixi shell` |
| Install from lockfile | `uv sync` | `pixi install` |
| Lockfile | `uv.lock` | `pixi.lock` |

Same principle throughout: **the lockfile guarantees everyone gets the exact same environment.**
