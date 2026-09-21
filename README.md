# 5G Secure Network Architecture — SDN Security Laboratory

Standalone synthetic research project aligned to the 2025 paper *Securing Software-Defined Networks (SDN) Against Emerging Cyber Threats in 5G and Future Networks – A Comprehensive Review*.

Research record: [Zenodo DOI: 10.5281/zenodo.22866476](https://doi.org/10.5281/zenodo.22866476)

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
