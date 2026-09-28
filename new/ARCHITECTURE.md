# Architecture

This file was organized into the `new/` folder for easier grouping of the recently uploaded notes.

## Overview
The system is designed as an evidence-grounded, constraint-enforcing multi-agent workflow built around a deterministic pipeline and LLM-based planning stages.

## Core Principles
- Deterministic validation overrides LLM discretion
- Symbolic clip references prevent hallucinated timestamps
- State isolation prevents parallel-write conflicts
- Replanning is targeted and limited to impacted segments

## Pipeline Summary
1. Ingestion and catalog generation
2. Constraint compilation
3. Story and spoiler mapping
4. Audience strategy and planning
5. Verification and repair
6. Final release or escalation
