# Scripts Directory & Engineering Standards

All CLI tools in this directory adhere to the following architecture:

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
- Each CLI tool solves **one exact, clear problem**.
- CLI scripts in this skill are deterministic, standard-library-only tools with zero external network or LLM dependencies.

## 3. Logging & Debuggability
- Every CLI tool configures a logger by default.
- Logs are appended to `./.logs/<tool_name>_<timestamp>.log` within this working directory for rapid post-mortem debugging.
- The `./.logs` directory is gitignored.

## 4. Temporary Data Directory (`data/`) & Target Overrides
- `scripts/data/` is the **default** directory for intermediate JSON files, cached payloads, or scratch outputs generated during tool execution.
- **Target Override Exception**: If a command, workflow requirement, or user prompt specifies a designated target directory or file (e.g., via `--output`), the tool writes directly to that target instead of `data/`.
- The `scripts/data/` directory is gitignored.

## Tools in this Directory
- `score_competitors.v1.py` (symlinked as `score_competitors.py`):
  Evaluates competitor relevance scores, calculates claim confidence scores, checks evidence log verification rules (2+ independent sources for material claims), and generates comparative matrices.
