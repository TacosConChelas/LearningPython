# LearningPython
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=for-the-badge)
![Level](https://img.shields.io/badge/level-intermediate%E2%86%92advanced-blue?style=for-the-badge)

<pre>
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
</pre>

---

A repository that documents my journey learning and practicing Python — from
language fundamentals to algorithm challenges, OOP, decorators, generators,
scripting tools, and containerized mini-projects. The long-term goal is to
reach **professional / mid-level** proficiency for backend and tooling roles.

This README also doubles as a **personal learning roadmap**: every level
below lists what is already covered (with file/folder references) and what is
still pending. Items marked `[x]` are practiced, `[~]` are partially covered,
and `[ ]` are gaps I am actively planning to fill.

---

## Table of Contents

- [Repository Map](#repository-map)
- [Learning Path](#learning-path)
  - [Stage 1 — Foundations](#stage-1--foundations)
  - [Stage 2 — Core Data Structures & Idioms](#stage-2--core-data-structures--idioms)
  - [Stage 3 — Functions, Decorators & Generators](#stage-3--functions-decorators--generators)
  - [Stage 4 — Object-Oriented Programming](#stage-4--object-oriented-programming)
  - [Stage 5 — Algorithms & Problem Solving](#stage-5--algorithms--problem-solving)
  - [Stage 6 — Practical Scripting, Regex & APIs](#stage-6--practical-scripting-regex--apis)
  - [Stage 7 — Packaging & Containers](#stage-7--packaging--containers)
  - [Stage 8 — Testing](#stage-8--testing-pending)
  - [Stage 9 — Advanced Typing, Logging & Context Managers](#stage-9--advanced-typing-logging--context-managers-partial)
  - [Stage 10 — Concurrency & Async I/O](#stage-10--concurrency--async-io-pending)
  - [Stage 11 — Web APIs & Databases](#stage-11--web-apis--databases-pending)
  - [Stage 12 — Engineering Practices](#stage-12--engineering-practices-pending)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)

---

## Repository Map

| Folder | Purpose |
|--------|---------|
| `CS50P/` | Exercises from Harvard's CS50P (Chapter0–3, APIs, comprehensions, imports). |
| `Concepts/` | Deep dives into individual language features (decorators, generators, OOP, comprehensions, sets, interfaces, queues). |
| `Retos/` | Algorithmic challenges and small problem-solving katas (incl. `Retos/LeetCode/`). |
| `Scripting/` | Real-world CLI tools — CSV→JSON converter, calculator, networking/API fuzzing. |
| `Mini_Docker_Proyects/` | Small containerized exercises (generators, web server, volumes). |

---

## Learning Path

The path is ordered by **conceptual difficulty**, not by chronological order of
practice. Each stage points to the folder(s) or file(s) that act as proof of
practice.

---

### Stage 1 — Foundations

> Variables, control flow, I/O, basic types, modules, imports.

- [x] Variables, conditionals, loops → `CS50P/Chapter0/`, `CS50P/Chapter1/`
- [x] Functions & basic I/O → `CS50P/Chapter2/`, `CS50P/Chapter3/`
- [x] Module imports & code reuse → `CS50P/importing_code/`
- [x] Standard library basics (`random`, `math`) → `CS50P/Random/`

---

### Stage 2 — Core Data Structures & Idioms

> Lists, dicts, sets, tuples and the Pythonic way of expressing transformations.

- [x] Lists & list algorithms → `Concepts/List/`
- [x] List comprehensions → `Concepts/List_Comprehension/`, `CS50P/comprehencions/`
- [x] Dict comprehensions → `Concepts/Dictionary_Comprehension/`
- [x] Sets (membership, dedup, set algebra) → `Concepts/Set/`
- [x] Queues (FIFO patterns) → `Concepts/Queue/`

---

### Stage 3 — Functions, Decorators & Generators

> Higher-order functions, closures, lazy iteration.

- [x] Decorators (logging, timing, retry, memoization, composition) → `Concepts/Decorator/`
- [x] Generators & `yield` / `send()` → `Concepts/Generator/`, `Concepts/Yield/`
- [x] File handling with generators → `Concepts/Generator/File_Handling_and_Generators/`, `Concepts/Generator/lazy_file_line_generator/`
- [ ] **Finish incomplete exercise** → `Concepts/Decorator/memoisation_cache_decorator.py` (currently only contains the prompt).
- [ ] **Finish incomplete exercise** → `Concepts/Generator/async_number_stream_geneator.py` (only the prompt; depends on Stage 10).

---

### Stage 4 — Object-Oriented Programming

> Classes, inheritance, polymorphism, abstraction, interfaces.

- [x] Classes, encapsulation, dunder methods → `Concepts/OOP/back_account_lvUP.py`
- [x] Inheritance & `super()` → `Concepts/OOP/inheritance_vehicle_lvUP.py`
  - [ ] **Bug to fix:** `Motorcycle.speed()` is defined twice in this file — the second silently overrides the first.
- [x] Abstract Base Classes (`ABC`, `@abstractmethod`) → `Concepts/OOP/Abstraction/`
- [x] Interfaces & duck typing → `Concepts/Interface/` (incl. `protocol_runtime_interface.py`, `duck_typed_interface.py`, `plug_in_system_interface.py`)
- [ ] `@property`, `@staticmethod`, `@classmethod` patterns (refactor `back_account_lvUP.py` and `inheritance_vehicle_lvUP.py` to use `@property` for getters).
- [ ] `dataclasses` (`@dataclass`, `field`, `frozen=True`).

---

### Stage 5 — Algorithms & Problem Solving

> Complexity awareness (O(n) vs O(n²)), classic patterns.

- [x] Set-based optimizations (Two Sum, Longest Consecutive Sequence) → `Concepts/Set/`
- [x] String/number katas (palindromes, Armstrong numbers, prime numbers, factorials, fibonacci) → `Retos/palindromos/`, `Retos/ArmstrongNumber/`, `Retos/numbersPrimes/`, `Retos/factorial/`, `Retos/fibonacci/`
- [x] Frequency counting & text analysis → `Retos/wordCount/`, `Retos/frequencyCounter/`, `Retos/analizarTexto/`
- [x] LeetCode practice → `Retos/LeetCode/` (`two_Sum.py`, `add_two_numbers.py`)
- [ ] **Bug to fix:** `Retos/wordCount/word_counter_lvUP.py` imports `Counter` from `typing` — it should be `from collections import Counter`.
- [ ] Dynamic programming (memoization + tabulation) — start with classic problems (climb stairs, coin change, longest common subsequence).
- [ ] Graph / tree traversals (BFS, DFS) — frequent in interviews.

---

### Stage 6 — Practical Scripting, Regex & APIs

> Real tooling — CLI args, file I/O, HTTP clients, regular expressions.

- [x] Interactive CLI tools → `Scripting/basic_calculator/`
- [x] Production-grade CSV/JSON converter (`argparse`, encoding detection, error handling) → `Scripting/csv_to_json/csv_to_json_v2.py`
- [x] Log analysis → `Scripting/csv_to_json/log_analyzer.py`
- [x] HTTP requests with `requests` → `CS50P/APIs/`, `Scripting/Networking/requests_http.py`
- [x] API fuzzing with wordlists → `Scripting/Networking/`
- [x] Regular expressions, 3 difficulty tiers → `Retos/exprecionesRegulares_Regex/level_1/`, `level_2/`, `level_3/`

---

### Stage 7 — Packaging & Containers

> Containerized exercises and environment isolation.

- [x] Containerizing Python scripts → `Mini_Docker_Proyects/docker_proyect_1/` (generators + env vars)
- [x] Minimal containerized HTTP server → `Mini_Docker_Proyects/networking_docker_proyect/`
- [x] Docker volumes for persistence → `Mini_Docker_Proyects/volume_proyect/`
- [ ] Python virtual environments (`venv`, `pip freeze`, `requirements.txt`) — add a root `requirements.txt` and per-project venvs.
- [ ] Modern packaging (`pyproject.toml`, `poetry` or `uv`).

---

### Stage 8 — Testing *(pending)*

> The single most important missing skill for an interview.

- [ ] `unittest` basics — write tests for `Concepts/OOP/back_account_lvUP.py`.
- [ ] `pytest` fundamentals — `assert`, fixtures, `parametrize`.
- [ ] Test the algorithms in `Concepts/Set/` and `Retos/LeetCode/` (great for property-style assertions).
- [ ] Mocking external calls — write tests for `Scripting/Networking/requests_http.py` using `unittest.mock` or `pytest-mock`.
- [ ] Coverage reporting with `coverage.py` or `pytest-cov`.

**Target:** A new top-level `tests/` folder with at least one test module per existing `Concepts/` subtopic.

---

### Stage 9 — Advanced Typing, Logging & Context Managers *(partial)*

> The polish that separates intermediate from senior code.

- [~] Basic type hints — already used in ~75% of files.
- [~] `Protocol` / structural subtyping — partially explored in `Concepts/Interface/protocol_runtime_interface.py` and `file_protocol_interfaces.py`.
- [ ] `TypedDict`, `Generic[T]`, `Callable[..., T]`, `Optional`, `Union` / `X | Y`.
- [ ] Static type checking with `mypy`.
- [ ] Custom context managers — both class-based (`__enter__`/`__exit__`) and `@contextlib.contextmanager`. Suggested exercise: a `with timer():` helper.
- [ ] Structured logging with the `logging` module (replace `print` debugging in `Scripting/`).
- [ ] Custom exception hierarchies.

---

### Stage 10 — Concurrency & Async I/O *(pending)*

> Required for backend/networking roles.

- [ ] Threading basics — `threading.Thread`, `Lock`, `Queue`.
- [ ] `concurrent.futures.ThreadPoolExecutor` / `ProcessPoolExecutor`.
- [ ] `asyncio` fundamentals — `async def`, `await`, `asyncio.run`, `asyncio.gather`.
- [ ] Async HTTP with `httpx` or `aiohttp`.
- [ ] **Suggested project:** rewrite the API fuzzer in `Scripting/Networking/` as an async client and benchmark it against the synchronous version.
- [ ] Complete `Concepts/Generator/async_number_stream_geneator.py`.

---

### Stage 11 — Web APIs & Databases *(pending)*

> The flagship missing project. This is what the interviewer will want to see.

- [ ] **FastAPI** — minimal CRUD with at least 5 endpoints, Pydantic models for validation.
- [ ] **SQLite** + raw SQL (the basics matter).
- [ ] **SQLAlchemy** (Core or ORM) — one model with relationships.
- [ ] Request/response schemas, dependency injection, error handling middleware.
- [ ] Auth basics (API keys or JWT).
- [ ] Tests for the API using `pytest` + FastAPI's `TestClient`.

**Suggested target:** a `Projects/task_api/` folder containing the full mini-project.

---

### Stage 12 — Engineering Practices *(pending)*

> Tooling and habits expected in any professional team.

- [ ] Formatter — `black` or `ruff format`.
- [ ] Linter — `ruff` (preferred) or `flake8` + `pylint`.
- [ ] Pre-commit hooks (`pre-commit` framework).
- [ ] CI on GitHub Actions — run tests + lint + mypy on every push.
- [ ] Conventional commit messages (currently mixed Spanish/English — pick one and stick to a convention like `feat:`, `fix:`, `docs:`).
- [ ] A `CONTRIBUTING.md` or at least a documented project structure in this README.

---

## Tech Stack

- **Language:** Python 3.10+ (uses `list[int]` syntax, `match`/`case`).
- **Currently used libs:** `requests`, `csv`, `json`, `re`, `abc`, `collections`, `typing`.
- **Planned:** `pytest`, `httpx`, `fastapi`, `pydantic`, `sqlalchemy`, `mypy`, `ruff`.
- **Tooling:** Docker (for the `Mini_Docker_Proyects/`).

---

## How to Run

Most files are self-contained scripts:

```bash
python3 path/to/script.py
```

Scripts with CLI arguments (e.g. the CSV→JSON converter) document their flags
via `--help`:

```bash
python3 Scripting/csv_to_json/csv_to_json_v2.py --help
```

The Docker mini-projects each contain their own `Dockerfile`; build and run
from inside the relevant folder:

```bash
cd Mini_Docker_Proyects/docker_proyect_1
docker build -t safe-divider .
docker run --rm safe-divider
```

---

## Progress Snapshot

| Stage | Status |
|-------|--------|
| 1. Foundations | Done |
| 2. Core data structures & idioms | Done |
| 3. Functions, decorators & generators | Done (2 exercises pending) |
| 4. OOP | Done (minor bug + `@property` refactor pending) |
| 5. Algorithms | Active (DP & graphs pending) |
| 6. Scripting, regex & APIs | Done |
| 7. Packaging & containers | Partial (modern packaging pending) |
| 8. Testing | **Not started — highest priority** |
| 9. Advanced typing, logging, context managers | Partial |
| 10. Concurrency & async | Not started |
| 11. Web APIs & databases | Not started |
| 12. Engineering practices | Not started |
