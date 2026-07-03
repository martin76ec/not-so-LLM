# AGENTS.md

Compact guidance for OpenCode sessions working in this repo.

## Toolchain

- Managed with **uv** (Python **3.14**, pinned in `.python-version`). Run anything via `uv run python ...`.
- Runtime deps: **`regex`** PyPI package (not stdlib `re` — existing code imports `regex`, prefer it for new text/string code) and **PyTorch Lightning** for NN layers/training.
- No test runner, linter, formatter, or typechecker is configured. `tests/` exists but is empty. Do not assume `pytest`/`ruff`/`mypy` are available — confirm with the user before introducing one.
- No `uv run` task aliases or `[tool.uv]` scripts are defined.
- When adding Lightning, run `uv add lightning` so the lockfile stays consistent.

## Architecture

From-scratch transformer LLM. The pipeline is documented in `README.md` (input prep -> transformer block -> efficiency/generation upgrades -> prediction head); trust it as the spec.

- Text prep / tokenizer / data-handling components are written from scratch (see `src/components/text_preparation.py`).
- **Neural network layers and training use PyTorch Lightning** (`lightning.LightningModule`, `Trainer`, built-in `nn` layers, etc.). Do not hand-roll attention/FFN/normalization forward passes — compose Lightning/torch primitives.
- `src/stages/` — pipeline stage orchestration (composes components). Currently stubs.
- `src/components/` — individual NN building blocks (attention, FFN, normalization, KV cache, tokenizer, sampler, LM head, etc.). Mostly empty stubs.
- `src/datasets/` — reserved, empty.
- `src/main.py` — real entrypoints: `nn_build()`, `nn_train()`, `nn_use()` (stubs).
- Root `main.py` is the uv-generated hello stub, not the app entrypoint — don't extend it.

## Code style

Repo-specific rules (differ from common defaults):

- **No unnecessary comments.** Only comment where the code genuinely needs explanation; skip restating what a line does.
- **Prefer short forms of blocks** — list/dict comprehensions, single-expression returns, inline conditionals where readable — over verbose multi-line equivalents.
- **Do not wrap everything in try/except.** Use a single general try/except at the top level / program boundary, not around every statement. Let errors propagate naturally to the boundary handler.
- Use `regex` (not stdlib `re`) for text/string code.
- Class/file names use `snake_case` (e.g. `class text_preparation:`, `mult_head_attention.py`), not PascalCase — match the existing style.