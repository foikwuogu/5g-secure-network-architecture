import hashlib,json
from sqlalchemy import select
from .models import Controller,Slice,Edge,Flow,Event

def seed(db):
 if db.scalar(select(Controller.id).limit(1)): return
 for x in [('SDN-C1',92,28,99),('SDN-C2',95,25,99)]: db.add(Controller(name=x[0],trust=x[1],load=x[2],availability=x[3],status='healthy'))
 for x in [('URLLC-CRITICAL','URLLC',100,96,5,94),('eMBB-PUBLIC','eMBB',60,91,20,82),('mMTC-IOT','mMTC',75,83,30,76),('PRIVATE-5G','Private',85,89,15,88)]: db.add(Slice(name=x[0],service=x[1],criticality=x[2],isolation=x[3],latency=x[4],trust=x[5]))
 for x in [('EDGE-01','Plant-A',92,94),('EDGE-02','Plant-B',84,88),('EDGE-03','Remote-A',65,61),('EDGE-04','Hospital-A',95,96)]: db.add(Edge(name=x[0],location=x[1],trust=x[2],visibility=x[3],status='healthy'))
 db.commit()
 for s in db.scalars(select(Slice)).all(): db.add(Flow(name=s.name+'-baseline',verified=True,digest=hashlib.sha256((s.name+'ALLOW').encode()).hexdigest()))
 db.commit()

def risk(db):
 c=list(db.scalars(select(Controller))); s=list(db.scalars(select(Slice))); e=list(db.scalars(select(Edge))); f=list(db.scalars(select(Flow)))
 cr=sum((100-x.trust)*.5+x.load*.25+(100-x.availability)*.25 for x in c)/len(c)
 sr=sum((100-x.isolation)*.4+(100-x.trust)*.35+x.criticality*.15 for x in s)/len(s)
 er=sum((100-x.trust)*.5+(100-x.visibility)*.5 for x in e)/len(e)
 ir=sum(not x.verified for x in f)/len(f)*100
 return {'risk':round(max(0,min(100,.4*cr+.35*sr+.2*er+.05*ir)),2),'zero_trust':round(sum(x.trust for x in c)/len(c)*.5+sum(x.trust for x in s)/len(s)*.5,2),'isolation':round(sum(x.isolation for x in s)/len(s),2),'visibility':round(sum(x.visibility for x in e)/len(e),2),'pqc_readiness':88}

def scenario(db,n):
 before=risk(db)['risk']; c=list(db.scalars(select(Controller)));s=list(db.scalars(select(Slice)));e=list(db.scalars(select(Edge)));f=list(db.scalars(select(Flow)));lat=0
 if n=='ddos_control_plane':
  [setattr(x,'load',min(100,x.load+50)) or setattr(x,'availability',max(50,x.availability-25)) for x in c];lat=3.8;title='Synthetic control-plane DDoS'
 elif n=='mitm':
  [setattr(x,'trust',max(20,x.trust-25)) for x in c+s];lat=1.8;title='Synthetic MITM condition'
 elif n=='slice_hopping':
  [setattr(s[1],'isolation',max(25,s[1].isolation-50)),setattr(s[0],'trust',max(30,s[0].trust-15))];lat=2.2;title='Synthetic slice hopping'
 elif n=='cross_slice': [setattr(x,'isolation',max(30,x.isolation-25)) for x in s];lat=2.7;title='Synthetic cross-slice exposure'
 elif n=='edge_compromise':
  [setattr(x,'trust',max(20,x.trust-35)) or setattr(x,'visibility',max(20,x.visibility-30)) or setattr(x,'status','degraded') for x in e if x.location in ('Plant-B','Remote-A')];lat=2.5;title='Synthetic edge compromise'
 elif n=='apt_lateral_movement':
  [setattr(x,'trust',max(15,x.trust-20)) for x in c+s];lat=3.0;title='Synthetic APT lateral movement'
 elif n=='controller_compromise':
  c[0].status='compromised';c[0].trust=20;c[0].availability=45;[setattr(x,'verified',False) for x in f];lat=4.5;title='Synthetic SDN controller compromise'
 elif n=='adaptive_mitigation':
  [setattr(x,'load',max(20,x.load-20)) or setattr(x,'availability',min(100,x.availability+8)) or setattr(x,'trust',min(100,x.trust+10)) for x in c];[setattr(x,'isolation',min(100,x.isolation+12)) or setattr(x,'trust',min(100,x.trust+10)) for x in s];[setattr(x,'visibility',min(100,x.visibility+8)) for x in e];[setattr(x,'verified',True) for x in f];lat=4;title='Synthetic adaptive mitigation'
 elif n=='baseline': title='Baseline'
 else: raise KeyError(n)
 db.add(Event(category=n,severity='CRITICAL' if n not in ('baseline','adaptive_mitigation') else 'INFO',title=title,target='synthetic 5G/SDN',risk=0,description='Simulator-only state change; no network command was issued.'));db.commit();after=risk(db)['risk']; reduction=max(0,before-after); eff=round(reduction/max(before,.01)*100,2)
 return {'scenario':n,'risk_before':before,'risk_after':after,'risk_reduction_percent':eff,'latency_overhead_percent':lat,'human_review_required':True}
