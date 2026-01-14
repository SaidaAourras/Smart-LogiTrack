from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.v1.dependencies import get_db
from app.services.auth_services import verify_token

analytic_router = APIRouter(prefix="/analytics", tags=["Analytics"])


@analytic_router.post('/avg-duration-by-hour')
def avg_duration_by_hour(db: Session = Depends(get_db) , _ = Depends(verify_token)):
    sql_request = text("""
                       WITH hourly_trips AS (
                           SELECT pickup_hour , trip_duration
                           FROM silver_data
                           WHERE trip_duration IS NOT NULL
                       )
                       SELECT pickup_hour AS pickuphour , AVG(trip_duration) AS avg_duration
                       FROM hourly_trips
                       GROUP BY pickup_hour
                       ORDER BY pickup_hour;
    """)

    result = db.execute(sql_request).mappings().all()
    
    return result