# Rain Prediction Project

This project uses machine learning to predict whether it will rain based on input features such as temperature, humidity, wind speed, and others.

## Live Demo

You can access the live prediction app here: (http://127.0.0.1:5000/) 

##Rain Prediction Project Explanation
This project is a Rain Prediction System that uses machine learning to predict whether it will rain based on various environmental parameters. The system takes input values like temperature, humidity, wind speed, cloud cover, and pressure, processes them using a pre-trained machine learning model, and outputs whether it will rain or not.

Overview
Objective: Predict whether it will rain based on input features like temperature, humidity, wind speed, cloud cover, and pressure.
Machine Learning Model: A machine learning model (such as a Random Forest, Logistic Regression, or Decision Tree classifier) is trained using historical weather data. The model is then used to predict rainfall.
Input Features:
Temperature: The current temperature (in °C).
Humidity: The relative humidity in percentage.
Wind Speed: The speed of wind in meters per second.
Cloud Cover: The percentage of cloud cover in the sky.
Pressure: The atmospheric pressure (in hPa).
Model Training
Data Collection: The dataset used for training consists of historical weather data, including the features mentioned above and the target variable (whether it rained or not).

Model Selection and Training: Various machine learning models (e.g., Random Forest, Support Vector Machine, or Decision Trees) can be used. The model is trained on historical data to learn the relationship between input features (like temperature, humidity, etc.) and the target variable (whether it rains or not).

Saving the Model: Once the model is trained and validated, it is saved to a file (e.g., .pkl or .joblib). This saved model is later used for making predictions.

Web Application (Flask App)
Flask Framework: A Python web framework called Flask is used to create a simple web application that allows users to interact with the model. The app presents a form where users can input values for temperature, humidity, wind speed, cloud cover, and pressure.

HTML Form: The web page contains an HTML form where users enter the values for the features. Upon submission, the values are sent to the Flask backend to be processed.

Predicting Rain: When the form is submitted, the app uses the input values to:

Load the pre-trained machine learning model.
Make predictions based on the input values.
Return the prediction (either "rain" or "no rain").
Flask Route: The web application has a route (/) that handles both GET and POST requests:

On a GET request (when the page is initially loaded), the form is displayed.
On a POST request (when the form is submitted), the input values are passed to the model for prediction.
Result Display: After prediction, the result (either "rain" or "no rain") is displayed on the same web page.

Code Structure
app.py:

Contains the logic for loading the model, making predictions, and handling web requests (using Flask).
index.html:

Contains the HTML form where users input the weather data (temperature, humidity, etc.) and display the result.
Machine Learning Model:

The pre-trained machine learning model is saved as a .pkl or .joblib file and is loaded when the web application starts.
Technologies Used
Python: The programming language used to build the machine learning model and web application.
Flask: A lightweight Python web framework used to create the web app.
Joblib or Pickle: Used to save and load the trained machine learning model.
HTML/CSS: Used to create and style the user interface for the web form.
Machine Learning Libraries: Scikit-learn or other ML libraries for training and using the model (e.g., RandomForestClassifier, LogisticRegression).
How It Works
The user visits the web page.
The user fills in the weather data (temperature, humidity, wind speed, cloud cover, and pressure) in the form and submits it.
The Flask app receives the input data, processes it, and feeds it to the pre-trained machine learning model.
The model outputs a prediction (rain or no rain).
The result is displayed on the web page.
