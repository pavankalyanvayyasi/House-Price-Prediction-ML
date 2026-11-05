# House Price Prediction Using Machine Learning

## Project Overview

The House Price Prediction System is a Machine Learning-based web application that predicts house prices based on property information such as area, number of bedrooms, bathrooms, construction year and location.

The application uses Python, Flask and Machine Learning to generate price predictions and provides an interactive analytics dashboard to visualize prediction statistics.

## Key Features

- House price prediction using Machine Learning.
- Property information input form.
- Location-based price prediction.
- Interactive analytics dashboard.
- Total, average, highest and lowest prediction statistics.
- Average house price by location visualization.
- Prediction history management.
- MySQL database integration.
- Responsive web interface.

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- MySQL
- HTML
- CSS
- JavaScript
- Chart.js
- Git and GitHub

## Project Structure

    House Price Prediction/
    |
    |-- dataset/
    |   |-- house_data.csv
    |
    |-- model/
    |   |-- templates/
    |   |   |-- dashboard.html
    |   |   |-- history.html
    |   |   |-- index.html
    |   |   |-- result.html
    |   |
    |   |-- app.py
    |   |-- house_price_model.pkl
    |
    |-- generate_dataset.py
    |-- train_model.py
    |-- requirements.txt
    |-- .gitignore
    |-- README.md

## Installation and Setup

### Step 1: Clone the Repository

    git clone YOUR_GITHUB_REPOSITORY_URL

### Step 2: Navigate to the Project

    cd "House Price Prediction"

### Step 3: Create Virtual Environment

    python -m venv venv

### Step 4: Activate Virtual Environment

Windows:

    venv\Scripts\activate

### Step 5: Install Dependencies

    pip install -r requirements.txt

### Step 6: Configure MySQL

Configure your MySQL database connection and required database and table settings in model/app.py.

### Step 7: Run the Application

    cd model
    python app.py

### Step 8: Open in Browser

    http://127.0.0.1:5000/

## Dashboard Features

The analytics dashboard displays:

- Total Predictions
- Average House Price
- Highest Predicted Price
- Lowest Predicted Price
- Average Price by Location

## Testing

The application was tested for:

- Successful Flask application startup.
- House price prediction functionality.
- Prediction result display.
- Dashboard statistics.
- Location-based price visualization.
- Prediction history storage and retrieval.
- Successful saving of new predictions.

## Project Objective

The objective of this project is to develop a Machine Learning-based house price prediction application that provides estimated property prices and useful analytics through an interactive web interface.

## Author

Pavan Kalyan

Computer Science Engineering Graduate

## Conclusion

This project demonstrates practical knowledge of Python programming, Machine Learning, Flask web development, SQL database integration and data visualization.