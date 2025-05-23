import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Railway!"}

if __name__ == "__main__":
    port = int(os.environ["PORT"])  # استخدم PORT مباشرة بدون قيمة افتراضية
    uvicorn.run(app, host="0.0.0.0", port=port)


