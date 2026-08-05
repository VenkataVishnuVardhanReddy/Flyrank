# Agent MVP: Build Log & Run Verification

This document contains the build log, system deviations, and run verification for the **Perception Safety Telemetry Auditor** agent.

---

## 1. Agent Build Log & Iteration History

### Run 1: Basic Python Pytest Trigger
- **What broke:** Invoking raw `pytest` on the local test script raised a `ModuleNotFoundError: No module named 'src'` due to python pathing issues with relative imports on Windows.
- **What we changed:** Pre-pended the shell execution command with `$env:PYTHONPATH="."` to force Python to resolve the workspace root directory correctly.

### Run 2: Output JSON File Generation
- **What broke:** The agent successfully compiled the metrics but outputted them as console print statements instead of writing them to a structured file.
- **What we changed:** Added specific instructions in the agent's prompt to dump the final metrics dictionary to a dedicated `outputs/telemetry_metrics.json` file.

### Run 3: Epsilon Bound Extraction
- **What broke:** When parsing paper text fragments, the model struggled to differentiate between the training epsilon (learning rate bounds) and adversarial perturbation bounds.
- **What we changed:** Refined the Gather Prompt system constraints, directing the model to search strictly for "$L_p$-norm perturbation constraints" and cross-reference them with the results table.

---

## 2. Deviations from the FL-04 Spec
1. **Dynamic arXiv PDF Download (Cut):**
   - *Spec:* Download raw PDFs dynamically from arXiv.
   - *Actual:* We cut this in favor of ingesting pre-downloaded txt/PDF paper extracts. Dynamic download introduces slow network timeouts and complex parsing (PDF-to-text formatting errors), which frequently broke the agent's context loop. Keeping the papers local guarantees speed and high-confidence extraction.
2. **Interactive Calendly Booking (Simplified):**
   - *Spec:* Automate booking creation.
   - *Actual:* Simplified to rendering the Calendly calendar embed link, as a full OAuth API integration exceeded the 10-hour build limit.

---

## 3. End-to-End Execution Walkthrough

```text
[Step 1] Ingest local perception paper extract ('Madry_PGD.txt')
   │
   ├──► Extraction: L-inf norm bound (8/255)
   │
[Step 2] Read local tests/test_defense.py
   │
   ├──► Verification: parameters match paper limits
   │
[Step 3] Run Pytest execution command:
   │    $env:PYTHONPATH="." ; pytest tests/test_defense.py
   │
   ├──► Output: 3 passed, 0 failed (100% success)
   │
[Step 4] Write work/outputs/telemetry_metrics.json
```

---

## 4. Evidence of Successful Run (Screenshots)

We have verified the agent's operations using screenshots of the active workspace and tools in use:
1. **Claude Project configuration setup:** `work/ai-fluency/images/claude_project_screenshot.png` (displays instructions and active text sources).
2. **Terminal execution run:** Verification logs displaying 100% test success under active tool calls.
