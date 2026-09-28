# Known Limitations

This file was organized into the `new/` folder for easier grouping of the recently uploaded notes.

## Major Trade-offs
1. Mock mode is used for stable and cheap testing, but real Groq integration still needs the API path configured.
2. Audio and subtitle slicing require stronger real media metadata handling.
3. Parallel LLM calls may bottleneck under network or concurrency constraints.
4. Replanning currently uses a deterministic fallback strategy rather than more advanced semantic replacement logic.
