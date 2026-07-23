# Exercise 00 — Check Your Tools

Before we start, make sure the following CLI tools are installed on your machine.

---

## Git

Distributed version control system for tracking changes in your code.

<details>
<summary>macOS</summary>

Install via [Homebrew](https://brew.sh): `brew install git`
Or download the installer from https://git-scm.com/download/mac

</details>

<details>
<summary>Windows</summary>

Download Git for Windows from https://git-scm.com/download/win

</details>

<details>
<summary>Linux</summary>

```bash
# Debian/Ubuntu
sudo apt install git

# Fedora
sudo dnf install git
```

Or see https://git-scm.com/download/linux

</details>

---

## uv

An extremely fast Python package and project manager, written in Rust.

<details>
<summary>macOS / Linux</summary>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Full instructions: https://docs.astral.sh/uv/getting-started/installation/

</details>

<details>
<summary>Windows</summary>

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Full instructions: https://docs.astral.sh/uv/getting-started/installation/

</details>

---

## pixi (optional)

A fast, cross-platform package manager for reproducible environments. Optional for this workshop — install it if you'd like to follow along with the pixi-based examples.

<details>
<summary>macOS / Linux</summary>

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

If your system doesn't have `curl`, you can use `wget`:

```bash
wget -qO- https://pixi.sh/install.sh | sh
```

Full instructions: https://pixi.prefix.dev/latest/installation/

</details>

<details>
<summary>Windows</summary>

```powershell
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Full instructions: https://pixi.prefix.dev/latest/installation/

</details>

---

### Success Criteria

Run the following — both should print a version number:

```bash
git --version
uv --version
```

If you installed pixi, this should also print a version number:

```bash
pixi --version
```
