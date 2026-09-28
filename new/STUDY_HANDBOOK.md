# Study Handbook

This file was organized into the `new/` folder for easier grouping of the recently uploaded notes.

## Objective
Build an AI agent that takes a TV episode and automatically creates audience-specific trailers while obeying legal, age-rating, and cultural constraints.

## Stack
- LangGraph for workflow orchestration
- Pydantic for state validation
- LangChain and Groq for model access

## Safety Measures
- Symbolic timecodes reduce hallucination risk
- Deterministic verification blocks invalid outputs
- Semantic review checks tone, rating, and spoiler issues
- Replanning handles mission-critical rule violations

## Execution
Use a CLI with `uv run python -m src.cli run --mode MOCK` for deterministic testing and `--mode LIVE` for real model calls.
