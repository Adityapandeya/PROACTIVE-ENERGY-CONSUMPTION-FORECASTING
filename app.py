from flask import Flask, render_template, request,url_for
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the form
    #datetime = request.form['datetime']
    nuclear = float(request.form['nuclear'])
    wind = float(request.form['wind'])
    hydroelectric = float(request.form['hydroelectric'])
    oil_gas = float(request.form['oil-gas'])
    coal = float(request.form['coal'])
    solar = float(request.form['solar'])
    biomass = float(request.form['biomass'])
    
    # Preprocess the input data (if needed)
    # Perform any necessary feature scaling or transformations
    
    # Make prediction using the machine learning model
    prediction = model.predict(np.array([[nuclear, wind, hydroelectric, oil_gas, coal, solar, biomass]]))
    
    # Format the prediction for display
    formatted_prediction = f'Predicted energy consumption: {prediction[0]:.2f}'

    total = nuclear + wind + hydroelectric + oil_gas + coal + solar + biomass

    # Pass the prediction to the HTML template
    return render_template('predict.html', prediction_result=formatted_prediction, production = total)

if __name__ == '__main__':
    app.run(debug=True)
