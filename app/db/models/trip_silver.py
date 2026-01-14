from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class TripSilver(Base):
    """
    Table Silver - Données nettoyées + Features pour ML
    Contient UNIQUEMENT les colonnes utilisées pour l'entraînement du modèle
    """
    __tablename__ = 'silver_data'
    __table_args__ = {'extend_existing': True}
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Foreign Key vers Bronze (traçabilité)
    bronze_id = Column(Integer, ForeignKey('trips_bronze.id', ondelete='CASCADE'), 
                       unique=True, nullable=False, index=True)
    
    # ========== FEATURES UTILISÉES DANS LE MODÈLE ML ==========
    # Colonnes originales conservées
    trip_distance = Column(Float, nullable=False)
    RatecodeID = Column(Integer, nullable=False)
    tolls_amount = Column(Float, nullable=False, default=0.0)
    fare_amount = Column(Float, nullable=False)
    tip_amount = Column(Float, nullable=False, default=0.0)
    total_amount = Column(Float, nullable=False)
    Airport_fee = Column(Float, nullable=False, default=0.0)
    
    # Features engineered (créées depuis tpep_pickup_datetime)
    pickup_hour = Column(Integer, nullable=False, index=True)  # 0-23
    day_of_week = Column(Integer, nullable=False, index=True)  # 0=Lundi, 6=Dimanche
    
    # ========== COLONNES ADDITIONNELLES POUR ANALYTICS ==========
    pickup_datetime = Column(DateTime, nullable=False, index=True)
    dropoff_datetime = Column(DateTime, nullable=False)
    trip_duration = Column(Float, nullable=False)  # En minutes (TARGET pour ML)
    payment_type = Column(Integer, index=True)
    
    # Métadonnées
    created_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relation avec Bronze
    bronze_trip = relationship("TripBronze", back_populates="silver_trip")