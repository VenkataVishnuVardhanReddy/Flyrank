# Portfolio Flagship: Domain & Analytics Launch

This document details the final launch settings, custom domain fallback routes, the privacy-preserving analytics configuration, and the verification badge integrations.

---

## 1. Domain Configuration
- **Live URL:** **[https://venkatavishnuvardhanreddy.github.io/Flyrank/](https://venkatavishnuvardhanreddy.github.io/Flyrank/)**
  - *HTTPS Security:* Encrypted under GitHub's automatic SSL wildcard certificate framework.
  - *Domain Strategy:* Uses the clean GitHub Pages repository mapping fallback, ready to instantly swap with your custom FlyRank subdomain (`vishnu.flyrank.ai`) once the graduation registry updates.

---

## 2. Web Analytics Configuration

We wired **GoatCounter**—a free, open-source, GDPR-compliant web analytics dashboard that requires zero tracking cookies and loads asynchronously without blocking page rendering speed.

### Embedded Analytics Tag:
```html
<script data-goatcounter="https://vishnu-flyrank.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

- **Analytics Dashboard URL:** `https://vishnu-flyrank.goatcounter.com`
- **Captured Telemetry:** Tracks aggregate page views, referrer links, screen resolution bins, and country of origin without storing personal data, matching safety compliance criteria.

---

## 3. Social-Share & Favicon Hygiene
- **Page Title:** *Prioritizing Content Refreshes for Organic Traffic Recovery | FlyRank Capstone*
- **Social Sharing Preview:** Verified utilizing social preview debuggers. Displays the Gini feature importance chart and the correct 3-sentence summary in messaging cards (Discord, Slack, LinkedIn).
- **Graduate Badge:** Embedded in the footer, displaying the shields.io indigo "FlyRank Certified Graduate" indicator linking directly to the verified page: `https://internship.flyrank.ai/verify/venkatavishnuvardhanreddy`.
