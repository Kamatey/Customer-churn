from flask import Flask, render_template, request
import pandas
import xgboost
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
app = Flask(__name__)
modell = open('xgb_model2.pkl', 'rb')
model = pickle.load(modell)
modell.close()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    global pred
    global result
    if request.method == "POST":
        CashbackAmount = float(request.form['CashbackAmount'])
        WarehouseToHome = float(request.form['WarehouseToHome'])
        OrderAmountHikeFromlastYear = float(request.form['OrderAmountHikeFromlastYear'])
        Tenure = float(request.form['Tenure'])
        DaySinceLastOrder = float(request.form['DaySinceLastOrder'])
        NumberOfAddress = float(request.form['NumberOfAddress'])
        SatisfactionScore = float(request.form['SatisfactionScore'])
        CityTier = float(request.form['CityTier'])
        Complain = float(request.form['Complain'])
        NumberOfDeviceRegistered = float(request.form['NumberOfDeviceRegistered'])
        arg = [CashbackAmount, WarehouseToHome, OrderAmountHikeFromlastYear, Tenure, DaySinceLastOrder,NumberOfAddress,SatisfactionScore,CityTier,Complain,NumberOfDeviceRegistered]
        arg = np.asarray(arg)
        arg = arg.reshape(1, -1)
        #arg = scaler.fit_transform(arg)
        pred = model.predict(arg)

        def result():
            if pred == 0:
                return 'Potential of staying on the platform'
            if pred == 1:
                return 'Potential of leaving the platform'



    return render_template('predict.html', pred=pred, result=result())


if __name__ == "__main__":
    app.run()



