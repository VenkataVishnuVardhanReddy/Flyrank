# Tech Stack Decision: Three Roads

This document outlines the architectural constraints, the three technology stack options considered, and the final rationale for selecting a static HTML/CSS stack hosted on GitHub Pages.

---

## 1. Architectural Constraints

1. **Free Only:** Zero deployment or hosting budget; must rely on free hobby-tier platforms.
2. **Skill Level:** Proficient in Python, C/C++, and machine learning architectures, with basic/moderate knowledge of frontend design (HTML, CSS, basic JS).
3. **Portfolio Requirements:** Must host an academic research paper, tabular data, metric charts, code repository links, and embed a Calendly meeting scheduler.
4. **Dynamic Requirements:** No backend database required yet; static performance telemetry and simple embeds are sufficient for initial verification.

---

## 2. The Three Stack Options

### Option 1: Static HTML5 + Vanilla CSS (Simplest)
- **How to Build:** Write clean semantic HTML and a custom, responsive stylesheet.
- **Where to Host:** GitHub Pages (free).
- **Backend Needed:** No.
- **Trade-off:** High load speeds, zero build dependencies, and zero maintenance. However, lacks modular components (e.g. duplicating headers/footers if split across multiple files).

### Option 2: Astro Static Site Generator + Tailwind CSS (Medium)
- **How to Build:** Use Astro components for layout modularity and Tailwind utility classes for styling.
- **Where to Host:** Netlify or Vercel (free).
- **Backend Needed:** No.
- **Trade-off:** Highly modular page building and rapid styling. However, introduces local Node.js setup, package manager dependency overhead, and requires learning Astro's syntax.

### Option 3: Next.js + React + Tailwind + Streamlit Embed (Most Powerful)
- **How to Build:** Develop a full React web application in Next.js, hosting the perception defense filters as interactive front-end components.
- **Where to Host:** Vercel (free).
- **Backend Needed:** Not yet (can scale to serverless API routes later).
- **Trade-off:** Maximum interaction potential, custom telemetry dashboarding, and path to scale. However, very high framework complexity, high build maintenance overhead, and easy to break during major Next.js version upgrades.

---

## 3. Final Decision & Rationale

**Chosen Stack:** **Option 1: Static HTML5 + Vanilla CSS served on GitHub Pages**

**Alternatives Rejected:**
- *Next.js (Option 3):* Rejected due to excessive complexity. For an academic research portfolio, Next.js is overkill. It distracts engineering focus away from the core machine learning and safety telemetry algorithms.
- *Astro (Option 2):* Rejected because the sitemap fits perfectly on a single, continuous, beautifully-structured data report. We do not need complex component routing.

**Discernment & Maintainability:**
As an AI safety and perception engineer, my portfolio's target lead (automotive safety director) values clean data, transparent validation, and mathematical rigor—not complex frontend framework animations. A static, single-page academic paper served directly from the repository is lightweight, has zero deployment dependencies, and requires zero package maintenance over time. It will never break due to package updates or API deprecations, ensuring 100% long-term durability.
