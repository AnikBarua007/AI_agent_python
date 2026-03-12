# Python AI Agent (from scratch)

A lightweight command-line AI coding agent built in Python using the Google Gemini API.
It accepts a user prompt, lets the model call local tools, and iterates until a final response is produced.

## What this project does

- Runs a CLI chat loop with Gemini (`gemini-2.5-flash` in `main.py`).
- Exposes local tool functions the model can call:
	- `get_files_info`
	- `get_file_content`
	- `run_python_file`
	- `write_file`
- Restricts tool access to a safe working directory (`./calculator`).
- Returns tool outputs back to the model for multi-step reasoning.

## Project structure

```
.
├── main.py                     # CLI entry point and agent loop
├── prompts.py                  # System prompt used by the model
├── config.py                   # Shared config values (e.g., max read limit)
├── model_lists.py              # Model listing helpers
├── functions/
│   ├── call_function.py        # Tool registration and dispatch
│   ├── get_files_info.py       # List files in working directory
│   ├── get_file_content.py     # Read file contents (bounded)
│   ├── run_python_file.py      # Execute Python scripts safely
│   └── write_file.py           # Write text files safely
├── calculator/                 # Sandboxed working directory for tools
└── test_*.py                   # Simple script-based checks
```

## Technologies used

- **Language:** Python 3.14+
- **AI SDK:** `google-genai==1.12.1`
- **Environment management:** `.env` via `python-dotenv==1.1.0`
- **CLI:** Python standard library (`argparse`)
- **Process execution:** Python standard library (`subprocess`)
- **File system operations:** Python standard library (`os`)

## Prerequisites

- Python 3.14+
- A Google Gemini API key

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

3. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the agent

```bash
python main.py "List files in the calculator folder"
```

Verbose mode (prints tool-call details):

```bash
python main.py "Create a hello.py file and run it" --verbose
```

## How tool safety works

- Every tool call is forced to use `working_directory="./calculator"`.
- Paths are normalized and validated with `os.path.commonpath(...)`.
- Requests outside the working directory are rejected.
- `run_python_file` only allows `.py` files and applies a timeout.
- `get_file_content` enforces a maximum read length from `config.max_word_limit`.

## Notes

- The current test files are executable scripts (`test_*.py`) that print outputs.
- This project is intentionally minimal and focused on learning agent/tool orchestration.