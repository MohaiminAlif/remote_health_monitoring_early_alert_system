import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the dataset
df = pd.read_csv("train_data.csv")

# Select features
X = df[['heart_rate', 'temperature', 'spo2']]

# Debug info
print("Preview of data:\n", X.head())
print("Data types:\n", X.dtypes)
print("Missing values:\n", X.isnull().sum())

# Clean the data
X = X.dropna()
X = X.astype(float)

# Train the model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Save the model
joblib.dump(model, "health_anomaly_model.pkl")

print("✅ Model trained and saved as health_anomaly_model.pkl")
