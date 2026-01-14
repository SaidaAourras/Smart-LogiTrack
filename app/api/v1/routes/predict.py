from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db
from app.services.auth_services import verify_token
from app.db.models.eta_predictions import ETAPrediction
from app.db.models.user import User
from app.utils.init_spark import init_spark
from pyspark.ml import PipelineModel
import os
from app.api.v1.schemas.trip_features import TripFeatures


predict_router = APIRouter(prefix="/predict", tags=["Prediction"])

spark = init_spark()

MODEL_PATH = os.path.join(os.getcwd(), "ml/models/eta_spark")
print("MODEL_PATH =", MODEL_PATH)
print("Exists =", os.path.exists(MODEL_PATH))


loaded_model = PipelineModel.load(MODEL_PATH)



@predict_router.post("/")
def predict_eta(
    payload: TripFeatures,
    db: Session = Depends(get_db),
    current_user: User = Depends(verify_token)
):
    """
    Entrée : features du trajet (JSON)
    Sortie : { "estimated_duration": 12.5 }
    """

    features = spark.createDataFrame(
        [(
            payload.trip_distance,
            payload.RatecodeID,
            payload.tolls_amount,
            payload.fare_amount,
            payload.tip_amount,
            payload.total_amount,
            payload.Airport_fee,
            payload.pickup_hour,
            payload.day_of_week
        )],
    [
        'trip_distance',
        'RatecodeID',
        'tolls_amount',
        'fare_amount',
        'tip_amount',
        'total_amount',
        'Airport_fee',
        'pickup_hour',
        'day_of_week'
    ])
    predictions = loaded_model.transform(features)

    predicted_duration = predictions.select("prediction").collect()[0]["prediction"]

    prediction = ETAPrediction(
        user_id=current_user.get("sub"),
        predicted_duration=float(predicted_duration),
        **payload.model_dump()
    )

    db.add(prediction)
    db.commit()

    return {"estimated_duration": predicted_duration}
