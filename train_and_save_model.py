import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import joblib

df = pd.read_csv('cancer_data.csv')
df.columns = df.columns.str.strip()

df.drop(['index', 'Patient Id'], axis=1, inplace=True)

df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 2})

df['Level'] = df['Level'].replace({'Low': 0, 'Medium': 1, 'High': 2})

X = df.drop(columns=['Level'])
y = df['Level']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_scaled, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000, multi_class='ovr')
model.fit(X_train, y_train)

joblib.dump(model, 'lung_cancer_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("✅ Model and scaler saved successfully!")