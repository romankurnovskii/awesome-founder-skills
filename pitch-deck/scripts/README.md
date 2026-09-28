# Scripts Directory & Engineering Standards

## Tools in this directory

| Tool | Purpose |
| :--- | :--- |
| [`score_deck.py`](score_deck.py) → `score_deck.v1.py` | Deterministic pitch-deck pre-screen. Reconstructs slides from Markdown, text, PDF, or PPTX and evaluates Track A (42 anti-patterns) and Track B (28 acceptance criteria), then applies the Capital Gate verdict. Emits Markdown or JSON. |

```bash
python3 score_deck.py --file deck.md --company "Acme"            # read-ahead budget
python3 score_deck.py --file deck.md --artifact presented        # 30-word budget
python3 score_deck.py --file deck.pdf --json --out audit.json
python3 score_deck.py --doctor                                   # self-diagnostic
```

All CLI tools in this directory must adhere to the following architecture:

## 1. CLI Tool Immutability & Versioning
When a CLI tool requires refactoring that could change logic:
1. **Treat the existing tool as immutable** (unless fixing an obvious typo).
2. If the tool is not yet versioned (`tool.py`), snapshot it to `tool.v1.py`.
3. Author the updated logic in `tool.v2.py`.
4. Update the canonical softlink to point to the latest version:
   ```bash
   ln -sf tool.v2.py tool.py
   ```
5. **Docstring Changelog**: Every new version MUST document in its docstring what changed compared strictly to the previous version.

## 2. Simplicity & Single Responsibility
- Each CLI tool must solve **one exact, clear problem**.
- If a new problem arises, author a separate discrete CLI tool rather than bloating an existing script into a monolith.

## 3. Logging & Debuggability
- Every CLI tool must configure a logger by default.
- Logs must be appended to `./.logs/<tool_name>_<timestamp>.log` within the working directory for rapid post-mortem debugging.
- The `./.logs` directory is gitignored.

## 4. Temporary Data Directory (`data/`) & Target Overrides
- `scripts/data/` is the **default** directory for intermediate JSON files, cached payloads, or scratch outputs generated during tool execution.
- **Target Override Exception**: If a command, workflow requirement, or user prompt specifies a designated target directory (e.g., via `--output-dir`), the tool MUST write to that target directory instead of falling back to `data/`.
- The `data/` directory is gitignored.
