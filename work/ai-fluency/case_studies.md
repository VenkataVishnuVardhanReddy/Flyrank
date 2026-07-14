# Portfolio Case Studies & Voice Card

This document contains the voice card, case studies matching the sitemap structure, the professional bio, and a before/after copywriting audit.

---

## 1. Voice Card
> **"Mathematically rigorous, concise, direct, transparent, plain."** (6 words)

---

## 2. Before / After Copywriting Audit

- **Before (Generic AI Sludge)**:
  > *“As a results-driven machine learning engineer, I leverage state-of-the-art predictive modeling pipelines to systematically optimize digital content refresh schedules and maximize organic search traffic synergies.”*
- **After (My Edited Version)**:
  > *“I train Random Forest models to rank content refresh priorities by predicting future traffic decline. The system achieves a 74% Precision@50, tripling the accuracy of static rules.”*

---

## 3. Case Studies (Three Beats)

### Case Study 1: FlyRank Search Telemetry & Refresh Opportunity Scoring
- **The Problem**: 
  Content editors waste hundreds of hours manually auditing articles for ranking decay. Blunt, static rules—like "refresh every page older than 180 days"—miss critical new pages in decay while wasting budget updating older, stable pages.
- **What I Did & Decided**: 
  I built a machine learning-based priority ranking model (Random Forest) that fuses Google Search Console visibility indicators and Google Analytics 4 scroll/engagement rates. I decided to enforce a strict client-holdout validation strategy during model training to ensure the ranking generalizes to unseen client domains, and optimized the model on Precision@50 to align with weekly editorial review capacity.
- **What Came of It**: 
  Achieved a Precision@50 of **74.0%**, delivering a **~3x lift** over standard static rules (which only get 24.0% of recommendations right). This ensures that 37 out of the top 50 recommended pages are indeed in decline, saving significant editorial budget.

### Case Study 2: SecureDrive-CV: Real-Time Perception Shielding
- **The Problem**: 
  Autonomous vehicle perception models are vulnerable to adversarial pixel perturbations (FGSM/PGD attacks), which manipulate traffic sign markings and cause fatal classification bypasses at the edge.
- **What I Did & Decided**: 
  I developed an edge-compatible bilateral filter shield that sanitizes camera frames before inputting them to the classifier. I decided to stream zero-storage, clean test datasets to perform a robustness sweep and track real-time SSIM recovery factor under Swedish ISO 21448 standards.
- **What Came of It**: 
  Recovered classifier accuracy from **12.0%** under attack back to **98.1%** (SSIM recovery factor of `1.000`), outputting telemetry to a custom Streamlit robustness console.

### Case Study 3: Sovereign-Shield: Secure Enterprise AI Gateway
- **The Problem**: 
  Direct LLM deployments in enterprise environments lack robust defenses against prompt injection attacks and real-time compliance logging for data protection.
- **What I Did & Decided**: 
  Built a secure, multi-tenant API gateway using FastAPI, Redis caching, Celery workers, and PostgreSQL. I decided to implement a Gemini-RAG compliance reporter for automated NIS2 compliance auditing.
- **What Came of It**: 
  Mitigated prompt injection risks and automated NIS2 compliance auditing across **10,000+ test queries**, maintaining sub-100ms routing latency.

---

## 4. Bio & Contact/CTA Copy

- **Bio**: 
  I am Venkata Vishnu Vardhan Reddy, a graduate student and AI Safety & Perception Engineer. I design, audit, and secure machine learning systems—ranging from computer vision defense filters to search intelligence ranking models.
- **Contact/CTA**: 
  **[Book a 15-Minute Technical Demo of the Telemetry Console]**
