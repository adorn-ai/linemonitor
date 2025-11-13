from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)

class AirflowInstance(Base):
    __tablename__ = "airflow_instances"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    base_url = Column(String, nullable=False)
    encrypted_username = Column(String, nullable=True)
    encrypted_password = Column(String, nullable=True)
    token_encrypted = Column(String, nullable=True)

    user = relationship("User", backref="instances")

class Pipeline(Base):
    __tablename__ = "pipelines"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    airflow_dag_id = Column(String, nullable=False)
    last_status = Column(String, nullable=True)
    last_run_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", backref="pipelines")

class PipelineRun(Base):
    __tablename__ = "pipeline_runs"
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"))
    run_id = Column(String, nullable=False)
    status = Column(String, nullable=False)
    raw_payload = Column(Text)

    pipeline = relationship("Pipeline", backref="runs")
