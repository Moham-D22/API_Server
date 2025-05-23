import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Railway!"}

if _name_ == "_main_":
    port = int(os.environ["PORT"])
    uvicorn.run(app, host="0.0.0.0", port=port)
