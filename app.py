from flask import Flask, render_template, request
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime
import gspread
import pandas as pd
import pickle
import numpy as np


# load model
model = pickle.load(open('model.pkl','rb'))

#function to get current time  
def date_now():
    now = datetime.now()
    mydate = datetime.strftime(now , '%Y-%m-%d %H:%M:%S')
    return mydate

# app
app = Flask(__name__, template_folder='UI')

# routes
@app.route('/',  methods=['GET'])
def home():
    return render_template("index.html")

if __name__ == '__home__':
    app.run(port = 5000, debug=True)