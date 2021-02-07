#import libraries
import numpy as np 
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#ignore warnings
import warnings
warnings.filterwarnings('ignore')


#import data
df = pd.read_csv("./data/cleaned_data_with2.csv",index_col=0)

df = df.drop(['Year'],axis=1)

X = df.drop(['Price'], axis=1)
y = df['Price']  #target variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42,shuffle=True)


norm_cols = ['Millage','Ratings','Age']

# fit scaler on training data
nm = MinMaxScaler()

nm.fit(X_train[norm_cols])


#One Hot encoding for History and Transmission

ohe = ce.OneHotEncoder(cols=['History','Transmission'])  #instantiate the one-hot encoder

X_train = ohe.fit_transform(X_train)  #fit and transform ohe


# encodings for city, Make and Model
be = ce.BaseNEncoder(cols=['city','Make','Model'],base=3)

# fit and transform and you will get the encoded data
X_train = be.fit_transform(X_train)

