from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_health(): assert c.get('/api/health').status_code==200
def test_risk(): assert 0<=c.get('/api/risk').json()['risk']<=100
def test_slices(): assert len(c.get('/api/slices').json())>=4
def test_scenario(): assert 'risk_after' in c.post('/api/scenarios/ddos_control_plane').json()
def test_reset(): assert c.post('/api/reset').status_code==200
