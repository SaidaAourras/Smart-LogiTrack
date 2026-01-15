from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.v1.dependencies import get_db
from app.services.auth_services import verify_token

payment_analysis_router = APIRouter(prefix="/analytics", tags=["Analytics"])

@payment_analysis_router.get("/payment-analysis")
def payment_analysis(db: Session = Depends(get_db) , _=Depends(verify_token)):
    sql_request = text("""
        SELECT
            payment_type,
            COUNT(*) AS total_trips,
            AVG(trip_duration) AS avg_duration
        FROM silver_data
        WHERE trip_duration IS NOT NULL
        GROUP BY payment_type
        ORDER BY payment_type;
    """)

    result = db.execute(sql_request).mappings().all()

    return result

