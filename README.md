![image](https://github.com/Ignatiocalvin/flight_predictions/assets/50834160/4b94c951-e0fa-459f-a444-869ebb3a3dc2)

![link](https://docs.google.com/document/d/1Ae0xtEXFEMzhun0KKtgLBYkRW7adbTQI28qCInSYUVk/edit?usp=sharing)

## 🔨 1. The Problem
Flight delays are grave problems for both passengers and airlines. While there are many factors that contribute to flight delays, dangerous weather like storms, fog, and high wind speeds plays an undoubtedly significant role. Fortunately, there are vast amounts of data pertaining to weather and aviation recorded by meteorology stations and airports. Therefore, with the correct application of data processing and machine learning, we would be able to build a model that could aid in predicting flight delays based on weather conditions.


## 📊 2. Data
The dataset we took is published on Kaggle. [1] Jen Wadkins, who provided the dataset, merged datasets from the Bureau of Transportation Statistics [2] and the National Center for Environmental Information (NCEI) [3]. Reporting carriers are required to report on-time data for flights they operate: on-time arrival and departure data for non-stop domestic flights by month and year, by carrier, and by origin and destination airport. Whereas meteorological information, provided by the NCEI, is derived from designated stations or sites at airports equipped with meteorological instrumentation. These stations range from automated observing equipment providing hourly data to volunteer observers collecting daily precipitation measurements. Our aim is to forecast whether an aircraft will experience a departure delay exceeding 15 minutes, labeled as 1, or a delay of 15 minutes or less, labeled as 0, as denoted in the column “DEP_DEL15”. The dataset has 26 columns and over 6.5 million rows.

## 🕯 3. Solving the Problem
We are building a classification model in order to predict whether the flight is delayed or not. There are several factors that may affect the cancellation of the flight like weather conditions, technical issues that may arise before the flight, the duration of flight, etc. Here is a step-by-step outline of how we are going to solve this problem:


  ### 3.1. Data Collection and Preprocessing:
The first step is to gather relevant data. The dataset that we took provides a diverse set of features including weather conditions, flight duration, the age of the aircraft, and airport details. 
Data preprocessing is an essential part of this phase where we are dealing with missing values, outliers, or any inconsistencies in our dataset. We also perform feature engineering to convert columns like DEP_TIME_BLK into numerical values. Another main issue is the unbalanced data since approximately 23 % of the flights are delayed. Since the class imbalance is not extreme, we use oversampling to balance the dataset. 
  ### 3.2. Data Visualization:
The next important step is to visualize our data in order to understand underlying patterns and relationships in the dataset. Data visualization helps us to identify factors that may influence the flight delays such as the day of the week, weather conditions, and plane age.
  ### 3.3. Feature and Model Selection:
Not all the features are important for predicting flight delays. We will remove the columns that won’t be useful for predicting flight delay such as CARRIER_NAME, and PREVIOUS_AIRPORT. 
Model selection is another vital step since it affects the model’s performance, and accuracy and addresses specific problems. For this project, we will try different models to obtain the best possible outcome. Here are the models that we are going to try:
Random Forest can offer high predictive accuracy by capturing complex interactions in flight delays. Moreover, it’s less prone to overfitting and computationally efficient. 
XGBoost can provide excellent accuracy and can often outperform other algorithms. It is also good at handling noisy data. 

  ### 3.4. Model Training and Tuning :
In this phase, we are going to train our selected model on pre-processed data. Our primary goal in this phase is to improve the model's accuracy. For the Random Forest, we focus on optimizing the hyperparameters n_estimators and max_depth to obtain the right balance between model complexity and overfitting. Additionally, for the XGBoost model, we optimize n_estimators, max_depth, and learning_rate to improve its performance. To achieve these optimizations, we used cross-validation as a technique to fine-tune our models for optimal results. 

## 🏆 4. Measure of Success
To measure the success of the models trained, We are using two different evaluation techniques. The first is the F1 score since the output class (DEP_DEL15) is highly unbalanced. The number of flights that got delayed represents 19% of the feature while the ones that did not get delayed represent 81%. So one value is approximately four times the other. When one class dominates the other, the F1 score is very useful, giving a better measurement when dealing with imbalanced class problems. The second one is the accuracy. The dual evaluation approach can help make more informed decisions about the model.

## 🛩 5. Expected Results
The outcome of this project is to use a binary classification model that takes in all kinds of flight details along with the temperature and predicts if the flight is going to be delayed or not. Aside from that, we strive to find the best model and hyperparameter combinations that yield the best evaluation score.
