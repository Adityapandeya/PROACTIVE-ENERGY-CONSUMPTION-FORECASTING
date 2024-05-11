# PROACTIVE-ENERGY-CONSUMPTION-FORECASTING


This project focuses on predicting  energy consumption, which is crucial for effective energy management and sustainability. By analyzing historical data, we aim to develop a model that can accurately forecast energy usage, helping energy providers and policymakers make informed decisions.

## Dataset Description

The dataset contains daily electricity consumption data over a specified time period. It includes features such as date and time, total electricity production, consumption, and various renewable and non-renewable energy sources.

## Exploratory Data Analysis (EDA)

During the exploratory data analysis, we performed the following tasks:
- Checked for missing values and outliers in the dataset
- Visualized the data using histograms, line plots, and scatter plots
- Extracted temporal features such as day of the week, month, and season

## Feature Engineering

We applied feature engineering techniques to create new features that could help improve the model's predictive accuracy. For example, we extracted features such as day of the week, month, and season from the date and time column to account for temporal patterns.

## Model Selection and Training

We chose the Random Forest Regressor model for its ability to handle non-linear relationships and interactions between features effectively. We split the dataset into training and testing sets and trained the model using the training data.

## Model Evaluation

We evaluated the performance of the trained model using metrics such as mean squared error (MSE) and R-squared (R²) score on the testing set. Additionally, we considered other evaluation metrics such as accuracy, precision, and recall.

## Hyperparameter Tuning

We used GridSearchCV to systematically search for the optimal hyperparameters of the Random Forest Regressor model. Cross-validation was employed to ensure the robustness of the selected hyperparameters.

## Deployment

We deployed our predictive model using Flask on the Render platform. The frontend was developed using HTML and CSS, while the backend was implemented in Python. Dependencies such as Jinja2, NumPy, Flask, and Gunicorn were installed for deployment.

## Future Work

Some potential future directions for our project include incorporating additional features such as weather data, improving model performance through ensemble methods, and exploring the use of deep learning algorithms for more complex predictions.

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Render

## Website URL

[EnergySage](www.energysage4.onrender.com)

## Author

Aditya pandey

