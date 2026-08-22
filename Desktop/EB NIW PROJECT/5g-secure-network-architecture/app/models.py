from sqlalchemy import Integer,String,Float,Boolean
from sqlalchemy.orm import Mapped,mapped_column
from .database import Base
class Controller(Base):
 __tablename__='controllers'; id:Mapped[int]=mapped_column(Integer,primary_key=True); name:Mapped[str]=mapped_column(String); trust:Mapped[float]=mapped_column(Float); load:Mapped[float]=mapped_column(Float); availability:Mapped[float]=mapped_column(Float); status:Mapped[str]=mapped_column(String)
class Slice(Base):
 __tablename__='slices'; id:Mapped[int]=mapped_column(Integer,primary_key=True); name:Mapped[str]=mapped_column(String); service:Mapped[str]=mapped_column(String); criticality:Mapped[int]=mapped_column(Integer); isolation:Mapped[float]=mapped_column(Float); latency:Mapped[float]=mapped_column(Float); trust:Mapped[float]=mapped_column(Float)
class Edge(Base):
 __tablename__='edges'; id:Mapped[int]=mapped_column(Integer,primary_key=True); name:Mapped[str]=mapped_column(String); location:Mapped[str]=mapped_column(String); trust:Mapped[float]=mapped_column(Float); visibility:Mapped[float]=mapped_column(Float); status:Mapped[str]=mapped_column(String)
class Flow(Base):
 __tablename__='flows'; id:Mapped[int]=mapped_column(Integer,primary_key=True); name:Mapped[str]=mapped_column(String); verified:Mapped[bool]=mapped_column(Boolean); digest:Mapped[str]=mapped_column(String)
class Event(Base):
 __tablename__='events'; id:Mapped[int]=mapped_column(Integer,primary_key=True); category:Mapped[str]=mapped_column(String); severity:Mapped[str]=mapped_column(String); title:Mapped[str]=mapped_column(String); target:Mapped[str]=mapped_column(String); risk:Mapped[float]=mapped_column(Float); description:Mapped[str]=mapped_column(String)
