from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/data")
def get_data():
    # Simulate load (100-500ms)
    time.sleep(random.uniform(0.1, 0.5))
    return {"data": "sample", "timestamp": time.time()}

@app.get("/api/process")
def process():
    # Simulate intensive load (500-2000ms)
    time.sleep(random.uniform(0.5, 2.0))
    return {"result": "processed", "timestamp": time.time()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
