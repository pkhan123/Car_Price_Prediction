# specific custom functions
# import libraries
import numpy as np


# specific custom functions
def Specific_Custom_Functions():
    print_statement = '''
    Available Specific Custom Functions: 
    
    Extract_Cylinder_Number(engine_type_string)
    Extract_Wheel_Drive_Number(wheel_drive_type_string) 
    Extract_MPG_City(miles_per_gallon_string)
    Extract_MPG_Highway(miles_per_gallon_string)

    '''
    return print(print_statement)

# extract the cylinder number from the Engine_Type
def Extract_Cylinder_Number(engine_type_string):
    if isinstance(engine_type_string, str):
        probable_cylinder_number = engine_type_string.split('-')[0]
        cylinder_number = probable_cylinder_number if probable_cylinder_number.isdigit() else np.nan
        cylinder_number = float(cylinder_number)
    else:
        cylinder_number = np.nan
    return cylinder_number

# extract the wheel drive number from the Wheel_Drive_Type
def Extract_Wheel_Drive_Number(wheel_drive_type_string):
    if isinstance(wheel_drive_type_string, str):
        probable_wheel_drive_number = wheel_drive_type_string.split(' ')[0]
        if probable_wheel_drive_number.isdigit():
            wheel_drive_number = probable_wheel_drive_number
            wheel_drive_number = float(wheel_drive_number)
        elif probable_wheel_drive_number == 'All':
            wheel_drive_number = 4
        else:
            wheel_drive_number = np.nan
    else:
        wheel_drive_number = np.nan
    return wheel_drive_number

# extract miles per gallon in city from the Miles_Per_Gallon
def Extract_MPG_City(miles_per_gallon_string):
    if isinstance(miles_per_gallon_string, str):
        mpg_split_list = miles_per_gallon_string.split(' ')
        number_list = [int(i) for i in mpg_split_list if i.isdigit()]
        mpg_city = number_list[0] if number_list else np.nan
    else:
        mpg_city = np.nan
    return mpg_city

# extract miles per gallon in highway from the Miles_Per_Gallon
def Extract_MPG_Highway(miles_per_gallon_string):
    if isinstance(miles_per_gallon_string, str):
        mpg_split_list = miles_per_gallon_string.split(' ')
        number_list = [int(i) for i in mpg_split_list if i.isdigit()]
        mpg_highway = number_list[1] if number_list else np.nan
    else:
        mpg_highway = np.nan
    return mpg_highway
