from sqlalchemy import  create_engine, String, Column, Integer, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Clientes(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)



class PipelineCheckpoint(Base):
    __tablename__ = "pipeline_checkpoints"

    pipeline_name= Column(String(100), primary_key=True)
    last_update_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)