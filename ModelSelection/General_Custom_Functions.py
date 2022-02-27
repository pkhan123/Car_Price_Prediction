# general custom functions
# import libraries

import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# general custom functions
def General_Custom_Functions():
    print_statement = '''
    Available General Custom Functions: 
    Check_Missing_Values(input_dataset)
    Move_Column_Last(input_dataset, target_variable)
    Check_Feature_Details(input_dataset, input_feature)
    Rearrange_Features(input_X_train, input_y_train)
    Check_Correlation(input_X_train)
    Check_Multicollinearity(input_X_train, numerical_feature_list)
    Make_Feature_Selection(input_X_train, input_y_train, max_validation_round)
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

# move column to last of dataframe
def Move_Column_Last(input_dataset, target_variable):
    local_y = input_dataset[target_variable].copy()
    input_dataset.rename(columns={target_variable: 'change_name'}, inplace=True)
    input_dataset[target_variable] = local_y
    input_dataset = input_dataset.drop('change_name', axis = 1, inplace=True)
    return input_dataset

# check feature details
def Check_Feature_Details(input_dataset, input_feature):
    unique_features = input_dataset[input_feature].unique()
    print(unique_features)
    value_counts = input_dataset[input_feature].value_counts(ascending=False).head(10)
    value_counts_percentage = (value_counts*100/len(input_dataset)).round(2)
    feature_details_df = pd.DataFrame({'Value_Counts': value_counts,
                                    'Value_Counts (%)': value_counts_percentage})
    return feature_details_df

# rearange features as per feature importance
def Rearrange_Features(input_X_train, input_y_train):
    model = RandomForestRegressor(random_state = 42)
    model.fit(input_X_train,input_y_train)
    feature_dictionary = {} 
    for feature, importance in zip(input_X_train.columns, model.feature_importances_):
        feature_dictionary[feature] = importance 
    sorted_feature_dictionary = sorted(feature_dictionary.items(), key=lambda x:x[1], reverse = True)
    rearranged_feature_list = []
    for index, tuple in enumerate(sorted_feature_dictionary):
        important_feature = tuple[0]
        rearranged_feature_list.append(important_feature)
    with open('rearranged_feature_list.txt', 'w') as f:
        for item in rearranged_feature_list:
            f.write('%s\n' % item)



# check correlation
def Check_Correlation(input_X_train):
    max_correlation = 0.90
    X_train_feature_list = input_X_train.columns.values.tolist()
    correlation_matrix = input_X_train.corr().abs()
    upper_traingular_part = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape),k=1).astype(np.bool_))
    unstacked_upper_traingular_part = upper_traingular_part.unstack()
    sorted_unstacked_upper_traingular_part = unstacked_upper_traingular_part.sort_values(ascending=False).head(10)
    print('Top 10 correlated pairs ... \n')
    print(sorted_unstacked_upper_traingular_part) 
    highly_correlated_feature_list = [column for column in upper_traingular_part.columns if any(upper_traingular_part[column] > max_correlation)]
    correlation_qualified_feature_list = list((Counter(X_train_feature_list) - Counter(highly_correlated_feature_list)).elements())
    # input_X_train = input_X_train.drop(temp_feature_list_to_drop, axis = 1, inplace=True)
    print('\nFeature dropped: ')
    print(highly_correlated_feature_list)
    with open('correlation_qualified_feature_list.txt', 'w') as f:
        for item in correlation_qualified_feature_list:
            f.write('%s\n' % item)
    print('Correlation qualified features: ', len(correlation_qualified_feature_list))


# check multicollinearity
def Check_Multicollinearity(input_X_train, numerical_feature_list):
    check_value = 999
    feature_to_drop = []
    input_X_train_list = input_X_train.columns.values.tolist()
    local_X_train = input_X_train[numerical_feature_list].copy()
    local_X_train_list = local_X_train.columns.values.tolist()
    # scale the dataset
    standard_scaler = StandardScaler()
    local_X_train[local_X_train_list] = standard_scaler.fit_transform(local_X_train[local_X_train_list])
    while check_value > 5:
        vif_dataset = local_X_train[local_X_train_list].copy()
        vif = pd.DataFrame()
        vif['VIF'] = [variance_inflation_factor(vif_dataset.values, i) for i in range(vif_dataset.shape[1])]
        vif['Features'] = vif_dataset.columns
        vif = vif.sort_values(by=['VIF'], ascending=False)
        first_row_VIF = vif['VIF'].iloc[0]
        first_row_feature = vif['Features'].iloc[0]
        check_value = first_row_VIF
        if first_row_VIF > 5:
            print(first_row_VIF, first_row_feature)
            drop_list = [first_row_feature]
            feature_to_drop.append(first_row_feature)
            local_X_train_list = list((Counter(local_X_train_list) - Counter(drop_list)).elements())
        else:
            print('VIFs < 5 ... OK')
    print('\nFeature dropped: ')
    print(feature_to_drop)
    # input_X_train = input_X_train.drop(feature_to_drop, axis = 1, inplace=True)
    multicollinearity_qualified_feature_list = list((Counter(input_X_train_list) - Counter(feature_to_drop)).elements())
    with open('multicollinearity_qualified_feature_list.txt', 'w') as f:
        for item in multicollinearity_qualified_feature_list:
            f.write('%s\n' % item)
    print('Multicollinearity qualified features: ', len(multicollinearity_qualified_feature_list))
    return print(vif)

# make feature selection
def Make_Feature_Selection(input_X_train, input_y_train, max_validation_round):
    print('Freature selection using RandomForestRegressor ...')
    max_random_state = 100
    round_counter = 0
    execute_round = 1
    validation_round = 0
    list_of_important_feature_lists = []
    selected_feature_list = []

    for random_state in range(1, max_random_state+1, 1): # default: 10 random_state
        if (execute_round == 1 or validation_round < max_validation_round):
            round_counter = round_counter + 1
            print('\nRound Counter: ', round_counter)
            
            # train test split
            X_train, X_test, y_train, y_test = train_test_split(input_X_train, input_y_train,
                                                                test_size = 0.2, random_state = random_state)
            X_train_feature_list = X_train.columns.values.tolist()

            model = RandomForestRegressor(random_state = random_state*random_state)
            model.fit(X_train,y_train)
            # print top 10 features
            feature_importances = pd.Series(model.feature_importances_, index=X_train.columns)
            if round_counter == 1: print('Top 10 features: ')
            if round_counter == 1: print(feature_importances.nlargest(10))
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
                important_feature = tuple[0]
                importances = tuple[1]
                # conditional loop to select number of features
                if importances > 0.005: # (min: 0.001, default: 0.005, max: 0.010)
                    local_counter = local_counter + 1
                    local_sum = local_sum + importances
                    important_feature_list.append(important_feature)
                else:
                    pass
            
            list_of_important_feature_lists.append(important_feature_list)
            common_elements_in_all_lists = list(set.intersection(*map(set, list_of_important_feature_lists)))
            if set(selected_feature_list) != set(common_elements_in_all_lists):
                dropped_this_round = list((Counter(selected_feature_list) - Counter(common_elements_in_all_lists)).elements())
                selected_feature_list = common_elements_in_all_lists
                execute_round = 1
                validation_round = 0
            else:
                dropped_this_round = []
                execute_round = 0
                validation_round = validation_round + 1

            print('Random State: ', random_state, '\tSelected features: ', local_counter, '\tImportance: ', local_sum)
            if round_counter == 1: print(important_feature_list)
            print('Total common features up to this round:', len(selected_feature_list), '\tValidation Round:', validation_round)
            print('Dropped this round: ', dropped_this_round)
            if (execute_round == 1 or validation_round < max_validation_round):
                print('Execute Next Round: Yes')
            else:
                print('Execute Next Round: No')

        else:
            pass

    feature_to_remove = list((Counter(X_train_feature_list) - Counter(common_elements_in_all_lists)).elements())
    # input_X_train = input_X_train.drop(feature_to_remove, axis = 1, inplace=True)
    print('\nFeature dropped during final selection: ')
    list_of_all_important_features = list({x for l in list_of_important_feature_lists for x in l})
    important_feature_removed = list((Counter(list_of_all_important_features) - Counter(common_elements_in_all_lists)).elements())
    print(important_feature_removed)
    with open('selected_feature_list.txt', 'w') as f:
        for item in selected_feature_list:
            f.write('%s\n' % item)
    print('Final selected features:', len(selected_feature_list))
    print('Final list of selected features: ')
    print(selected_feature_list)

    

