import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(42)
n = 500
study_hours = rng.uniform(0, 10, n)
attendance = rng.uniform(40, 100, n)
prev_score = rng.uniform(30, 100, n)
score = 0.35 * study_hours * 10 + 0.25 * attendance + 0.4 * prev_score + rng.normal(0, 5, n)
y = (score >= 55).astype(int)
X = np.column_stack([study_hours, attendance, prev_score])

model = LogisticRegression(max_iter=1000).fit(X, y)
joblib.dump(model, "model/model.joblib")
print("Model saved. Train accuracy:", round(model.score(X, y), 3))
