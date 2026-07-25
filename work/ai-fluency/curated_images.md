# Curated Images & Visual Discernment

This document details the portfolio's visual asset mapping, the decision log for choosing real captures over AI-generated placeholders, and the audit of a rejected generated asset.

---

## 1. Visual Asset Directory & Design Decisions

| Asset Name | Purpose | Selection Call | Rationale |
| :--- | :--- | :--- | :--- |
| **1. Monogram Logo** (`monogram.svg`) | Branding & header identity. | **Real Code** | Custom hand-crafted SVG code to ensure sharp vector scaling and clean rendering, avoiding any generic AI icon styling. |
| **2. Feature Importances Chart** (`feature_importances.png`) | Case study evidence. | **Real Capture** | A direct matplotlib export of the Gini feature importances from `capstone.ipynb`. A real chart carries scientific credibility that no generated chart can fake. |
| **3. Claude Workspace Config** (`claude_project_screenshot.png`) | Toolkit setup proof. | **Real Capture** | A cropped, high-contrast screenshot of the Claude AI Projects interface showing your actual workspace rules and custom instructions. |
| **4. Sitemap Sketch** (`portfolio_sitemap_sketch.png`) | Visual planning proof. | **Real Capture** | A photo of a physical grid-paper notebook sketch. It shows the real, raw planning phase before clean digital layout. |
| **5. Professional Headshot** (`profile_headshot.png`) | Personal bio identification. | **Real Photo** | A real, professional photo. Using an AI-generated portrait for a personal bio completely breaks trust with recruiters. |

---

## 2. Visual Discernment: Rejected Generated Asset

- **Rejected Asset Description**:
  An AI-generated abstract graphic showing a glowing blue shield grid blocking binary codes (representing the Bilateral filter perception shield for computer vision).
- **Why it was rejected (Discernment Audit)**:
  The generated image looked like generic tech stock art—slick, glowing, and completely devoid of domain-specific meaning. A recruiter or safety engineer in the autonomous vehicle space would immediately recognize it as a decorative placeholder. To establish technical authority, we rejected the generic graphic and replaced it with a **real matplotlib chart** displaying the actual classification recovery factor under active FGSM/PGD attacks. Concrete data visualizations prove technical skill; decorative AI graphics look like filler.
