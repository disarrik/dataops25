from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict():
    return {"prediction": 0}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
