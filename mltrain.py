
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

def binaryf (x):
    return x.map({'yes':1,'no':0})

def prep_data():
    housing=pd.read_csv("data/Housing.csv")
    varlist=['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea']
    housing[varlist]=housing[varlist].apply(binaryf)
    status=pd.get_dummies(housing['furnishingstatus'],drop_first = True)
    housing=pd.concat([housing,status],axis=1)
    housing=housing.drop(['furnishingstatus'],axis=1)
    np.random.seed(0)
    df_train,df_test=train_test_split(housing,train_size=0.7,random_state=100)
    scaler=MinMaxScaler()
    num_vars=['price','area','bedrooms','bathrooms','stories','parking']
    df_train[num_vars]=scaler.fit_transform(df_train[num_vars])
    y=df_train.pop('price')
    x=df_train
    lr=LinearRegression()
    lr.fit(x,y)
    pickle.dump(lr,open('model1.pkl','wb'))

    y_test=df_test.pop('price')
    x_test=df_test
    pickled_model=pickle.load(open('model1.pkl','rb'))
    y_test_pred=pickled_model.predict(x_test)
    y_test_pred=pd.DataFrame(data=y_test_pred,columns=['pred'])
    X_pred_final_test=pd.concat((x_test,y_test_pred),axis=0)
    X_pred_final_test.to_csv("data/file.csv")
    return '10'
