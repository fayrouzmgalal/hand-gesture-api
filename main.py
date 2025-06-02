from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialize FastAPI app
app = FastAPI(title="Hand Gesture Classifier")

# Define the input data model
class LandmarkInput(BaseModel):
    landmarks: list[float]  # 42 floats (x1, y1, ..., x21, y21)

# Load the trained model
model_path = os.path.join("models", "RandomForest_hand_gesture_classifier.pkl")
try:
    model = joblib.load(model_path)
    print("Loaded model type:", type(model))
except Exception as e:
    raise RuntimeError(f"Failed to load the model: {e}")

# Load the label encoder (if available)
label_encoder_path = os.path.join("models", "label_encoder.pkl")
if os.path.exists(label_encoder_path):
    label_encoder = joblib.load(label_encoder_path)
else:
    label_encoder = None  # fallback to raw numeric prediction

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Hand Gesture Classifier API"}

# Prediction endpoint
@app.post("/predict")
def predict(input_data: LandmarkInput):
    try:
        landmarks = input_data.landmarks

        if len(landmarks) != 42:
            raise HTTPException(status_code=400, detail="Expected 42 values (x1, y1, ..., x21, y21)")

        input_array = np.array(landmarks).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        if label_encoder:
            prediction = label_encoder.inverse_transform([prediction])[0]
            return {"prediction": str(prediction)}
        else:
            return {"prediction": int(prediction)}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
