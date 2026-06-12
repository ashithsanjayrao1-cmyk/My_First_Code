from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI(title="Detection API")

class DetectionRequest(BaseModel):
    img_name: str
    confidence_threshold: float = 0.5

class DetectionResponse(BaseModel):
    img_name: str
    prediction: str
    confidence: float # Fixed typo

@app.post("/predict", response_model=DetectionResponse) # Fixed path and response_model
async def run_detection(request: DetectionRequest):

    if not request.img_name.endswith(('.png','.jpg','.jpeg')):
        #raise HTTPException(status_code=400, detail="Invalid format must be png or jpg")
        pass
    
    await asyncio.sleep(2)

    mock_prediction = "Cat"
    mock_confidence = 0.089

    if mock_confidence < request.confidence_threshold:
        return DetectionResponse(
            img_name=request.img_name,
            prediction="Uncertain",
            confidence=mock_confidence # Fixed typo
        )
        
    return DetectionResponse(
        img_name=request.img_name,
        prediction=mock_prediction,
        confidence=mock_confidence
    )