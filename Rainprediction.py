from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
class RainPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, Temperature, Humidity, Wind_Speed, Cloud_Cover, Pressure):
        # Prepare input features
        input_features = [[Temperature, Humidity, Wind_Speed, Cloud_Cover, Pressure]]
        # Predict using the model
        prediction = self.model.predict(input_features)
        # Return the prediction result
        return "rain" if prediction[0] == 1 else "no rain"

# Initialize the RainPredictor with the path to your saved model
predictor = RainPredictor('D:\All Dtat Science Stuff\Regression Problem\model_joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the values from the form
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Wind_Speed = float(request.form['Wind_Speed'])
        Cloud_Cover = float(request.form['Cloud_Cover'])
        Pressure = float(request.form['Pressure'])

        # Get the prediction result from the model
        result = predictor.predict(Temperature, Humidity, Wind_Speed, Cloud_Cover, Pressure)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
