# Build in Public: FlyRank Capstone

*Draft for LinkedIn / Twitter*

I just shipped my final capstone for the FlyRank AI Internship: a Machine Learning Content Refresh Prioritization Engine. 🚀

**The Problem:** Out of 30,000 unique URLs across 57 distinct brand portfolios, how does an editorial team decide which 50 pages to update this week to reverse organic traffic decay?

**The Build:** Using the FlyRank Search Performance Warehouse, I trained a Random Forest classifier on trailing 90-day search and engagement telemetry to predict future traffic drop-offs. The model achieved a 78.00% Precision@50 under strict GroupKFold validation, significantly outperforming standard SEO heuristics. 

**One Real Decision:** I actively chose Random Forest over a standard Logistic Regression baseline because search decay is highly non-linear. The data revealed that newer pages experience much sharper drop-offs than older, established legacy assets—an interaction threshold that linear models completely miss. 

**One Real Limitation:** While the model is highly accurate at identifying decay risk, it remains observational. It predicts which pages *will* drop, but it doesn't prove that executing a rewrite will causally recover that traffic. We use it as a highly efficient triage radar, not an automatic guarantee.

The entire project, from the validation notebooks to the fully deployed web portfolio, is live here: [https://venkatavishnuvardhanreddy.github.io/Flyrank/](https://venkatavishnuvardhanreddy.github.io/Flyrank/)

Built using AI as a true reasoning partner and co-founder, not just an autocomplete shortcut. 

#MachineLearning #SEO #DataScience #AIFluency #BuildInPublic
