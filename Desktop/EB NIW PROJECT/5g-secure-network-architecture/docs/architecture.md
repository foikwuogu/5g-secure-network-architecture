# Architecture

5G service layer -> network slices -> edge/VNF layer -> SDN data plane -> redundant SDN controllers -> security plane (Zero Trust, ML-ready anomaly detection, telemetry, flow integrity, PQC readiness) -> risk engine -> dashboard/API.

No real packets or control messages are sent.
