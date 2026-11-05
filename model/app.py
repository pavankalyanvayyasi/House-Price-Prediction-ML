
import pandas as pd
from flask import Flask, render_template, request
import joblib
import os
import mysql.connector

app = Flask(__name__)

# Load trained ML model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "house_price_model.pkl")
model = joblib.load(MODEL_PATH)


# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="house_price_db"
    )


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Predict house price and save prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        area_sqft = float(request.form["area_sqft"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        year_built = int(request.form["year_built"])
        location = request.form["location"]

        house_data = pd.DataFrame([{
            "area_sqft": area_sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "year_built": year_built,
            "location": location
        }])

        predicted_price = float(model.predict(house_data)[0])
        price = round(predicted_price, 2)

        connection = get_db_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO prediction_history
            (area_sqft, bedrooms, bathrooms, year_built,
             location, predicted_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            area_sqft, bedrooms, bathrooms,
            year_built, location, price
        )

        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

        return render_template(
            "result.html",
            predicted_price=price,
            area_sqft=area_sqft,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            year_built=year_built,
            location=location
        )

    except Exception as error:
        return f"Prediction error: {error}", 400


# Prediction history
@app.route("/history")
def history():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM prediction_history
            ORDER BY created_at DESC
        """)

        records = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template(
            "history.html",
            records=records
        )

    except Exception as error:
        return f"Database error: {error}", 500


# Dashboard page
@app.route("/dashboard")
def dashboard():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                COUNT(*) AS total_predictions,
                AVG(predicted_price) AS average_price,
                MAX(predicted_price) AS highest_price,
                MIN(predicted_price) AS lowest_price
            FROM prediction_history
        """)
        stats = cursor.fetchone()

        cursor.execute("""
            SELECT
                location,
                COUNT(*) AS total,
                AVG(predicted_price) AS average_price
            FROM prediction_history
            GROUP BY location
            ORDER BY total DESC
        """)
        location_data = cursor.fetchall()

        cursor.close()
        connection.close()

        chart_labels = [row["location"] for row in location_data]
        chart_values = [
            float(row["average_price"] or 0)
            for row in location_data
        ]

        return render_template(
            "dashboard.html",
            stats=stats,
            location_data=location_data,
            chart_labels=chart_labels,
            chart_values=chart_values
        )

    except Exception as error:
        return f"Dashboard error: {error}", 500


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
