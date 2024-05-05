from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__)

@app.route('/train', methods=['GET'])
def train_model():
    data = pd.read_csv('data.csv')
    
    # Features Selection
    features = [
        "currentRatio", "quickRatio", "cashRatio", "grossProfitMargin",
        "operatingProfitMargin", "returnOnAssets", "returnOnEquity",
        "debtRatio", "debtEquityRatio", "interestCoverage"
    ]
    
    # Separating features and target
    X = data[features]
    y = data['priceFairValue']
    
    # Handling missing values
    X = X.fillna(X.mean())
    
    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling the dataset
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test) 

    # Linear Regression model
    model = LinearRegression()
    
    # fitting the model
    model.fit(X_train_scaled, y_train)
    
    # making predictions on test set
    y_pred = model.predict(X_test_scaled)
    
    # Calculating R^2 and RMSE
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"R² score: {r2}")
    print(f"RMSE: {rmse}")
    
    # Return Response on training completion
    return f"Model training completed. R² score: {r2}, RMSE: {rmse}"

if __name__ == '__main__':
    app.run(debug=True)
