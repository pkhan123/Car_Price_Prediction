# %% [markdown]
# # Data Cleaning

# %% [markdown]
# ## Step-1: Import Libraries

# %% [markdown]
# ### Import the necessary base libraries

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ### Import visualization libraries

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %% [markdown]
# ### Import the general custom functions

# %%
# import general custom data preprocessing functions
from General_Custom_Functions import *
General_Custom_Functions()

# %% [markdown]
# ### Import the specific custom functions

# %%
# import specific custom data preprocessing functions
from Specific_Custom_Functions import *
Specific_Custom_Functions()

# %% [markdown]
# ## Step-2: Import Dataset

# %% [markdown]
# ### Connect to PostgreSQL server

# %%
from MyCredentials import My_Credentials
username = My_Credentials.username
password = My_Credentials.password
hostname = My_Credentials.hostname
port = My_Credentials.port
database = 'Used_Cars_Database'

# %%
# create sqlalchemy engine and connect to PostgreSQL server
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
engine=create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

# %% [markdown]
# ### Import the data into pandas dataframe

# %%
# read data from PostgreSQL
if database_exists(engine.url):
    dataset = pd.read_sql('SELECT * FROM public."Raw_Used_Cars_Dataset"', engine)
    print('Database exists ... ')
else:
    print('Database does not exist!')

# %% [markdown]
# ### Data Exploration

# %%
# fast look of the data set
dataset.head()

# %%
# shape of the datset
dataset.shape

# %%
# check missing values
Check_Missing_Values(dataset)

# %%
Check_Feature_Details(dataset, 'Fuel_Type')

# %%
# copy the dataset into a new dataframe for further processing
imported_dataset = dataset.copy()


# %% [markdown]
# ## Step-3: Data Formating

# %% [markdown]
# ### Extract numerical data

# %%
Check_Missing_Values(imported_dataset)

# %%
# check feature details
Check_Feature_Details(imported_dataset, 'Engine_Type')

# %%
# now let's extract numerical values from some categorical data columns one by one
imported_dataset.loc[:, 'Cylinder_Number'] = imported_dataset.loc[:, 'Engine_Type'].apply(Extract_Cylinder_Number)
imported_dataset.loc[:, 'Wheel_Drive_Number'] = imported_dataset.loc[:, 'Wheel_Drive_Type'].apply(Extract_Wheel_Drive_Number)
imported_dataset.loc[:, 'MPG_City'] = imported_dataset.loc[:, 'Miles_Per_Gallon'].apply(Extract_MPG_City)
imported_dataset.loc[:, 'MPG_Highway'] = imported_dataset.loc[:, 'Miles_Per_Gallon'].apply(Extract_MPG_Highway)


# %%
# convert Year to Car_Age
imported_dataset['Current_Year'] = 2022
imported_dataset['Car_Age'] = imported_dataset['Current_Year'] - imported_dataset['Year']


# %% [markdown]
# ### Change data type

# %%
# convert Zip_Code to object
imported_dataset['Zip_Code'] = imported_dataset['Zip_Code'].astype(str)

# %%
# now convert the mileage and price column to float
imported_dataset['Mileage'] = imported_dataset['Mileage'].str.replace(',','').astype(float)
imported_dataset['Price'] = imported_dataset['Price'].astype(float)

# %%
Check_Missing_Values(imported_dataset)

# %%
imported_dataset.columns

# %%
# now we will only keep the relevant columns, order them and drop others
formatted_dataset = imported_dataset[['Brand', 'Model', 'Body', 'Certification',
                                   'Exterior_Color', 'Interior_Color', 'Transmission_Type', 'Fuel_Type',
                                   'City', 'Zip_Code', 'Mileage', 'Cylinder_Number',
                                   'Wheel_Drive_Number', 'MPG_City', 'MPG_Highway', 'Car_Age',
                                   'Price']].copy()

# %% [markdown]
# ## Step-4: Clean Dataset

# %% [markdown]
# ### Check the probability distribution function of numerical features

# %%
# A great step in the data exploration is to display the probability distribution 
# function (PDF) of a variable. The PDF will show us how that variable is distributed 
# This makes it very easy to spot anomalies, such as outliers
# The PDF is often the basis on which we decide whether we want to transform a feature
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=3, figsize=(20, 30))
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(ncols=2, nrows=4, sharey=False, figsize =(20,40))
sns.histplot(formatted_dataset['Mileage'], ax=ax1)
sns.histplot(formatted_dataset['Cylinder_Number'], ax=ax2)
sns.histplot(formatted_dataset['Wheel_Drive_Number'], ax=ax3)
sns.histplot(formatted_dataset['MPG_City'], ax=ax4)
sns.histplot(formatted_dataset['MPG_Highway'], ax=ax5)
sns.histplot(formatted_dataset['Car_Age'], ax=ax6)
sns.histplot(formatted_dataset['Price'], ax=ax7)
sns.histplot(formatted_dataset['Price'], ax=ax8)
plt.show()

# %% [markdown]
# ### Clean the dataset by removing the outliers

# %%
# trim the dataset to remove the outliers
Trim_Dataset(formatted_dataset)

# %%
# after removing the outliers, lets check the PDFs again
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=3, figsize=(20, 30))
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(ncols=2, nrows=4, sharey=False, figsize =(20,40))
sns.histplot(formatted_dataset['Mileage'], ax=ax1)
sns.histplot(formatted_dataset['Cylinder_Number'], ax=ax2)
sns.histplot(formatted_dataset['Wheel_Drive_Number'], ax=ax3)
sns.histplot(formatted_dataset['MPG_City'], ax=ax4)
sns.histplot(formatted_dataset['MPG_Highway'], ax=ax5)
sns.histplot(formatted_dataset['Car_Age'], ax=ax6)
sns.histplot(formatted_dataset['Price'], ax=ax7)
sns.histplot(formatted_dataset['Price'], ax=ax8)
plt.show()

# %%
Check_Missing_Values(formatted_dataset)

# %%
formatted_dataset.shape

# %% [markdown]
# ## Step-5: Cleaned Dataset

# %%
# now lets create cleaned_dataset
cleaned_dataset = formatted_dataset.copy()

# %%
cleaned_dataset.shape

# %%
# now let's check the dependence of y with selected features
# since Price is the 'y' axis of all the plots, it made sense to plot them side-by-side (so we can compare them)
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=3, figsize=(20, 30))
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(ncols=2, nrows=3, sharey=True, figsize =(20,30))
ax1.scatter(cleaned_dataset['Mileage'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax1.set_title('Mileage and Price')
ax2.scatter(cleaned_dataset['Cylinder_Number'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax2.set_title('Cylinder_Number and Price')
ax3.scatter(cleaned_dataset['Wheel_Drive_Number'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax3.set_title('Wheel_Drive_Number and Price')
ax4.scatter(cleaned_dataset['MPG_City'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax4.set_title('MPG_City and Price')
ax5.scatter(cleaned_dataset['MPG_Highway'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax5.set_title('MPG_Highway and Price')
ax6.scatter(cleaned_dataset['Car_Age'],cleaned_dataset['Price'], s=100, facecolors='none', edgecolors='r', alpha=0.2)
ax6.set_title('Car_Age and Price')
plt.show()


# %% [markdown]
# ## Step-6: Export Cleaned Dataset

# %%
cleaned_dataset.describe(include='all')

# %%
# check feature details
Check_Feature_Details(cleaned_dataset, 'Certification')

# %% [markdown]
# ### Export cleaned data to XLSX and CSV file

# %%
cleaned_dataset.to_excel('Cleaned_Dataset.xlsx', index=False)

# %%
cleaned_dataset.to_csv('Cleaned_Dataset.csv', index=False)

# %% [markdown]
# ### Export cleaned data to PostgreSQL

# %%
# now cleaned_dataset will be exported to PostgreSQL table 
try:
    cleaned_dataset.to_sql('Cleaned_Dataset', engine, if_exists= 'replace', index= False)
    print('Data uploaded to PostgreSQL table')

except:
    print("Sorry, some error has occurred!")

finally:
    engine.dispose()

# %%



