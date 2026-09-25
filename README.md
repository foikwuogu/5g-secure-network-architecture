# 5G Secure Network Architecture — SDN Security Laboratory

Standalone synthetic research project aligned to the 2025 paper *Securing Software-Defined Networks (SDN) Against Emerging Cyber Threats in 5G and Future Networks – A Comprehensive Review*.

## Project authorship

This repository is aligned with the published review paper and its research authorship. The project author attribution is as follows:

- David Olufemi — Department of Computer Science & Engineering, University of Fairfax, USA
- Ayodeji Olutosin Ejiade — Department of Computer, Texas Tech University, USA
- Friday Ogochukwu Ikwuogu — Department of Computer Science, University of Texas Permian Basin, Texas, USA
- Phebe E. Olufemi — Ahmadu Bello University, Zaria, Nigeria
- Deligent Bobie-Ansah — Information and Telecommunication Systems, Ohio University, United States

Friday Ogochukwu Ikwuogu
ORCID: 0009-0009-2222-1318
Google Scholar: https://scholar.google.com/citations?pli=1&authuser=3&user=XADxRNkAAAAJ
ResearchGate: https://www.researchgate.net/profile/Friday-O-Ikwuogu/research
GitHub: https://github.com/foikwuogu
Portfolio: Ikwuogufoikwuogu.github.io
LinkedIn: Ogochukwu Friday Ikwuogu
email: Friday.ikwuogu@gmail.com|ikwuogu_f57913@utpb.edu | ogochukwu.f.ikwuogu@ieee.org
Affiliation: Independent Researcher, Odessa, Texas, USA

Research record: [Zenodo DOI: 10.5281/zenodo.22866476](https://doi.org/10.5281/zenodo.22866476)

Paper reference:
- [ResearchGate publication](https://www.researchgate.net/publication/389946028_Securing_Software-Defined_Networks_SDN_Against_Emerging_Cyber_Threats_in_5G_and_Future_Networks_-A_Comprehensive_Review)
- Accessed: Sep 24, 2026

Features: SDN controllers, 5G network slices, edge nodes, Zero Trust posture, telemetry visibility, ML-ready anomaly/risk layer, flow-rule integrity ledger, PQC readiness, threat scenarios, adaptive mitigation, risk scoring, dashboard, REST API, Docker and tests.

Threat scenarios: DDoS/control-plane saturation, MITM, slice hopping, cross-slice attack, edge compromise, APT lateral movement, controller compromise, adaptive mitigation.

Safety: simulator only. No packet injection, exploit code, real 5G/RAN/core connection, OpenFlow control, credentials, carrier integration or autonomous production changes.

Run:
```bash
python -m venv .venv
# activate it
pip install -r requirements.txt
python -m pytest -q
python run.py
```
Open http://127.0.0.1:8004/ and API docs at http://127.0.0.1:8004/docs.

GitHub:
```bash
git init
git add .
git commit -m "Initial 5G SDN security laboratory"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/5g-secure-network-architecture.git
git push -u origin main
```
