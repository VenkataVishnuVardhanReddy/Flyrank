# Perception Safety Telemetry Auditor: README

This repository contains the autonomous AI safety agent designed to verify machine learning perception models (e.g. Bilateral pre-processing filters) against adversarial attacks (FGSM/PGD) and output ISO 21448 telemetry compliance logs.

---

## 1. System Architecture Sketch

```text
               +----------------------------------+
               |  Raw Academic Paper / Txt Input  |
               +----------------+-----------------+
                                |
                                v
               +----------------+-----------------+
               |  Gather Agent: Parse math & bounds|
               +----------------+-----------------+
                                |
                                v (JSON Payload)
               +----------------+-----------------+
               |  Critique Agent: Check Volatility|
               +----------------+-----------------+
                                |
                                v (Terminal Trigger)
               +----------------+-----------------+
               |  Pytest Script execution (Local) |
               +----------------+-----------------+
                                |
                                v (JSON output)
               +----------------+-----------------+
               |  Telemetry Log Writer            |
               +----------------+-----------------+
```

---

## 2. Installation & Setup

A stranger can reproduce the agent setup locally by following these steps:

### Prerequisites:
- Python 3.9+
- Git

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/VenkataVishnuVardhanReddy/Flyrank.git
   cd Flyrank
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the Python Path:**
   On Windows PowerShell:
   ```powershell
   $env:PYTHONPATH="."
   ```
   On Linux/macOS:
   ```bash
   export PYTHONPATH="."
   ```
4. **Configure your API Keys:**
   Ensure your local environment variable holds your Brave Search API key or Claude API keys if running the agent via terminal:
   ```bash
   export BRAVE_API_KEY="your-api-key"
   ```

---

## 3. Usage Example

To audit a local defense test against a new adversarial paper summary, run:
```bash
python work/scripts/run_audit.py --paper work/ai-fluency/papers/Madry_PGD.txt --test tests/test_defense.py
```

### Expected Output Log:
```text
[INFO] Reading paper: Madry_PGD.txt
[INFO] Extracted bounds: L_inf norm, epsilon = 8/255
[INFO] Auditing tests/test_defense.py...
[INFO] Running local pytest suite...
====================== 3 passed in 1.42s ======================
[SUCCESS] Robust recovery rate: 82.4% (Clean: 98.0%, Robust: 80.8%)
[SUCCESS] Log written to work/outputs/telemetry_metrics.json
```

---

## 4. Evaluation Results (v2)

We evaluated the agent across 5 distinct pre-build test cases:

| Test ID | Case Description | Target Output | Status | Result |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Math Extraction | Extract $\epsilon = 8/255$ | **PASSED** | 100% extraction accuracy. |
| **02** | Syntax Repair | Auto-fix NumPy index error | **PASSED** | Corrected index slices in 1 pass. |
| **03** | Telemetry Calculation | Calculate recovery metrics | **PASSED** | Output matching math formulas. |
| **04** | Exclusion Filters | Rejection of ToS/Login pages | **PASSED** | Correctly blocked utility pages. |
| **05** | Guardrail Interception | Intercept raw `git push` commands | **PASSED** | Blocked execution, requested input. |

---

## 5. System Limitations & Guardrails
- **Observation Only:** The agent evaluates model performance but cannot prove causal robustness gains under physical-world camera occlusions.
- **API Rate Limits:** High-frequency searches using Brave Search API can throttle the gather loop.
- **Strict Terminal Lock:** The agent is restricted to read-only tools and cannot write or modify core source modules without active user prompts.
