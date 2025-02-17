import pandas as pd
from sklearn.ensemble import IsolationForest

# Sample transaction data
data = {'amount': [50, 20, 1000, 200, 5000, 30, 40000], 
        'type': ['debit', 'credit', 'debit', 'debit', 'credit', 'debit', 'debit']}

df = pd.DataFrame(data)

# Train fraud detection model
model = IsolationForest(contamination=0.2)
df['fraud_score'] = model.fit_predict(df[['amount']])

# Detect fraud
df['is_fraud'] = df['fraud_score'].apply(lambda x: "Yes" if x == -1 else "No")
print(df)
