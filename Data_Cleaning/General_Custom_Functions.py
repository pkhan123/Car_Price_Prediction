# general custom functions
# import libraries
import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from collections import Counter


# general custom functions
def General_Custom_Functions():
    print_statement = '''
    Available General Custom Functions: 

    Check_Missing_Values(input_dataset)
    Trim_Dataset(input_dataset)
    Check_Feature_Details(input_dataset, input_feature)
    Check_Correlation(input_dataset, input_feature_list)
    Check_Multicollinearity(input_dataset, input_feature_list)
    Create_Dummy_Variables(input_dataset, input_feature_list)
    Create_Feature_Selected_Dataset(input_dataset)

    '''
    return print(print_statement)

# check missing values
def Check_Missing_Values(input_dataset):
    missing_data = input_dataset.isnull().sum()
    missing_data_percentage = (missing_data*100/len(input_dataset)).round(2)
    data_Types = input_dataset.dtypes
    missing_data_df = pd.DataFrame({'Missing_Data': missing_data,
                                    'Missing_Data (%)': missing_data_percentage,
                                    'Data_Type': data_Types})
    return missing_data_df

# trim the dataset upto 1%
def Trim_Dataset(input_dataset):
    total_data_removed = 0
    initial_data_length = len(input_dataset.index)
    numerical_feature_list = list(input_dataset.select_dtypes(include=['float64', 'int64']).columns) 
    for numerical_feature in numerical_feature_list:
        low_removed_counter = 0
        high_removed_counter = 0
        initial_min_value = input_dataset[numerical_feature].min()
        initial_max_value = input_dataset[numerical_feature].max()
        initial_median_value = input_dataset[numerical_feature].median()
        min_cut = round(abs(initial_median_value - initial_min_value)/(abs(initial_max_value - initial_min_value)*100), 3)
        max_cut = round(abs(initial_max_value - initial_median_value)/(abs(initial_max_value - initial_min_value)*100), 3)
        min_quantile = round(input_dataset[numerical_feature].quantile(min_cut))
        max_quantile = round(input_dataset[numerical_feature].quantile(1-max_cut))
        lenght_before_quantile = len(input_dataset.index)
        for index, row in input_dataset.iterrows(): # drop row based on condition
            if row[numerical_feature] < min_quantile:
                input_dataset.drop(index, inplace=True)
                low_removed_counter = low_removed_counter + 1
            elif row[numerical_feature] > max_quantile:
                input_dataset.drop(index, inplace=True)
                high_removed_counter = high_removed_counter + 1
            else:
                pass
        lenght_after_quantile = len(input_dataset.index)
        data_removed = (lenght_before_quantile - lenght_after_quantile)
        total_data_removed = total_data_removed + data_removed
        data_removed_percentage = round((data_removed*100/initial_data_length), 2)
        total_data_removed_percentage = round((total_data_removed*100/initial_data_length), 2)
        final_min_value = input_dataset[numerical_feature].min()
        final_max_value = input_dataset[numerical_feature].max()
        final_median_value = input_dataset[numerical_feature].median()
        print('Feature: ', numerical_feature)
        print('Initial Min: ', initial_min_value, ' Initial Median: ', initial_median_value, ' Initial Max: ', initial_max_value)
        print('Min Cut: ', min_quantile, ' Max Cut: ', max_quantile)
        print('Data Removed: ', data_removed, '(',data_removed_percentage,'%)'
            ' Total Data Removed: ', total_data_removed, '(',total_data_removed_percentage,'%)')
        print('Low Value Removed: ', low_removed_counter, ' High Value Removed: ', high_removed_counter)
        print('Final Min: ', final_min_value, ' Final Median: ', final_median_value, ' Final Max: ', final_max_value)
        print('\n')




# check feature details
def Check_Feature_Details(input_dataset, input_feature):
    unique_features = input_dataset[input_feature].unique()
    print(unique_features)
    value_counts = input_dataset[input_feature].value_counts(ascending=False).head(10)
    value_counts_percentage = (value_counts*100/len(input_dataset)).round(2)
    feature_details_df = pd.DataFrame({'Value_Counts': value_counts,
                                    'Value_Counts (%)': value_counts_percentage})
    return feature_details_df

# check correlation 
def Check_Correlation(input_dataset, input_feature_list):
    local_dataset = input_dataset[input_feature_list]
    correlation_matrix = local_dataset.corr().abs()
    upper_traingular_part = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape),k=1).astype(np.bool_))
    unstacked_upper_traingular_part = upper_traingular_part.unstack()
    sorted_unstacked_upper_traingular_part = unstacked_upper_traingular_part.sort_values(ascending=False).head(10)
    print('Correlated pairs ... \n')
    print(sorted_unstacked_upper_traingular_part)
    temp_feature_list_to_drop = [column for column in upper_traingular_part.columns if any(upper_traingular_part[column] > 0.95)]
    print('\n\nFeature list to drop ...')
    return temp_feature_list_to_drop

# check Multicollinearity of numerical data
def Check_Multicollinearity(input_dataset, input_feature_list):
    vif_variables = input_dataset[input_feature_list]
    vif = pd.DataFrame()
    vif['VIF'] = [variance_inflation_factor(vif_variables.values, i) for i in range(vif_variables.shape[1])]
    vif['Features'] = vif_variables.columns
    vif = vif.sort_values(by=['VIF'], ascending=False)
    return vif

# create dummy variables for all the categorical variables
def Create_Dummy_Variables(input_dataset, input_feature_list):
    print('Creating dummies for top 10 levels in each feature having data more than 1% ...\n')
    # input_feature_list = input_dataset.columns.values.tolist()
    for input_feature in input_feature_list:
        one_percent = len(input_dataset)/100
        top_10_values = [x for x in input_dataset[input_feature].value_counts().sort_values(ascending=False).head(10).index]
        top_10_values_above_one_percent = [x for x in top_10_values if input_dataset[input_feature].value_counts()[x] > one_percent]
        print(top_10_values_above_one_percent)
        for label in top_10_values_above_one_percent:
            # if number of unique values is greater than 1 and less than 10
            # and level count greater than 1%
            if (1 < len(top_10_values_above_one_percent) <= 10): 
                input_dataset[str(input_feature)+'_'+str(label)] = np.where(input_dataset[input_feature]==label, 1, 0)
            else:
                print('Dummy not created for:', input_feature)
    input_dataset = input_dataset.drop(input_feature_list, axis = 1, inplace=True)
    return input_dataset

# create feature selected dataset
def Create_Feature_Selected_Dataset(input_dataset):
    localdataset = input_dataset.copy()
    X = localdataset.iloc[:, :-1]
    y = localdataset.iloc[:, -1]

    localdataset_list = localdataset.columns.values.tolist()
    X_feature_list = X.columns.values.tolist()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    # model = RandomForestRegressor()
    model = ExtraTreesRegressor()
    model.fit(X_train,y_train)

    feature_dictionary = {} # a dictionary to hold feature_name: feature_importance
    # lets make dictionary of features as per importance
    for feature, importance in zip(X_train.columns, model.feature_importances_):
        feature_dictionary[feature] = importance #add the name/value pair 
    sorted_feature_dictionary = sorted(feature_dictionary.items(), key=lambda x:x[1], reverse = True)

    # lets make a list of selected features
    local_counter = 0
    local_sum = 0
    important_feature_list = []
    for index, tuple in enumerate(sorted_feature_dictionary):
        if local_sum < 0.8:
            local_counter = local_counter + 1
            important_feature = tuple[0]
            importances = tuple[1]
            local_sum = local_sum + importances
            important_feature_list.append(important_feature)
        else:
            pass
    print('Selected features:', local_counter)
    print('Selected features total score:', local_sum)
    print(important_feature_list)
    feature_to_remove = list((Counter(X_feature_list) - Counter(important_feature_list)).elements())
    input_dataset = input_dataset.drop(feature_to_remove, axis = 1, inplace=True)
    return input_dataset
