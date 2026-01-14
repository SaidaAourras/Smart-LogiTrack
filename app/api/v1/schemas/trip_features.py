from pydantic import BaseModel

class TripFeatures(BaseModel):
    trip_distance: float
    RatecodeID: int
    tolls_amount: float
    fare_amount: float
    tip_amount: float
    total_amount: float
    Airport_fee: float
    pickup_hour: int
    day_of_week: int
