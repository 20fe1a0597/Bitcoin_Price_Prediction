from django.http import HttpResponse
import os
import joblib
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from django.conf import settings
from django.shortcuts import render

def train_svr_model(num_days):
    # Load historical Bitcoin price data and preprocess it
    bitcoin_data = pd.read_csv('BTC-USD.csv')
    bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])
    bitcoin_data.set_index('Date', inplace=True)

    # Split the data into training and testing sets
    train_data = bitcoin_data[:-num_days]
    test_data = bitcoin_data[-num_days:]

    # Train an SVR algorithm on the training data
    X_train = np.array(range(1, len(train_data) + 1)).reshape(-1, 1)
    y_train = train_data['Price'].values
    svr_model = SVR(kernel='rbf', C=1000, gamma=0.1)
    svr_model.fit(X_train, y_train)

    # Save the trained model to a file in the Django project
    filename =  'svr_model.sav'
    joblib.dump(svr_model,os.path.join(settings.BASE_DIR,filename))

def predict_bitcoin_price(num_days):
    # Load the saved SVR model from the file in the Django project
    svr_model = joblib.load(os.path.join(settings.BASE_DIR,'svr_model.sav'))

    # Predict Bitcoin price after the specified number of days
    X_test = np.array(range(1, num_days + 1)).reshape(-1, 1)
    predicted_price = svr_model.predict(X_test)

    return predicted_price[0]

def home(request):
    if request.method == 'POST':
        num_days = int(request.POST.get('days', 7))
        train_svr_model(num_days)
    else:
        num_days = int(request.GET.get('days', 7))
    
    predicted_price = predict_bitcoin_price(num_days)
    context = {
        'predicted_price': predicted_price,
        'num_days': num_days
    }
    return render(request, 'home.html', context)

def convertor(request):
    return render(request,"convertor.html")
