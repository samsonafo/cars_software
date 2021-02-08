from flask import Flask, render_template, request
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import pickle
import numpy as np
import xgboost as xgb
import time
from encoder import nm,ohe,be


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
        city = request.form['City']
         
        year = time.strftime("%Y")
        Age = int(year) - int(Model_Year)
        
        
        
        data_df = pd.DataFrame([[city,History,Millage,Ratings,Make,Model,Transmission,Age]],
                               columns=['city','History','Millage','Ratings','Make','Model','Transmission','Age'])
        
        
        #encodings
        
        norm_cols = ['Millage','Ratings','Age']
        
        # normalize cols
        data_df.loc[:,norm_cols] = nm.transform(data_df[norm_cols])
        
        #one hot encoding
        data_df = ohe.transform(data_df)
        
        #base encoder
        data_df = be.transform(data_df)
        
        # predictions
        output = model.predict(data_df)
        output = np.int(np.round(output,decimals=2)*1000000) #price was divided by a million to build the model
        output = "{:,}".format(output) 
        
    # return data
    return render_template("index.html",prediction=output) #output sent here


if __name__ == '__home__':
    app.run(port = 5000, debug=True)