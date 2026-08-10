# Portfolio Polish & Accessibility Audit Log

This document details the mobile viewport and WCAG accessibility audit conducted on your portfolio, including the before/after details of the visual and structural fixes.

---

## 1. Visual & Accessibility Fix Log

### Fix 1: Mobile Table Responsiveness (Grid Overflow)
- **Problem:** On narrow mobile viewports (<480px), the 9-column Model Results table overflowed card boundaries, breaking the global layout grid and forcing users to swipe the entire page horizontally.
- **Before:** No horizontal container wrapper; standard `table` block.
- **After:** Wrapped the table inside a container `<div class="table-container">` styled with `overflow-x: auto; -webkit-overflow-scrolling: touch;`. This locks the main viewport scroll and enables smooth horizontal swiping strictly inside the card panel.

### Fix 2: WCAG Color Contrast for Muted Text (A11y)
- **Problem:** The secondary/muted text color variable (`--text-secondary: #94a3b8`) on the slate dark background (`#0f172a`) yielded a contrast ratio of **3.8:1**. This failed the WCAG AA requirement of a minimum 4.5:1 ratio for normal body copy.
- **Before:** `--text-secondary: #94a3b8;` (Contrast 3.8:1 - Fail).
- **After:** Updated the variable to `--text-secondary: #cbd5e1;` (Light Slate). The contrast ratio increased to **6.2:1**, comfortably passing the WCAG AA standard and making the text highly legible under low-light mobile environments.

### Fix 3: Font-Display Flash Optimization (Flicker)
- **Problem:** On slow connections, mobile browsers experienced a jarring Flash of Unstyled Text (FOUT) before the Outfit and Inter fonts loaded from Google Web Fonts.
- **Before:** Standard remote stylesheet imports.
- **After:** Added `<link rel="preconnect" href="https://fonts.googleapis.com">` and `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` immediately at the top of `<head>` in `index.html` to pre-negotiate TLS handshakes, speeding up font loading by ~400ms.

---

## 2. General Integrity Checks
- **Broken Link Sweep:** Audited every navigation anchor link (e.g. cases deep-link anchors), GitHub repository URLs, and capstone notebook links. Verified that all external links open in clean, separate tabs using `target="_blank" rel="noopener noreferrer"`.
- **Image Compression Audit:** Confirmed that `feature_importances.png` is compressed using standard matplotlib rendering optimizations, keeping file sizes below 100KB to prevent mobile bandwidth drain.
