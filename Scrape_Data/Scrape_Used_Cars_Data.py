# %% [markdown]
# # Scrape Used Cars Data

# %%
# scrape used cars data from autotrader.com

# %% [markdown]
# ## Step-1: Import Libraries

# %%
import pandas as pd
import numpy as np
import importlib 
import shutil
import os


# %% [markdown]
# ## Step-2: Scraping Multiple Pages to Get 500 Results

# %% [markdown]
# Necessary Data
# - brand 
# - model
# - body
# - certification
# - exterior_color
# - interior_color
# - transmission_type
# - fuel_type
# - engine_type
# - wheel_drive_type
# - miles_per_gallon
# - year
# - zip_code
# - mileage
# - price

# %%
# search city
# 800
city = 'New York'
# city = 'Los Angeles'
# city = 'Chicago'
# city = 'Houston'
# city = 'Phoenix'

# 700
# city = 'Philadelphia'
# city = 'San Antonio'
# city = 'San Diego'
# city = 'Dallas'
# city = 'San Jose'

# 600
# city = 'Austin' 
# city = 'Jacksonville'
# city = 'Fort Worth'
# city = 'Columbus'
# city = 'Indianapolis'

# 500
# city = 'Charlotte'
# city = 'San Francisco'
# city = 'Seattle'
# city = 'Denver'
# city = 'Washington'

# 500
# city = 'Boston'
# city = 'Las Vegas'
# city = 'Detroit'
# city = 'Miami'
# city = 'Nashville'
# city = 'Oklahoma City'
# city = 'El Paso'
# city = 'Portland'
# city = 'Memphis'
# city = 'Louisville'
# city = 'Baltimore'
# city = 'Milwaukee'
# city = 'Albuquerque'
# city = 'Tucson'
# city = 'Fresno'
# city = 'Sacramento'
city_string = city.replace(' ', '_')


# %%
# import custom module from Curl_Python_XYZ.py
custom_module_name = f'Curl_Python_{city_string}'
print(custom_module_name)
imported_custom_module = importlib.import_module(custom_module_name)



# %%
# each page has 25 result
# for 500 result need 20 pages
# 800 -> 32 | 700 -> 28 | 600 -> 24 | 500 -> 20 
page_to_scroll = 20


# %%
brand = []
model = []
body = []
certification = []
exterior_color = []
interior_color = []
transmission_type = []
fuel_type = []
engine_type = []
wheel_drive_type = []
miles_per_gallon = []
year = []
zip_code = []
mileage = []
price = []

# %%
# may take up to 1-2 min to run this cell
for page in range(1,page_to_scroll+1):
    #print page to scroll
    print(page)

    # call curl_python_function from curl_python.py for each page and create esponse
    response = imported_custom_module.Curl_Python(page)

    # create response json object
    response_json_object = response.json()

    # result items
    result_items = response_json_object['listings']

    # iterate over result items
    for result in result_items:

        # brand
        brand.append(result['make'])

        # model
        model.append(result['model'])

        # body
        body.append(result['bodyStyleCodes'][0])

        # certification
        certification.append(result['type'])

        # exterior color
        if result.get('specifications', {}).get('color', {}).get('value') != None:
            exterior_color.append(result['specifications']['color']['value'])
        else:
            exterior_color.append(np.nan)

        # interior color
        if result.get('specifications', {}).get('interiorColor', {}).get('value') != None:
            interior_color.append(result['specifications']['interiorColor']['value'])
        else:
            interior_color.append(np.nan)

        # transmission type
        if result.get('specifications', {}).get('transmission', {}).get('value') != None:
            transmission_type.append(result['specifications']['transmission']['value'])
        else:
            transmission_type.append(np.nan)

        # fuel type
        fuel_type.append(result['fuelType'])

        # engine type
        engine_type.append(result['specifications']['engine']['value'])

        # wheel drive type
        if result.get('specifications', {}).get('driveType', {}).get('value') != None:
            wheel_drive_type.append(result['specifications']['driveType']['value'])
        else:
            wheel_drive_type.append(np.nan)

        # miles per gallon
        if result.get('specifications', {}).get('mpg', {}).get('value') != None:
            miles_per_gallon.append(result['specifications']['mpg']['value'])
        else:
            miles_per_gallon.append(np.nan)

        # year
        year.append(result['year'])

        # zip code
        zip_code.append(result['zip'])

        # mileage
        if result.get('specifications', {}).get('mileage', {}).get('value') != None:
            mileage.append(result['specifications']['mileage']['value'])
        else:
            mileage.append(np.nan)

        # price
        price.append(result['pricingDetail']['salePrice'])



# may take up to 1-2 min to run this cell

# %% [markdown]
# ## Step-3: Create Pandas Dataframe for Multiple Page

# %%
df_multiple_page = pd.DataFrame({'City': city, 'Brand': brand, 'Model': model, 'Body': body,
                                'Certification': certification, 'Exterior_Color': exterior_color,
                                'Interior_Color': interior_color, 'Transmission_Type': transmission_type,
                                'Fuel_Type': fuel_type, 'Engine_Type': engine_type,
                                'Wheel_Drive_Type': wheel_drive_type, 'Miles_Per_Gallon': miles_per_gallon,
                                'Year': year, 'Zip_Code': zip_code, 'Mileage': mileage, 'Price':price})

# %%
# display data frame
df_multiple_page.head()

# %%
df_multiple_page.shape

# %% [markdown]
# ## Step-4: Export Data to XLSX and CSV File

# %%
# export the data to a xlsx file
df_multiple_page.to_excel(f'Used_Cars_Dataset_{city_string}.xlsx', index=False)

# %%
shutil.move(f'Used_Cars_Dataset_{city_string}.xlsx', 'Dataset/XLSX')

# %%
# export the data to a csv file
df_multiple_page.to_csv(f'Used_Cars_Dataset_{city_string}.csv', index=False)

# %%
shutil.move(f'Used_Cars_Dataset_{city_string}.csv', 'Dataset/CSV')

# %%



