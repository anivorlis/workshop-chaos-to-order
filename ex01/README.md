# Goal: Run the scripts that our colleague gave us

Tools: uv and git
Dependencies: numpy and matplotlib


### Exercise

Step 0: 
- `uv init --python=3.13`

Step 1:
- `uv run ex01/e01.py`

Step 2:
- add to `e02.py`: `from ex01.e01 import roll_dice`
- `uv add numpy`
- `uv run ex01/e02.py` (this will give an error)
- *Running as a script breaks the `ex01.e01` package import.*
- `uv run -m ex01.e02`

**Question:** When we run the script multiple times, why do we get different results?

<details>
<summary>Answer</summary>

`random` uses a pseudorandom number generator. Each run is seeded from a different starting value (by default derived from the system time / OS entropy), so the sequence of "random" numbers differs every time. Set a fixed seed (e.g. `random.seed(42)`) to get reproducible results.

</details>

Step 3:
- add to `e03.py`: `from ex01.e02 import dice_simulation, dice_statistics`
- `uv add matplotlib`
- `uv run -m ex01.e03`

Step 4:
- write a new module: `ex01/e04.py`
- use a seed for consistent values
- `uv run -m ex01.e04`

### Success criteria
- We can roll the dice N times and have consistent results!
