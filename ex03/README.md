# Configuration files

We will use the code from ex02 but we will separate the code and configuration files.

This is very helpful because we no longer need to modify scripts when we want to change parameters, which makes tracking changes much easier.

### Success criteria: All tunable parameters moved to a configuration file

## Hints

1. Copy the files from ex02
2. Create a file `ex03/config.toml`
3. Move the tunable parameters (e.g. `NUM_POINTS`, `NOISE_LEVEL`, `SEED`, `DEGREE`, ...) to the toml file
   - Leave file paths as constants in the code — only the parameters you actually tune belong in the config
4. Import `tomllib` from the standard library (`import tomllib`)

Suggested `.toml` structure:

```toml
[module]
parameter = value
```

Load it with (this works regardless of where you run the script from):

```python
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.toml"

with open(CONFIG_PATH, "rb") as f:
    config = tomllib.load(f)
```

Access a parameter:

```python
value = config["module"]["parameter"]
```

5. Verify: re-run the pipeline and confirm you get the same results as ex02

```bash
uv run -m ex03.pipeline
```
