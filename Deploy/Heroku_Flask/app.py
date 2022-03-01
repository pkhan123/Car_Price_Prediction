from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
standard_scaler_pkl = pickle.load(open('catboost_standard_scaler.pkl', 'rb'))
regression_model_pkl = pickle.load(open('catboost_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':

        Brand_Name = request.form['Brand_Name']
        if(Brand_Name == 'Tesla'):
            Brand_Tesla = 1
            Brand_BMW = Brand_Mercedes_Benz = Brand_Lexus = Brand_Porsche = Brand_Audi = Brand_Land_Rover = 0
        elif(Brand_Name == 'BMW'):
            Brand_BMW = 1
            Brand_Tesla = Brand_Mercedes_Benz = Brand_Lexus = Brand_Porsche = Brand_Audi = Brand_Land_Rover = 0
        elif(Brand_Name == 'Mercedes_Benz'):
            Brand_Mercedes_Benz = 1
            Brand_Tesla = Brand_BMW = Brand_Lexus = Brand_Porsche = Brand_Audi = Brand_Land_Rover = 0
        elif(Brand_Name == 'Lexus'):
            Brand_Lexus = 1
            Brand_Tesla = Brand_BMW = Brand_Mercedes_Benz = Brand_Porsche = Brand_Audi = Brand_Land_Rover = 0
        elif(Brand_Name == 'Porsche'):
            Brand_Porsche = 1
            Brand_Tesla = Brand_BMW = Brand_Mercedes_Benz = Brand_Lexus = Brand_Audi = Brand_Land_Rover = 0
        elif(Brand_Name == 'Audi'):
            Brand_Audi = 1
            Brand_Tesla = Brand_BMW = Brand_Mercedes_Benz = Brand_Lexus = Brand_Porsche = Brand_Land_Rover = 0
        elif(Brand_Name == 'Land_Rover'):
            Brand_Land_Rover = 1
            Brand_Tesla = Brand_BMW = Brand_Mercedes_Benz = Brand_Lexus = Brand_Porsche = Brand_Audi = 0
        else:
            Brand_Tesla = Brand_BMW = Brand_Mercedes_Benz = Brand_Lexus = Brand_Porsche = Brand_Audi = Brand_Land_Rover = 0

        Body_Type = request.form['Body_Type']
        if(Body_Type == 'SUV'):
            Body_SUV = 1
            Body_TRUCKS = 0
        elif(Body_Type == 'TRUCKS'):
            Body_SUV = 0
            Body_TRUCKS = 1
        else:
            Body_SUV = Body_TRUCKS = 0

        Fuel_Type = request.form['Fuel_Type']
        if(Fuel_Type == 'Gasoline'):
            Fuel_Type_Gasoline = 1
        else:
            Fuel_Type_Gasoline = 0
            

        Car_Age = int(request.form['Car_Age'])
        Mileage = int(request.form['Mileage'])
        MPG_City = int(request.form['MPG_City'])
        Cylinder_Number = int(request.form['Cylinder_Number'])
        Wheel_Drive_Number = int(request.form['Wheel_Drive_Number'])

        list_X_test = [[Car_Age, MPG_City, Cylinder_Number, Brand_BMW, Brand_Land_Rover, Mileage, 999,
                        Body_TRUCKS, Brand_Lexus, Brand_Audi, Brand_Tesla, Brand_Mercedes_Benz,
                        Brand_Porsche, Fuel_Type_Gasoline, Body_SUV, Wheel_Drive_Number]]
        print(list_X_test)

        X_test = pd.DataFrame(list_X_test, columns = ['Car_Age', 'MPG_City', 'Cylinder_Number',
                                                    'Brand_BMW', 'Brand_Land Rover', 'Mileage',
                                                    'MPG_Highway', 'Body_TRUCKS', 'Brand_Lexus', 
                                                    'Brand_Audi', 'Brand_Tesla', 'Brand_Mercedes-Benz', 
                                                    'Brand_Porsche', 'Fuel_Type_Gasoline', 'Body_SUV', 
                                                    'Wheel_Drive_Number'])

        scaling_feature_list = ['Mileage', 'Cylinder_Number', 'Wheel_Drive_Number', 'MPG_City',
                                'MPG_Highway', 'Car_Age']

        X_test[scaling_feature_list] = standard_scaler_pkl.transform(X_test[scaling_feature_list])

        X_train_feature_list = ['Mileage', 'Cylinder_Number', 'Wheel_Drive_Number', 'MPG_City',
                                'Car_Age', 'Brand_Audi', 'Brand_BMW', 'Brand_Land Rover', 'Brand_Lexus',
                                'Brand_Mercedes-Benz', 'Brand_Porsche', 'Brand_Tesla', 'Body_SUV',
                                'Body_TRUCKS', 'Fuel_Type_Gasoline']

        X_test = X_test[X_train_feature_list]
        print(X_test)

        y_pred = regression_model_pkl.predict(X_test)
        
        output = round(y_pred[0])
        if output < 0:
            return render_template('index.html',prediction_texts='Sorry, prediction not available for this specifications.')
        else:
            return render_template('index.html',prediction_text='Estimated Car Price $ {}'.format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

