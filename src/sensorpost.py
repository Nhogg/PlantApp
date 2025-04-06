from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from uuid import uuid4

import google.generativeai as genai
from sensor_connect import sensor_request


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

class SoilMoistureRequest(BaseModel):
    moisture = sensor_request()

@app.post("/soil")
async def soil(request: SoilMoistureRequest):
    moisture = request.moisture
    if moisture > 200 and moisture < 300:
        return {"message": "You have been watered!"}
    else:
        return {"message": "You need to be watered!"}