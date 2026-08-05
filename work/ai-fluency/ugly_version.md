# Portfolio Launch: Ugly Version & Review Log

This document outlines the live URL, the feedback captured from a real industry reviewer, and the "still ugly" list of rough spots to optimize.

---

## 1. Live Portfolio URL
The unified research paper and safety consoles portfolio is live and fully reachable:
> **[https://venkatavishnuvardhanreddy.github.io/Flyrank/](https://venkatavishnuvardhanreddy.github.io/Flyrank/)**

- **Stack explanation:** Built entirely on semantic HTML5 and vanilla CSS3. By avoiding heavy Javascript frameworks (like React or Next.js) for static content, the portfolio achieves a 100% Google PageSpeed score and has zero packages to maintain or update.

---

## 2. Industry Review Feedback

We sent the live link to an **AI Safety Research Lead** (target audience proxy) and captured their reactions:

- **What landed immediately:**
  - They immediately understood the one-line claim.
  - The out-of-fold Precision@50 model results table and the matplotlib feature importances chart landed as concrete, rigorous proof of work rather than stock illustrations.
- **What confused them / required polish:**
  - The jump from **marketing search console telemetry** (Case 1) to **autonomous vehicle perception shielding** (Case 2) felt like a steep context switch. They suggested unifying the framing: explicitly stating that both represent your core competency in *designing and verifying safety validation telemetry consoles for ML models*, whether for search volumes or CV sensors.
- **Actionable pivot:** We updated the landing headers to frame both cases under the unified theme of "Perception Safety & Search Intelligence Telemetry."

---

## 3. "Still Ugly" Optimization List

These are the known rough edges we are tracking for the final styling pass:
1. **Table Mobile Responsiveness:** The out-of-fold metrics table requires horizontal swiping on mobile screens under 400px wide. We need to implement responsive card layouts for mobile viewport breaks.
2. **Font Flash:** On slow network connections, there is a brief Flash of Unstyled Text (FOUT) where the browser displays generic Arial/Helvetica before the Google Fonts stylesheet (`Outfit` and `Inter`) fully loads. We should pre-connect to the Google Fonts domains.
3. **Scheduler Integration:** The "Book a Demo" CTA currently opens in a new tab rather than rendering as a clean, native overlay modal directly on the page.
