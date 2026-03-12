# ATS-Ready Project Summary

## Project Title
Python AI Agent (from scratch)

## One-line Description
Built a Python-based AI coding agent that integrates Google Gemini function-calling with secure local tooling for file operations and script execution.

## ATS-Friendly Summary
Developed a command-line AI agent in Python that uses the Google GenAI SDK to process user prompts and autonomously invoke structured tool functions. Implemented function-calling for file discovery, content reading, file writing, and Python script execution within a restricted sandbox directory. Added safety controls for path traversal prevention, file-type validation, bounded file reads, and command execution timeout handling. Integrated environment-based API key management using dotenv and designed a multi-iteration tool-response loop for robust agent reasoning.

## Key Responsibilities
- Designed and implemented an LLM tool-calling architecture using Gemini function declarations.
- Built modular Python tools for directory scanning, file I/O, and script execution.
- Enforced secure path normalization and sandbox constraints to prevent unauthorized file access.
- Added runtime safeguards, including output handling and execution timeout behavior.
- Structured agent loop to append model outputs and tool responses across iterative reasoning steps.

## Technologies Used
- Python 3.14+
- Google GenAI SDK (`google-genai`)
- `python-dotenv`
- `argparse`, `subprocess`, `os` (Python standard library)
- Function-calling / tool invocation patterns for LLM agents

## Keywords (ATS)
Python, AI Agent, LLM, Gemini API, Function Calling, Tool Use, Prompt Engineering, CLI Application, File System Security, Path Traversal Prevention, Subprocess Automation, Sandbox Execution, API Integration, Software Engineering

## Impact Statement
Created a practical AI-agent foundation demonstrating secure local tool orchestration, modular architecture, and production-relevant controls for LLM-powered developer workflows.
