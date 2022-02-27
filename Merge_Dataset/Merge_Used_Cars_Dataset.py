# %% [markdown]
# # Merge Datasets and Export To PostgreSQL

# %% [markdown]
# ## Step-1: Imports Libraries

# %%
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import glob
import shutil
from MyCredentials import My_Credentials

# %% [markdown]
# ## Step-2: Import dataset and merge

# %%
# specifying the path to csv files
csv_path = '/Users/pluto/Documents/Code/Test/Used_Cars_Price_Prediction/Scrape_Data/Dataset/CSV'

# %%
# csv files in the path
csv_files = glob.glob(csv_path + "/*.csv")

# %%
# defining an empty list to store content
content = []

# %%
# reading all the csv files in the specified path
for filename in csv_files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

# %%
# converting content to data frame
data_frame = pd.DataFrame()
data_frame = pd.concat(content)

# %%
data_frame.head()

# %%
data_frame.shape

# %% [markdown]
# ## Step-3: Export Dataset to PostgreSQL Database

# %%
# copy the dataset
df_merged_used_cars_dataset = data_frame.copy()

# %% [markdown]
# ### Export to Excel and CSV File

# %%
df_merged_used_cars_dataset.to_excel('Raw_Used_Cars_Dataset.xlsx', index=False)

# %%
shutil.move('Raw_Used_Cars_Dataset.xlsx', 'Dataset/Merged')

# %%
df_merged_used_cars_dataset.to_csv('Raw_Used_Cars_Dataset.csv', index=False)

# %%
shutil.move('Raw_Used_Cars_Dataset.csv', 'Dataset/Merged')

# %% [markdown]
# ### Upload file to PostgreSQL table

# %%
username = My_Credentials.username
password = My_Credentials.password
hostname = My_Credentials.hostname
port = My_Credentials.port
database = 'Used_Cars_Database'


# %%
# create sqlalchemy engine and connect to PostgreSQL server
engine=create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

# %%
if database_exists(engine.url):
    print('Database exists!')
else:
    create_database(engine.url)
    print('Database created!')

# %%
try:
    df_merged_used_cars_dataset.to_sql('Raw_Used_Cars_Dataset', engine, if_exists= 'replace', index= False)
    print('Data uploaded to PostgreSQL table')

except:
    print("Sorry, some error has occurred!")

finally:
    engine.dispose()

# %%



