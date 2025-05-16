from flask import Flask , render_template, request
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)
df=pd.read_csv('data_cleaned.csv')

pipe=pickle.load(open("MainModel.pkl","rb"))
@app.route('/')
def index():
    locations=sorted(df['location'].unique())
    return render_template('index.html',locations=locations)



@app.route('/predict',methods=['POST'])
def predict():
    locations=request.form.get('location')

    bhk=request.form.get('bhk')

    bath=request.form.get('bath')

    sqft=request.form.get('sqft')


    input=pd.DataFrame([[locations,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])

    prediction=pipe.predict(input)[0]
    return str(np.round(prediction,2))

if __name__=="__main__":
    app.run(debug=True,port=5000)