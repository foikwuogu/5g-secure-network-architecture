from pathlib import Path
from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import Base,engine,SessionLocal,get_db
from .models import Controller,Slice,Edge,Flow,Event
from .engine import seed,risk,scenario
Base.metadata.create_all(engine);app=FastAPI(title='5G Secure Network Architecture',version='1.0.0')
@app.on_event('startup')
def startup():
 db=SessionLocal();seed(db);db.close()
@app.get('/',include_in_schema=False)
def home(): return FileResponse(Path(__file__).parent/'static/index.html')
@app.get('/api/health')
def health(): return {'status':'ok'}
@app.get('/api/risk')
def getrisk(db:Session=Depends(get_db)): return risk(db)
@app.get('/api/controllers')
def controllers(db:Session=Depends(get_db)): return db.scalars(select(Controller)).all()
@app.get('/api/slices')
def slices(db:Session=Depends(get_db)): return db.scalars(select(Slice)).all()
@app.get('/api/edges')
def edges(db:Session=Depends(get_db)): return db.scalars(select(Edge)).all()
@app.get('/api/flows')
def flows(db:Session=Depends(get_db)): return {'total':len(list(db.scalars(select(Flow)))),'verified':sum(x.verified for x in db.scalars(select(Flow)).all())}
@app.get('/api/events')
def events(db:Session=Depends(get_db)): return db.scalars(select(Event).order_by(Event.id.desc()).limit(20)).all()
@app.post('/api/scenarios/{name}')
def run(name:str,db:Session=Depends(get_db)):
 try:return scenario(db,name)
 except KeyError:raise HTTPException(404,'Unknown scenario')
@app.post('/api/reset')
def reset(db:Session=Depends(get_db)):
 for cls in (Event,Flow,Controller,Slice,Edge): db.query(cls).delete()
 db.commit();seed(db);return risk(db)
