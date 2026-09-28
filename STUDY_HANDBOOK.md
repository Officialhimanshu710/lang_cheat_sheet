# Autonomous Trailer Director: Full Study Handbook

## 1. What Did the PDF Ask For?
**The Objective:** Build an AI system ("Agent") that takes a single TV episode and automatically edits 3 different trailers for 3 different audiences: Family, Young Adult, and Dialect-Region.
**The Catch:** The AI cannot just be a simple prompt. It must be highly governed. It must strict obey legal contracts (don't use expired music), age ratings (no violence in Family), cultural respect (no stereotyping in Dialect), and story truth (no leaking spoilers in Young Adult). 
**The Deliverable:** A completely automated pipeline that outputs 3 JSON files (Edit Decision Lists) showing the exact clips, timecodes, and audio chosen, along with a report proving the trailers passed all safety checks.

---

## 2. According to the Architecture, What Did We Use?
We used a **Multi-Agent Directed Acyclic Graph (DAG)** built on **LangGraph**.
*   **LangGraph (`workflow.py`):** Acts as the traffic controller. It routes the data through different "nodes" (workstations). If a trailer is broken, LangGraph loops it backwards to get fixed.
*   **Pydantic (`state.py`):** Acts as the data enforcer. It defines exact schemas (blueprints) for how the data must look.
*   **LangChain & Groq (`model_gateway.py`):** Used to call the LLMs. We wrapped the Groq API inside a `ModelGateway` class to track token costs and enforce strict structured JSON outputs.

---

## 3. What Safety Measures Did We Use? (Reducing Hallucination)
We achieved "Zero-Hallucination" through architectural design, not prompt engineering:
1.  **Symbolic Timecodes (The `CandidateBuilder`):** LLMs cannot do math or reliably output strict timecode strings like `00:01:23.400`. We built a Python script (`ingest.py`) that hides the timecodes and labels the clips as `C001`, `C002`. The AI only picks `C001`. Python puts the real timecode back in at the end. This makes timecode hallucination physically impossible.
2.  **Two-Tier Verification Engine:** 
    *   **Tier 1 (Deterministic):** Pure Python code (`deterministic.py`). It scans the AI's chosen clips against a list of blocked contracts. If the AI hallucinates a fake clip ID or uses a blocked actor, Python mathematically catches it and blocks it. No AI is used here, guaranteeing 100% accuracy.
    *   **Tier 2 (Semantic):** We use a completely separate LLM (`semantic.py`) that acts as a critic. It does not write trailers; its only job is to scan the generated trailers for spoilers and stereotypes.
3.  **Prompt Injection Guardrails:** In `model_gateway.py`, we inject a hidden `[SYSTEM]` instruction underneath every LLM request forcing it to output strict JSON, preventing the LLM from trying to "chat" or bypass rules.

---

## 4. How Did We Combine the Code? (Our Approach)
We used a **State-Driven Modular Approach**. 
Instead of writing one massive Python script that runs top-to-bottom, we broke the code into isolated folders (`src/catalog`, `src/constraints`, `src/graph`, `src/repair`, `src/verification`). 
*   **The Glue:** The `GraphState` in `state.py` is the single dictionary that connects everything. As it flows through the LangGraph nodes, each node only reads the part of the state it needs, updates its specific key, and passes it on.
*   **Concurrency Fix:** Because we generate 3 trailers at once (parallel processing), we used Python's `typing.Annotated` with a custom `merge_dicts` function in the State. This allows the 3 parallel LLMs to write their results into the main dictionary at the exact same time without overwriting each other or crashing the program.

---

## 5. The Interview Questions (From Page 6 of the PDF)

**Q: How does the system define and detect a spoiler?**
**A:** At the very beginning, a "Story Mapper" LLM scans the raw episode and extracts key narrative twists into a list of `ProtectedFacts` (e.g., "The detective is the killer"). Later, during Tier 2 Semantic Verification, an Evaluator LLM compares the trailer against the `ProtectedFacts`. If a clip reveals that fact, it is flagged as a spoiler.

**Q: How do creative generation and validation remain meaningfully independent?**
**A:** They are completely isolated in the architecture. The Creative Planners (`nodes.py`) are LLMs instructed only to assemble a compelling story. They output data and shut down. The Validators (`deterministic.py` and `semantic.py`) run entirely separate logic—often just pure Python math—with zero creative instructions. They act as a strict firewall that the creative output must pass through.

**Q: What happens when a music contract changes after planning?**
**A:** The system handles this gracefully using the Replanner loop. If a contract expires, the Tier 1 Verifier flags the trailer as a "RIGHTS_VIOLATION". LangGraph routes the trailer to the Replanner (`replanner.py`). The Replanner identifies *only the specific segment* using the bad music, swaps it out for a compliant alternative from the catalog, and sends the trailer back to Tier 1 for re-validation.

**Q: How do you personalize for a dialect audience without stereotyping it?**
**A:** We supply the Dialect Planner with explicit prompt instructions to focus on cultural nuance rather than tropes. More importantly, we use Tier 2 Semantic Verification as a safeguard. The Evaluator LLM is given strict rules to flag dialect misuse or stereotyping, blocking the trailer from release if detected.

**Q: Which part of the system would fail first at large scale?**
**A:** The LLM network calls (the Planners and Semantic Verifiers). Doing multiple LLM calls per trailer (plan + semantic review) creates heavy network I/O bottlenecks. While our `ModelGateway` limits costs, at massive scale, we would hit API rate limits or timeout errors. We would need to implement asynchronous generation (`asyncio`) or batch processing to scale it.

**Q: What did the AI (Claude/Codex) suggest that looked plausible but was wrong?**
**A:** Early on, one might assume the best way to handle timecodes is to pass the strict `00:00:00.000` string formats directly to the LLM and ask it to output them in the JSON segment. While plausible, this is wrong because LLMs are statistically terrible at retaining exact mathematical string formats. It would lead to validation crashes. The correct solution was symbolic mapping (giving the LLM simple IDs like `C001` and doing the timecode mapping in Python at the end).

---

## 6. How We Run It (And Why)
We use a standard Command Line Interface (CLI) combined with `uv` (a lightning-fast Python package manager) to execute the system. 
*   **Command:** `uv run python -m src.cli run --mode MOCK` (or `--mode LIVE`).
*   **Why a CLI?** The assignment specifically requested prioritizing agent decisions over building a large, complex User Interface. A CLI is production-ready, easily testable, and allows us to pass in arguments (like the paths to our `sample_episode.json` and `contracts.json`) cleanly.
*   **Why `MOCK` vs `LIVE`?** LLM APIs cost money. The assignment demanded a way for an evaluator to run the pipeline without supplying their personal API keys. We built a `ModelGateway` that intercepts the calls. In `MOCK` mode, the gateway intercepts the prompt and immediately returns a hardcoded, perfectly structured Pydantic object, allowing us to test the Python logic thousands of times for free without hitting rate limits.

---

## 7. How We Store Things (State and File Outputs)
We store data in two distinct ways: **In-Memory State** (during the run) and **Disk Outputs** (after the run).

**1. In-Memory Storage (The `GraphState`):**
*   **How:** As the LangGraph flowchart executes, it passes around a single Python dictionary called `GraphState`. 
*   **Why:** Instead of saving temporary data to external databases (which slows things down and costs money), `GraphState` holds everything the AI needs (the list of clips, the blocked contracts, the trailer plans) in RAM. Because we process 3 trailers simultaneously, we used a custom `merge_dicts` function. This allows all three AI planners to save their work into the `GraphState` at the exact same millisecond without overwriting each other.

**2. Disk Storage (The `sample_run/` folder):**
*   **How:** When the pipeline finishes, the `release_gate_node` (and the `escalation_quarantine_node`) converts the final Pydantic objects into JSON strings and saves them as physical files (`family_trailer.json`, `story_map.json`, etc.).
*   **Why:** The assignment requested a precise, machine-readable "Edit Decision List" (EDL) that a human video editor could theoretically load into Premiere Pro. JSON is the industry standard for this. We also store the `constraint_map.json` (showing exactly which rules were enforced) and `validation_report.md` so that human reviewers have complete Observability over the AI's final decisions before publishing.
