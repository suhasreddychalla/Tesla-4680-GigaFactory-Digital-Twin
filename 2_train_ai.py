import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("🧠 Loading 1 Million records into AI trainer...")
df = pd.read_csv('tesla_production_big_data.csv')

# Features: What the AI looks at | Target: What the AI predicts
X = df[['Laser_Weld_Power_kW', 'Weld_Time_ms', 'Internal_Resistance_mOhm', 'Jelly_Roll_Alignment_Error_mm']]
y = df['Is_Scrap']

# Split: 80% to learn, 20% to test its own knowledge
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("🚀 Training Random Forest model (this uses Big Data logic)...")
model = RandomForestClassifier(n_estimators=20, max_depth=10, n_jobs=-1)
model.fit(X_train, y_train)

# Save the model so you can show it on GitHub
joblib.dump(model, 'tesla_ai_model.pkl')
print(f"✅ AI Brain is ready! Accuracy: {round(model.score(X_test, y_test)*100, 2)}%")