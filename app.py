from flask import Flask, render_template, request
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime
import gspread
import pandas as pd
import pickle
import numpy as np
import xgboost as xgb


# load model
model = pickle.load(open('model.pkl','rb'))

#function to get current time  
def date_now():
    now = datetime.now()
    mydate = datetime.strftime(now , '%Y-%m-%d %H:%M:%S')
    return mydate

# app
app = Flask(__name__, template_folder='templates',
            static_folder='static')

# routes
@app.route('/',  methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/result',  methods=['POST'])
def predict():
    if request.method == 'POST':
        # get data and convert data into dataframe
        Millage = request.form['Millage']
        History = request.form['History']
        Model_Year = request.form['Model-Year']
        Transmission = request.form['Transmission']
        Make = request.form['Make']
        Model = request.form['Model']
        Ratings = request.form['Ratings']
        City = request.form['City']
         
        year = time.strftime("%Y")
        Age = year - Model_Year
        
        
        
        data_df = pd.DataFrame([[Millage,History,Age,Transmission,Make,Model,Ratings,City]],
                               columns=['Millage','History','Age','Transmission','Make','Model','Ratings','City'])
        # predictions
        output = model.predict(data_df)
        #result = np.int(np.round(output))
        
    # return data
    return render_template("index.html#result",prediction=output)


if __name__ == '__home__':
    app.run(port = 5000, debug=True)