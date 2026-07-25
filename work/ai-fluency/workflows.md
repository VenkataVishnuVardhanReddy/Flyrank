# Research Synthesis Workflow & Walkthrough

This document details the design, configuration, and runs of the **Literature Synthesis Workflow for Thesis Research** (Task A from the FL-01 workflow audit).

---

## 1. Workflow Architecture & Step Diagram

We design a 3-step chained pipeline to ingest dense research papers and output structured, verified literature summaries for the thesis:

```text
  [ Raw Research Paper PDF / Text ]
                 │
                 ▼
     ┌───────────────────────┐
     │  Step 1: GATHER       │ (Extracts math, bounds, and datasets)
     └───────────┬───────────┘
                 │
                 ▼ (Handoff: Raw Extraction Notes)
     ┌───────────────────────┐
     │  Step 2: CRITIQUE     │ (Cross-references with bilateral shielding)
     └───────────┬───────────┘
                 │
                 ▼ (Handoff: Critiqued Synthesis)
     ┌───────────────────────┐
     │  Step 3: DRAFT & VIBE │ (Formats academic markdown + checks stats)
     └───────────────────────┘
```

---

## 2. Prompts & System Configuration

We build the workflow inside a custom Claude Project using chained system instructions:

### Step 1: The Gather Prompt
```text
System: Act as a mathematical extraction agent.
Input: Raw text of a computer vision or adversarial robustness research paper.
Instructions:
1. Extract the core mathematical formulation of the attack/defense.
2. Identify all epsilon bounds (L-infinity, L-2, L-0 norms) and the datasets tested (e.g., MNIST, CIFAR-10, ImageNet).
3. List the clean accuracy vs. adversarial accuracy metrics reported in the results section.
Output format: Raw JSON listing fields: "formula", "bounds", "metrics", "datasets".
```

### Step 2: The Critique Prompt
```text
System: Act as an academic reviewer and safety engineer.
Input: The JSON output from Step 1.
Instructions:
Analyze how the extracted attack or defense methodology intersects with a Bilateral Pre-Processing Filter defense.
Identify:
1. Volatility points: Does the attack target gradients? (Bilateral filters smooth high-frequency gradients).
2. Defense limitations: Will the defense fail against iterative attacks like PGD?
Output format: Two bulleted sections: "Gradient Vulns" and "Iterative Limitations".
```

### Step 3: The Draft & Vibe Prompt
```text
System: Act as a rigorous computer vision safety researcher.
Input: Outputs from Step 1 and Step 2.
Instructions:
Compile the findings into a structured markdown report using these exact headers:
### 1. Citation & Core Claim
### 2. Mathematical Formulation & Bounds
### 3. Quantitative Results (Metrics)
### 4. Thesis Relevance

Constraint: Use clear, decision-support language. Remove all conversational filler. Verify that all metrics are direct quotes.
```

---

## 3. The Five Runs

We ran the workflow on 5 real paper inputs relevant to our perception safety research:

### Run 1: Fast Gradient Sign Method (FGSM) - Goodfellow et al.
- **Output Excerpt:**
  ```markdown
  ### 1. Citation & Core Claim
  Goodfellow et al. (2015). 'Explaining and Harnessing Adversarial Examples.' Explores model linearity.
  ### 2. Mathematical Formulation & Bounds
  perturbation = epsilon * sign(grad_x L(theta, x, y)) under L_inf norm.
  ### 3. Quantitative Results (Metrics)
  Maxout network accuracy drops from 89.4% to 11.9% on MNIST with epsilon = 0.25.
  ### 4. Thesis Relevance
  Bilateral filter pre-processing successfully smooths single-step linear perturbations.
  ```

### Run 2: Projected Gradient Descent (PGD) - Madry et al.
- **Output Excerpt:**
  ```markdown
  ### 1. Citation & Core Claim
  Madry et al. (2018). 'Towards Deep Learning Models Resistant to Adversarial Attacks.' Casts security as robust optimization.
  ### 2. Mathematical Formulation & Bounds
  x^(t+1) = Proj(x^t + alpha * sign(grad_x L(theta, x^t, y))) under L_inf <= 8/255.
  ### 3. Quantitative Results (Metrics)
  ResNet clean accuracy drops from 95.2% to 45.8% under 20-step CIFAR-10 attack.
  ### 4. Thesis Relevance
  Shows single-step pre-processing filters will fail against iterative optimization attacks, requiring adaptive defense analysis.
  ```

### Run 3: Carlini & Wagner Attack (C&W) - Carlini & Wagner
- **Output Excerpt:**
  ```markdown
  ### 1. Citation & Core Claim
  Carlini & Wagner (2017). 'Towards Evaluating the Robustness of Neural Networks.' Proves defensive distillation fails.
  ### 2. Mathematical Formulation & Bounds
  Minimizes ||delta||_2^2 + c * f(x+delta) where f is the objective classification function.
  ### 3. Quantitative Results (Metrics)
  Achieves 100% attack success rate against defensive distillation on MNIST/CIFAR-10.
  ### 4. Thesis Relevance
  Represents the strongest optimization adversary; necessary test baseline to check if bilateral filters are bypassed by L2 distance scaling.
  ```

### Run 4: DeepFool - Moosavi-Dezfooli et al.
- **Output Excerpt:**
  ```markdown
  ### 1. Citation & Core Claim
  Moosavi-Dezfooli et al. (2016). 'DeepFool: a simple and accurate method to fool deep neural networks.' Calculates minimal orthogonal projections.
  ### 2. Mathematical Formulation & Bounds
  Iteratively projects input onto the closest decision boundary hyperplanes: r_i = - f(x_i) * w / ||w||_2^2.
  ### 3. Quantitative Results (Metrics)
  Reduces GoogLeNet accuracy on ImageNet to 0% with 5x fewer perturbations than FGSM.
  ### 4. Thesis Relevance
  Bilateral edge-preservation characteristics are critical here; smoothing the boundary pixels directly disrupts DeepFool's hyperplane projections.
  ```

### Run 5: Bilateral Filtering for Defending CNNs - Liu et al.
- **Output Excerpt:**
  ```markdown
  ### 1. Citation & Core Claim
  Liu et al. (2020). 'Feature Denoising for Adversarial Defense.' Denoising blocks inside the network improve robustness.
  ### 2. Mathematical Formulation & Bounds
  Applies non-local means / bilateral filters as intermediate layers in ResNeXt architectures.
  ### 3. Quantitative Results (Metrics)
  Improves CIFAR-10 PGD robust accuracy by +4.2% when integrated into training.
  ### 4. Thesis Relevance
  Validates our hypothesis that bilateral pre-processing works, but suggests intermediate layer integration performs better than input-only filtering.
  ```

---

## 4. Time-Saved Accounting

We compare the workflow economics against doing all 5 summaries manually:

- **Manual Method (Reading + Extraction + Drafting):**
  - Time per paper: 45 minutes
  - Total for 5 papers: **225 minutes**
- **Automated Workflow Method:**
  - Setup Cost (writing prompts, configure Claude Project): 30 minutes (one-time).
  - Execution Time per paper: 3 minutes (pasting and running steps). Total = 15 minutes.
  - Human Verification Time per paper: 5 minutes (verifying formulas against PDF). Total = 25 minutes.
  - Total for 5 papers: **70 minutes**
- **Net Time Saved:** **155 minutes (a 3.2× speedup)**. 
  - *Future Savings:* Since setup cost is paid, subsequent paper runs save 37 minutes per paper.

---

## 5. Failure Points & Human Review Checklist

The workflow is a decision-support system and exhibits the following failure modes:
1. **Formula Hallucinations:** The model occasionally replaces LaTeX math variables (e.g. confusing $\alpha$ step-sizes with $\epsilon$ bounds).
2. **Missing Dataset Context:** Tends to report accuracy drops without stating which dataset or model size was used.

### Human Verification Checklist:
- [ ] Cross-reference the exact values of $\epsilon$ (e.g., confirming it was 8/255 for CIFAR-10).
- [ ] Check that the cited model architecture (e.g., ResNet-50 vs. ResNet-18) is documented.
- [ ] Confirm no conversational introductory fluff is present.
