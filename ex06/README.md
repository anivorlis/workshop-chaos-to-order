# Containerise the Pipeline

A container packages your code, dependencies, and environment into a single image that runs identically anywhere. It is the final answer to "works on my machine."

Here we containerise the **ex03 pipeline** (the config-driven version) so it runs the same way on any machine, straight from the lockfile.

### Success criteria: Build the image and run the ex03 pipeline inside a container

---

## Build the image

```bash
docker build -t chaos-to-order .
```

This reads the `Dockerfile` at the project root and creates an image called `chaos-to-order`.

## Run the pipeline

```bash
docker run -v $(pwd)/data:/app/data chaos-to-order
```

The `-v` flag mounts your local `data/` folder into the container so the output files are saved on your machine after the container exits.

## Check the outputs

```bash
ls data/
```

You should see `input.csv`, `coefficients.json`, and `plot.png` — the outputs of the ex03 pipeline.

---

## How the Dockerfile works

```dockerfile
FROM python:3.13-slim                          # base OS + Python
COPY --from=ghcr.io/astral-sh/uv:latest ...   # add uv
COPY pyproject.toml uv.lock ./                 # copy dependency spec
RUN uv sync --frozen --no-dev                  # install exact versions from lockfile
COPY ex03/ ex03/                               # copy pipeline code + config.toml
CMD ["uv", "run", "-m", "ex03.pipeline"]       # default command
```

The lockfile (`uv.lock`) is the key — it guarantees the container installs the exact same package versions every time, on any machine.

`COPY ex03/` brings in `config.toml` too, so the container runs with the same parameters you set in ex03. Change a value in `ex03/config.toml`, rebuild, and the container picks it up.

## Useful commands

| Command | What it does |
|---|---|
| `docker build -t <name> .` | build an image from the Dockerfile |
| `docker run <name>` | run a container from an image |
| `docker run -v <host>:<container> <name>` | mount a folder from host into container |
| `docker images` | list built images |
| `docker ps -a` | list all containers (including stopped) |
| `docker rmi <name>` | delete an image |
