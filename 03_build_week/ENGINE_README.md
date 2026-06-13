# Engine README (Day 21 Deliverable)

> Fill this in once `engine_v3.py` is working end to end.

## What the engine does
<!-- TODO: 2-4 sentences describing the prompt -> validate -> retry ->
escalate -> resume -> audit loop, in your own words. -->

## How to run it
- `python engine_v3.py` — new run, reads `workspace/input.txt`
- `python engine_v3.py --resume` — continue from `workspace/PENDING_meeting_summary.md`
- `python engine_v3.py --verify` — check `workspace/AUDIT_LOG.md` against current file hashes

## The `workspace/` file structure
<!-- TODO: describe what each file means, e.g. -->
- `input.txt` —
- `model_output.json` —
- `final_summary.json` —
- `PENDING_meeting_summary.md` —
- `AUDIT_LOG.md` —
- `raw_response.txt` —
