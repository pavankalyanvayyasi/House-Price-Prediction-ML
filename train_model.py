
import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the dataset
df = pd.read_csv("dataset/house_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# 2. Separate input features and target
X = df[
    [
        "area_sqft",
        "bedrooms",
        "bathrooms",
        "year_built",
        "location"
    ]
]

y = df["price"]

# 3. Identify numerical and categorical columns
numerical_features = [
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "year_built"
]

categorical_features = ["location"]

# 4. Convert location text into numerical values
preprocessor = ColumnTransformer(
    transformers=[
        (
            "location_encoder",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# 5. Create the ML pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)

# 6. Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# 7. Train the model
model.fit(X_train, y_train)

print("\nModel training completed!")

# 8. Predict prices for test data
y_pred = model.predict(X_test)

# 9. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R2 Score:", round(r2, 4))

# 10. Save the trained model
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/house_price_model.pkl")

print("\nModel saved successfully!")
print("Saved at: model/house_price_model.pkl")
