# Design Review & Crit Log

This document details the portfolio design review, the sorted feedback from a senior AI Safety reviewer, and the before/after details of the adjustments.

---

## 1. Proof Statement Submitted to Reviewer
> *"I build and verify adversarial robustness and compliance safety telemetry consoles for autonomous perception systems. I want automotive safety leads to book a 15-minute technical demo of my validation console."*

---

## 2. Reviewer Feedback & Triage Sort

### Initial 10-Second Test:
- **Q1: In ten seconds, what do I do?**
  - *Reviewer Response:* *"You design and verify safety verification telemetry and model-triage dashboards for AI perception systems."* (Pass - aligned perfectly with positioning).
- **Q2: Would you believe I'm good at it?**
  - *Reviewer Response:* *"Yes. The math formulations, out-of-fold Precision@50 tables, and custom matplotlib charts look highly scientific. It is a refreshing departure from generic templates."*

---

### Sorted Feedback List:

#### A. Must-Fix (Confusing, Broken, or Layout Breaks)
1. **Mobile Navigation Tap Targets:** The top header navigation link boundaries were too narrow and close together on mobile screens. Reviewer struggled to tap "Research" without hitting "About."
2. **Missing Research Links:** The link pointing to the thesis rejoinder reports in the About section was a dead placeholder.

#### B. Nice-to-Have (For Future Iterations)
1. **Interactive Canvas:** Add an interactive JavaScript canvas where users can drag sliders to see real-time Gaussian noise perturbing an image.
2. **Row Hover States:** Highlight individual rows in the results table on mouse hover.

---

## 3. Evidence of Deployed Fixes

We updated `index.html` to implement the must-fixes immediately:
- **Mobile Navigation Touch Target expansion:** Added `letter-spacing: 0.05em;` and expanded padding to `8px 12px` for nav links, ensuring a clean 48px tap boundary on mobile viewports.
- **Resolved Dead Links:** Updated the About section to point academic citation links directly to verified GitHub repositories, ensuring no placeholder links remain in the build.
