import streamlit as st
import pandas as pd
import pickle


# load the pickle files
regression_model_pkl = pickle.load(open('catboost_regression_model.pkl','rb'))

# wide layout
st.set_page_config(layout='wide')

# hide main menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                    overflow: hidden; /* Hide scrollbars */
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

container1 = st.container()
container2 = st.container()
container3 = st.container()

with container1:
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
with container2:
    col8, col9 = st.columns([2, 6])
with container3:
    col10, col11, col12 = st.columns([1, 1, 1])


# initalize the feature values
Brand_Tesla, Brand_BMW, Brand_Mercedes_Benz, Wheel_Drive_Number, Mileage = 0, 0, 0, 0, 0
Brand_Lexus, MPG_Highway, Body_TRUCKS, Cylinder_Number, Brand_Land_Rover = 0, 0, 0, 0, 0
Fuel_Type_Gasoline, Car_Age, Brand_Porsche, Body_SUV, Brand_Audi = 0, 0, 0, 0, 0

with col1:
    Brand_Name = st.selectbox('Brand Name',options=['BMW', 'Mercedes-Benz', 'Lexus', 'Audi', 'Land Rover', 
                                                    'Porsche', 'Tesla',  'Other']) 
with col2:
    Body_Type = st.selectbox('Body Type',options=['SUV', 'TRUCKS', 'Other'])
with col3:    
    Fuel_Type = st.selectbox('Fuel Type',options=['Gasoline', 'Other'])

    
with col8:
    Mileage = st.slider('Mileage (Miles)', 0, 100000, 24000, 1)
    Car_Age = st.slider('How Old Car (Year)', 0, 10, 3, 1)
    MPG_Highway = st.slider('Miles Per Gallon (Highway)', 15, 40, 28, 1)
    Cylinder_Number = st.slider('Cylinder Number', 3, 8, 4, 1)
    Wheel_Drive_Number = st.slider('Wheel Drive Number', 2, 4, 2, 1)
    

# assign Brand_Name values
if Brand_Name == 'BMW':
    Brand_BMW = 1
elif Brand_Name == 'Mercedes-Benz':
    Brand_Mercedes_Benz = 1
elif Brand_Name == 'Lexus':
    Brand_Lexus = 1
elif Brand_Name == 'Audi':
    Brand_Audi = 1
elif Brand_Name == 'Land Rover':
    Brand_Land_Rover = 1
elif Brand_Name == 'Porsche':
    Brand_Porsche = 1
elif Brand_Name == 'Tesla':
    Brand_Tesla = 1
else:
	pass

# assign Body_Type values
if Body_Type == 'SUV':
    Body_SUV = 1
elif Body_Type == 'TRUCKS':
    Body_TRUCKS = 1
else:
	pass

# assign Fuel_Type values
if Fuel_Type == 'Gasoline':
    Fuel_Type_Gasoline = 1
else:
	pass

# feature list
feature_list = ['Brand_Tesla', 'Brand_BMW', 'Brand_Mercedes-Benz', 'Wheel_Drive_Number', 'Mileage', 
                'Brand_Lexus', 'MPG_Highway', 'Body_TRUCKS', 'Cylinder_Number', 'Brand_Land Rover', 
                'Fuel_Type_Gasoline', 'Car_Age', 'Brand_Porsche', 'Body_SUV', 'Brand_Audi']
# print(feature_list)

# feature values
feature_values = [[Brand_Tesla, Brand_BMW, Brand_Mercedes_Benz, Wheel_Drive_Number, Mileage, 
                    Brand_Lexus, MPG_Highway, Body_TRUCKS, Cylinder_Number, Brand_Land_Rover, 
                    Fuel_Type_Gasoline, Car_Age, Brand_Porsche, Body_SUV, Brand_Audi]]
X_test = pd.DataFrame(feature_values, columns = feature_list)
# print(X_test)

def predict(input_X_test, input_model):
    # predict the output
    y_pred = input_model.predict(input_X_test)
    output = round(y_pred[0])
    return output


n_min = 0
n_max = 100000

list_Mileage = []
list_Brand_BMW = []
list_Brand_Mercedes_Benz = []
list_Brand_Lexus = []
list_Brand_Audi = []
list_Brand_Land_Rover = []
list_Brand_Porsche = []
list_Brand_Tesla = []
list_Other = []


for x in range(n_min, n_max+1, 1000):
    Mileage = x
    list_Mileage.append(Mileage)

    feature_values_BMW = [[0, 1, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]
    feature_values_Mercedes_Benz = [[0, 0, 1, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]
    feature_values_Lexus = [[0, 0, 0, Wheel_Drive_Number, Mileage, 1, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]
    feature_values_Audi = [[0, 0, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]
    feature_values_Land_Rover = [[0, 0, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 1, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]
    feature_values_Porsche = [[0, 0, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 1, Body_SUV, 0]]
    feature_values_Tesla = [[1, 0, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 1]]
    feature_values_Other = [[0, 0, 0, Wheel_Drive_Number, Mileage, 0, MPG_Highway, Body_TRUCKS, Cylinder_Number, 0, Fuel_Type_Gasoline, Car_Age, 0, Body_SUV, 0]]

    output_Brand_BMW = predict(feature_values_BMW, regression_model_pkl)
    output_Brand_Mercedes_Benz = predict(feature_values_Mercedes_Benz, regression_model_pkl)
    output_Brand_Lexus = predict(feature_values_Lexus, regression_model_pkl)
    output_Brand_Audi = predict(feature_values_Audi, regression_model_pkl)
    output_Brand_Land_Rover = predict(feature_values_Land_Rover, regression_model_pkl)
    output_Brand_Porsche = predict(feature_values_Porsche, regression_model_pkl)
    output_Brand_Tesla = predict(feature_values_Tesla, regression_model_pkl)
    output_Other = predict(feature_values_Other, regression_model_pkl)

    list_Brand_BMW.append(output_Brand_BMW)
    list_Brand_Mercedes_Benz.append(output_Brand_Mercedes_Benz)
    list_Brand_Lexus.append(output_Brand_Lexus)
    list_Brand_Audi.append(output_Brand_Audi)
    list_Brand_Land_Rover.append(output_Brand_Land_Rover)
    list_Brand_Porsche.append(output_Brand_Porsche)
    list_Brand_Tesla.append(output_Brand_Tesla)
    list_Other.append(output_Other)
    

line_chart_dataframe = pd.DataFrame(dict(
    Mileage=list_Mileage,
    BMW = list_Brand_BMW,
    Mercedes_Benz = list_Brand_Mercedes_Benz,
    Lexus = list_Brand_Lexus,
    Audi = list_Brand_Audi,
    Land_Rover = list_Brand_Land_Rover,
    Porsche = list_Brand_Porsche,
    Tesla = list_Brand_Tesla,
    Other = list_Other
))

line_chart_dataframe = line_chart_dataframe.rename(columns={'Mileage':'index'}).set_index('index')


with col9:
    chart_title = '<p style="font-family:Courier; font-size: 20px; text-align: left;">Mileage vs Price Chart</p>'
    st.markdown(chart_title, unsafe_allow_html=True)
    st.line_chart(line_chart_dataframe)
    # chart_label = '<p style="font-family:Courier; font-size: 15px; text-align: left;">Mileage ⟶</p>'
    # st.markdown(chart_label, unsafe_allow_html=True)
    output_result = predict(X_test, regression_model_pkl)
    output_text = '<p style="font-family:Courier; color:#0074D9; font-size: 20px; text-align: center;">Predicted Price</p>'
    st.markdown(output_text, unsafe_allow_html=True)
    output_value = f'<p style="font-family:Courier; color:#0074D9; font-size: 30px; text-align: center;">$ {output_result}</p>'
    st.markdown(output_value, unsafe_allow_html=True)
    



