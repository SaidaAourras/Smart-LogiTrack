from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base



class TripBronze(Base):
    """
    Table Bronze - Données brutes NYC Taxi (toutes les colonnes originales)
    """
    __tablename__ = 'bronze_data'
    __table_args__ = {'extend_existing': True}
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Colonnes originales du dataset NYC Taxi
    VendorID = Column(Integer)
    tpep_pickup_datetime = Column(DateTime, nullable=False)
    tpep_dropoff_datetime = Column(DateTime, nullable=False)
    passenger_count = Column(Integer)
    trip_distance = Column(Float)
    RatecodeID = Column(Integer)
    store_and_fwd_flag = Column(String(1))  # 'Y' ou 'N'
    PULocationID = Column(Integer)  # Pickup Location ID
    DOLocationID = Column(Integer)  # Dropoff Location ID
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    improvement_surcharge = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    Airport_fee = Column(Float)
    cbd_congestion_fee = Column(Float)
    
    # Métadonnées
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relation avec Silver (1 Bronze → 1 Silver)
    silver_trip = relationship("TripSilver", back_populates="bronze_trip", uselist=False, cascade="all, delete-orphan")