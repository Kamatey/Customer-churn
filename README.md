E-commerce Churn Prediction Model

This is a Machine Learning model that predicts which customers are likely to leave an e-commerce platform.
The model is built using best data science practice, including data collection,exploratory data analysis,
data preprocessing, modeling and hyperparameter tuning.

Problem Statement

The model aims at predicting customers who are likely to churn from an e-commerce platform.
Identifying customers who are likely to churn, the platform
can take proactive measures to retain those customers, such as offering
personalized discounts or improving the user experience.

Data

The model uses data from Kaggle website with 5630 rows and
20 columns.The data contains 5 categorical variables and 15 numerical 
variables.Comprehensive analysis was done on the data by visualizing the distribution
of the data and the relationship between variables.
The data was preprocessed and cleaned to remove any missing values.
The numerical variables was having missing values
and they were replaced by the median.
I chose to replacing the missing value over removing them
because of outliers.
The categorical features were engineered by using one hot encoder.


Modeling
Random forest and xgboost algorithms was used in the training.
The performance of the random forest was 0.56 and
xgboost was 0.65.




THE WEB APP.
The web app is user-friendly to the end users.
The app capability is to predict E-commerce churn base on
the input feature the model was trained on.
It was built using one of the python web frameworks Flask.

How to use it.

To be able to use this app, you have to first install the
packages that was used in building, to get that executed, run the 
command 'pip install -r requirement.txt' in the terminal. This will 
install all the packages needed to run this app.

After that, type the command 'python app.py' to start the server and run
the app. The server link will pop up, copy the link and
paste into a web browser to open the app or click on the 
link from the terminal to open it directly.

Now input the values to the features the model was trained on
in the input fields, click on the prdict button to see the result.
