from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class ETAPrediction(Base):
    __tablename__ = "eta_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Features utilisées pour la prédiction (celles de votre modèle)
    trip_distance = Column(Float, nullable=False)
    RatecodeID = Column(Integer, nullable=False)
    tolls_amount = Column(Float, nullable=False)
    fare_amount = Column(Float, nullable=False)
    tip_amount = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    Airport_fee = Column(Float, nullable=False)
    pickup_hour = Column(Integer, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    
    # Résultat de la prédiction
    predicted_duration = Column(Float, nullable=False)
    model_version = Column(String, default="v1.0")
    
    # Métadonnées
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relation
    user = relationship("User", back_populates="predictions")