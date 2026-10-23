# Student Result Prediction (MLOps Practical 10)

FastAPI service that predicts Pass/Fail from study hours, attendance and previous score.
Image is built/tested/pushed to GHCR by GitHub Actions (Practical-9) and deployed to Render (Practical-10).

## Endpoints
`/` root, `/health`, `/docs` (Swagger), `POST /predict`

## Run locally
    pip install -r requirements.txt
    python train.py
    uvicorn app:app --host 0.0.0.0 --port 8000

## Docker
    docker build -t student-result-prediction .
    docker run -p 8000:8000 student-result-prediction

## Deploy to Render
1. Push to `main`; wait for the workflow to publish `ghcr.io/<github-username>/student-result-prediction:latest`.
2. Render > New > Web Service > Existing Image; enter the image URL (add a GHCR credential with `read:packages` if the package is private).
3. Env var `PORT=8000`, health check path `/health`.
4. Test: `curl -X POST https://<service>.onrender.com/predict -H "Content-Type: application/json" --data @test_payload.json`
5. After a new push, use Manual Deploy > Deploy latest reference.
